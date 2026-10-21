"""Scaffold checks: the app boots, routes exist, config files parse."""

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]


def test_healthz(client):
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_contract_routes_are_registered(client):
    paths = set(client.get("/openapi.json").json()["paths"])
    expected = {
        "/telephony/plivo/answer",
        "/telephony/plivo/dial-status",
        "/telephony/plivo/recording",
        "/bolna/webhook",
        "/bolna/fn/accuse",
        "/webcall/session",
        "/leaderboard",
        "/admin/shift",
        "/admin/calls/{call_id}/reprocess",
    }
    assert expected <= paths


def test_arms_yaml_is_valid():
    data = yaml.safe_load((REPO / "bolna" / "arms.yaml").read_text())
    ids = [a["id"] for a in data["arms"]]
    assert len(ids) == len(set(ids))
    assert sum(a["kind"] == "human" for a in data["arms"]) == 1
    for arm in data["arms"]:
        assert arm["kind"] in {"human", "ai"}
        assert "dial_numbers_env" in arm


def test_accuse_function_schema_is_valid():
    import json

    schema = json.loads((REPO / "bolna" / "functions" / "accuse_bot.json").read_text())
    assert schema["key"] == "custom_task"
    assert schema["value"]["method"] in {"GET", "POST"}
    assert schema["name"] == "accuse_bot"
