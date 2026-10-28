"""Production guard rails: what stops a deploy with dev secrets from serving callers."""

from pathlib import Path

import pytest
import yaml
from fastapi.testclient import TestClient
from typer.testing import CliRunner

from pehchana.cli import app
from pehchana.config import Settings, get_settings
from pehchana.main import create_app

GOOD = {
    "ENV": "prod",
    "ADMIN_TOKEN": "a" * 32,
    "CALLER_HASH_SALT": "b" * 32,
    "BOLNA_SHARED_SECRET": "c" * 32,
    "PLIVO_AUTH_TOKEN": "plivo-token",
    "PUBLIC_BASE_URL": "https://pk.example.com",
    "DATABASE_URL": "postgresql://pk:pw@db.example.com/pk",
    "CORS_ORIGINS": '["https://pk.example.com"]',
    "INCLUDE_DEMO_DATA": "false",
}


@pytest.fixture
def prod_env(monkeypatch):
    """Set environment variables for one test, with the settings cache cleared around it."""

    def apply(**overrides: str) -> None:
        for key, value in {**GOOD, **overrides}.items():
            monkeypatch.setenv(key, value)
        get_settings.cache_clear()

    yield apply
    monkeypatch.undo()
    get_settings.cache_clear()


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        ("postgres://u:p@h:5432/db", "postgresql+psycopg://u:p@h:5432/db"),
        ("postgresql://u:p@h/db", "postgresql+psycopg://u:p@h/db"),
        ("postgresql+psycopg://u:p@h/db", "postgresql+psycopg://u:p@h/db"),
        ("sqlite:///./pehchana.db", "sqlite:///./pehchana.db"),
    ],
)
def test_host_style_database_urls_get_the_driver_we_ship(given, expected):
    assert Settings(database_url=given).database_url == expected


def test_dev_defaults_are_not_fit_for_production():
    problems = " | ".join(Settings().production_problems())
    for needle in (
        "ADMIN_TOKEN",
        "CALLER_HASH_SALT",
        "BOLNA_SHARED_SECRET",
        "PLIVO_AUTH_TOKEN",
        "https://",
        "SQLite",
    ):
        assert needle in problems


def test_a_complete_configuration_has_no_problems(prod_env):
    prod_env()
    assert get_settings().production_problems() == []


@pytest.mark.parametrize(
    ("override", "fragment"),
    [
        ({"ADMIN_TOKEN": "short"}, "ADMIN_TOKEN is shorter"),
        ({"CALLER_HASH_SALT": "change-me"}, "CALLER_HASH_SALT is unset"),
        ({"PUBLIC_BASE_URL": "http://pk.example.com"}, "https://"),
        ({"DATABASE_URL": "sqlite:///x.db"}, "SQLite"),
        ({"INCLUDE_DEMO_DATA": "true"}, "INCLUDE_DEMO_DATA"),
        ({"PLIVO_AUTH_TOKEN": ""}, "PLIVO_AUTH_TOKEN"),
    ],
)
def test_each_unsafe_setting_is_named(prod_env, override, fragment):
    prod_env(**override)
    assert any(fragment in p for p in get_settings().production_problems())


def test_warnings_do_not_block(prod_env):
    prod_env(CORS_ORIGINS='["http://localhost:3000"]')
    settings = get_settings()
    assert settings.production_problems() == []
    assert any("CORS_ORIGINS" in w for w in settings.production_warnings())
    assert any("CONSENT_AUDIO_URL" in w for w in settings.production_warnings())


def test_prod_refuses_to_boot_with_dev_secrets(prod_env):
    prod_env(ADMIN_TOKEN="change-me")
    with (
        pytest.raises(RuntimeError, match=r"refusing to start in production.*ADMIN_TOKEN"),
        TestClient(create_app()),
    ):
        pass


def test_prod_boots_with_a_complete_configuration(prod_env):
    prod_env()
    with TestClient(create_app()):
        pass  # lifespan ran: no migration in prod, that is a deploy step


def test_check_config_command(prod_env):
    runner = CliRunner()
    prod_env()
    ok = runner.invoke(app, ["check-config"])
    assert ok.exit_code == 0 and "fit for production" in ok.output
    prod_env(ADMIN_TOKEN="change-me", PUBLIC_BASE_URL="http://x")
    bad = runner.invoke(app, ["check-config"])
    assert bad.exit_code == 1
    assert "ADMIN_TOKEN" in bad.output and "https://" in bad.output


# --- render.yaml: the Blueprint must set what the production guard demands ---------

ROOT = Path(__file__).resolve().parents[2]
SECRETS = {"ADMIN_TOKEN", "CALLER_HASH_SALT", "BOLNA_SHARED_SECRET"}


def _blueprint_env() -> dict[str, dict]:
    spec = yaml.safe_load((ROOT / "render.yaml").read_text())
    return {e["key"]: e for e in spec["services"][0]["envVars"]}


def test_blueprint_env_keys_are_ones_the_app_reads():
    arms = yaml.safe_load((ROOT / "bolna" / "arms.yaml").read_text())
    arm_envs = {
        a[k] for a in arms["arms"] for k in ("dial_numbers_env", "bolna_agent_id_env") if a.get(k)
    }
    known = {name.upper() for name in Settings.model_fields} | arm_envs
    assert set(_blueprint_env()) <= known


def test_blueprint_generates_secrets_and_never_hardcodes_them():
    env = _blueprint_env()
    for key in SECRETS:
        assert env[key] == {"key": key, "generateValue": True}
    for key in ("PLIVO_AUTH_TOKEN", "BOLNA_API_KEY", "DEEPGRAM_API_KEY", "ANTHROPIC_API_KEY"):
        assert env[key].get("sync") is False and "value" not in env[key]


def test_blueprint_satisfies_the_production_guard(prod_env):
    env = _blueprint_env()
    assert env["ENV"]["value"] == "prod"
    assert env["INCLUDE_DEMO_DATA"]["value"] == "false"
    assert "fromDatabase" in env["DATABASE_URL"]
    for key in ("PUBLIC_BASE_URL", "PLIVO_AUTH_TOKEN", "CORS_ORIGINS"):
        assert key in env  # prompted for: the guard refuses to boot without them
