"""POST /webcall/session: the browser game's session mint."""

from datetime import time
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from pehchana import db
from pehchana.api import webcall
from pehchana.api.deps import get_arms, get_bolna
from pehchana.arms import Arm, LiveHours, LiveWindow
from pehchana.config import Settings, get_settings
from pehchana.models import Call, CallStatus, Channel

ALL_DAYS = frozenset({"mon", "tue", "wed", "thu", "fri", "sat", "sun"})
ALWAYS = LiveHours(ZoneInfo("UTC"), (LiveWindow(ALL_DAYS, time(0, 0), time(23, 59, 59)),))
HUMAN = Arm("human", "human", "H", None, 1.0, dial_numbers=("+911",), live_hours=ALWAYS)
VOICE_A = Arm("kalpa", "ai", "Voice A", "Kalpa", 1.0, bolna_agent_id="agent-a")
VOICE_B = Arm("cartesia", "ai", "Voice B", "Cartesia", 1.0, bolna_agent_id="agent-b")
PHONE_ONLY = Arm("sarvam", "ai", "Voice C", "Sarvam", 1.0, dial_numbers=("+913",))
SESSION = {"session_id": "s-1", "ice_servers": [{"urls": "turn:x"}], "expires_in": 120}
OK = {"consent": True}


class FakeBolna:
    def __init__(self, result=SESSION):
        self.result = result
        self.minted: list[tuple[str, dict]] = []

    def mint_web_call_session(self, agent_id, user_data=None):
        self.minted.append((agent_id, user_data))
        if isinstance(self.result, BaseException):
            raise self.result
        return self.result


@pytest.fixture
def game(client):
    """(client, fake Bolna, set(arms=..., **settings)) with fresh rate limits."""
    webcall.reset_limits()
    fake = FakeBolna()
    app = client.app

    def configure(arms=(VOICE_A,), **settings):
        app.dependency_overrides[get_arms] = lambda: list(arms)
        app.dependency_overrides[get_settings] = lambda: Settings(**settings)

    configure()
    app.dependency_overrides[get_bolna] = lambda: fake
    yield client, fake, configure
    app.dependency_overrides.clear()
    webcall.reset_limits()


def calls() -> list[Call]:
    with db.get_sessionmaker()() as s:
        return list(s.scalars(select(Call)))


@pytest.mark.parametrize("body", [{}, {"consent": False}, {"consent": "yes"}])
def test_no_session_without_consent(game, body):
    client, fake, _ = game
    assert client.post("/webcall/session", json=body).status_code == 422
    assert fake.minted == [] and calls() == []


def test_mints_a_session_for_an_ai_arm_and_records_a_web_call(game):
    client, fake, _ = game
    r = client.post("/webcall/session", json=OK)
    assert r.status_code == 200
    assert r.json() == SESSION  # Bolna's JSON goes back unchanged
    (call,) = calls()
    assert (call.channel, call.status, call.arm_id, call.arm_kind) == (
        Channel.WEB,
        CallStatus.ROUTED,
        "kalpa",
        "ai",
    )
    assert call.caller_hash is None
    assert fake.minted == [("agent-a", {"call_id": call.id})]


def test_user_data_from_the_browser_is_ignored(game):
    client, fake, _ = game
    body = {**OK, "user_data": {"call_id": "someone-else", "name": "{{system}}"}}
    assert client.post("/webcall/session", json=body).status_code == 200
    (call,) = calls()
    assert fake.minted == [("agent-a", {"call_id": call.id})]


def test_never_a_human_or_a_phone_only_arm(game):
    client, fake, configure = game
    configure(arms=(HUMAN, PHONE_ONLY, VOICE_A, VOICE_B), webcall_per_ip=50)
    for _ in range(30):
        assert client.post("/webcall/session", json=OK).status_code == 200
    assert {agent for agent, _ in fake.minted} == {"agent-a", "agent-b"}
    assert {c.arm_id for c in calls()} == {"kalpa", "cartesia"}


def test_no_ai_arm_for_the_web_means_503(game):
    client, fake, configure = game
    configure(arms=(HUMAN, PHONE_ONLY))
    assert client.post("/webcall/session", json=OK).status_code == 503
    assert fake.minted == [] and calls() == []


def test_per_client_limit(game, client):
    _, fake, configure = game
    configure(webcall_per_ip=2)
    assert [client.post("/webcall/session", json=OK).status_code for _ in range(3)] == [
        200,
        200,
        429,
    ]
    # another client still gets in
    other = TestClient(client.app, client=("203.0.113.9", 5000))
    assert other.post("/webcall/session", json=OK).status_code == 200
    assert len(fake.minted) == 3


def test_limit_window_slides(game, monkeypatch):
    client, _, configure = game
    configure(webcall_per_ip=1, webcall_per_ip_window_s=60)
    clock = iter([1000.0, 1030.0, 1061.0])
    monkeypatch.setattr(webcall, "_clock", lambda: next(clock))
    assert client.post("/webcall/session", json=OK).status_code == 200
    assert client.post("/webcall/session", json=OK).status_code == 429  # 30 s later
    assert client.post("/webcall/session", json=OK).status_code == 200  # 61 s later


def test_site_wide_hourly_cap_does_not_use_up_the_clients_own_limit(game, client):
    _, _, configure = game
    configure(webcall_per_ip=2, webcall_per_hour=1)
    assert client.post("/webcall/session", json=OK).status_code == 200
    other = TestClient(client.app, client=("203.0.113.9", 5000))
    assert other.post("/webcall/session", json=OK).status_code == 429
    configure(webcall_per_ip=2, webcall_per_hour=5)
    # the refused try above did not count against this client
    assert [other.post("/webcall/session", json=OK).status_code for _ in range(3)] == [
        200,
        200,
        429,
    ]


def test_mint_not_built_yet_is_501_and_the_call_fails(game):
    client, fake, _ = game
    fake.result = NotImplementedError()
    assert client.post("/webcall/session", json=OK).status_code == 501
    (call,) = calls()
    assert call.status == CallStatus.FAILED and call.ended_at is not None


def test_bolna_error_is_502_and_the_call_fails(game):
    client, fake, _ = game
    fake.result = RuntimeError("bolna said 500 for key bn-secret")
    r = client.post("/webcall/session", json=OK)
    assert r.status_code == 502
    assert "bn-secret" not in r.text
    (call,) = calls()
    assert call.status == CallStatus.FAILED
    assert call.processing_error == "session mint failed: RuntimeError"
