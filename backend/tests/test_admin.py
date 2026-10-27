from datetime import UTC, datetime, time, timedelta
from zoneinfo import ZoneInfo

import pytest

from pehchana import db
from pehchana.api.deps import get_arms
from pehchana.arms import Arm, LiveHours, LiveWindow
from pehchana.config import get_settings
from pehchana.models import ShiftOverride
from pehchana.telephony import call_flow

ALL_DAYS = frozenset({"mon", "tue", "wed", "thu", "fri", "sat", "sun"})
# Open every minute of every day: only an override can close it.
ALWAYS = LiveHours(ZoneInfo("UTC"), (LiveWindow(ALL_DAYS, time(0, 0), time(23, 59, 59)),))
NEVER = Arm("human", "human", "H", None, 1.0, dial_numbers=("+911",))  # no live hours
OPEN = Arm("human", "human", "H", None, 1.0, dial_numbers=("+911",), live_hours=ALWAYS)
AI = Arm("kalpa", "ai", "Voice A", "Kalpa", 1.0, dial_numbers=("+913",), bolna_agent_id="a")


@pytest.fixture
def admin(client):
    """(client, auth headers); the arms in play are set per test with ``use_arms``."""
    client.app.dependency_overrides[get_arms] = lambda: [NEVER, AI]
    yield client, {"Authorization": f"Bearer {get_settings().admin_token}"}
    client.app.dependency_overrides.clear()


def use_arms(client, *arms: Arm) -> None:
    client.app.dependency_overrides[get_arms] = lambda: list(arms)


@pytest.mark.parametrize("method", ["get", "post"])
def test_shift_needs_the_admin_token(admin, method):
    client, _ = admin
    kwargs = {"json": {"humans_on_shift": True, "hours": 1}} if method == "post" else {}
    send = getattr(client, method)
    assert send("/admin/shift", **kwargs).status_code == 401
    assert (
        send("/admin/shift", headers={"Authorization": "Bearer wrong"}, **kwargs).status_code == 401
    )
    assert send("/admin/shift", headers={"Authorization": "Basic x"}, **kwargs).status_code == 401


def test_post_stores_an_override_that_routing_uses(admin):
    client, headers = admin
    body = {"humans_on_shift": True, "hours": 2, "set_by": "mahak"}
    assert client.post("/admin/shift", json=body, headers=headers).status_code == 200
    with db.get_sessionmaker()() as s:
        row = call_flow.current_shift_override(s, datetime.now(UTC))
        assert (row.humans_on_shift, row.set_by) == (True, "mahak")
        assert call_flow._humans_override(s, datetime.now(UTC)) is True


@pytest.mark.parametrize("hours", [0, -1, 25])
def test_post_rejects_a_bad_duration(admin, hours):
    client, headers = admin
    r = client.post("/admin/shift", json={"humans_on_shift": True, "hours": hours}, headers=headers)
    assert r.status_code == 422


def test_get_with_no_override_follows_live_hours(admin):
    client, headers = admin
    r = client.get("/admin/shift", headers=headers)
    assert r.json() == {"override": None, "humans_open_now": False}  # NEVER has no live hours
    use_arms(client, OPEN, AI)
    assert client.get("/admin/shift", headers=headers).json()["humans_open_now"] is True


def test_get_reports_the_override_and_that_humans_are_open(admin):
    client, headers = admin
    client.post("/admin/shift", json={"humans_on_shift": True, "hours": 1}, headers=headers)
    body = client.get("/admin/shift", headers=headers).json()
    assert body["humans_open_now"] is True
    assert body["override"]["humans_on_shift"] is True
    assert datetime.fromisoformat(body["override"]["until"]) > datetime.now(UTC)


def test_off_override_closes_the_human_arm_even_inside_live_hours(admin):
    client, headers = admin
    use_arms(client, OPEN, AI)
    client.post("/admin/shift", json={"humans_on_shift": False, "hours": 1}, headers=headers)
    assert client.get("/admin/shift", headers=headers).json()["humans_open_now"] is False


def test_latest_override_wins(admin):
    client, headers = admin
    client.post("/admin/shift", json={"humans_on_shift": True, "hours": 3}, headers=headers)
    client.post("/admin/shift", json={"humans_on_shift": False, "hours": 1}, headers=headers)
    body = client.get("/admin/shift", headers=headers).json()
    assert (body["override"]["humans_on_shift"], body["humans_open_now"]) == (False, False)


def test_expired_override_is_ignored(admin):
    client, headers = admin
    now = datetime.now(UTC)
    with db.get_sessionmaker()() as s:
        s.add(ShiftOverride(humans_on_shift=True, until=now - timedelta(minutes=1)))
        s.commit()
    body = client.get("/admin/shift", headers=headers).json()
    assert body == {"override": None, "humans_open_now": False}


def test_humans_never_open_without_a_dial_number(admin):
    client, headers = admin
    no_numbers = Arm("human", "human", "H", None, 1.0, live_hours=ALWAYS)
    use_arms(client, no_numbers, AI)
    client.post("/admin/shift", json={"humans_on_shift": True, "hours": 1}, headers=headers)
    assert client.get("/admin/shift", headers=headers).json()["humans_open_now"] is False
