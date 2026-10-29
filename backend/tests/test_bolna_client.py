"""BolnaClient: create_agent, get_execution, mint_web_call_session."""

import httpx
import pytest
import respx

from pehchana.integrations.bolna import BolnaClient

URL = "https://bolna.example/web-call/session"
SESSION = {"session_id": "s-1", "ice_servers": [{"urls": "turn:x"}], "expires_in": 120}


@pytest.fixture
def client() -> BolnaClient:
    return BolnaClient("bn-secret", "https://bolna.example")


@respx.mock
def test_mints_a_session_with_agent_id_and_user_data(client):
    route = respx.post(URL).mock(return_value=httpx.Response(200, json=SESSION))
    result = client.mint_web_call_session("agent-a", {"call_id": "c-1"})
    assert result == SESSION
    sent = route.calls.last.request
    assert sent.headers["authorization"] == "Bearer bn-secret"
    assert (
        sent.content
        == httpx.Request(
            "POST", URL, json={"agent_id": "agent-a", "user_data": {"call_id": "c-1"}}
        ).content
    )


@respx.mock
def test_user_data_is_omitted_when_not_given(client):
    route = respx.post(URL).mock(return_value=httpx.Response(200, json=SESSION))
    client.mint_web_call_session("agent-a")
    assert "user_data" not in route.calls.last.request.content.decode()


@respx.mock
def test_never_logs_or_leaks_the_api_key_on_failure(client):
    respx.post(URL).mock(return_value=httpx.Response(401, json={"error": "bad key"}))
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        client.mint_web_call_session("agent-a")
    assert "bn-secret" not in str(exc_info.value)


@respx.mock
def test_network_failure_propagates(client):
    respx.post(URL).mock(side_effect=httpx.ConnectTimeout("slow"))
    with pytest.raises(httpx.ConnectTimeout):
        client.mint_web_call_session("agent-a")


# --- create_agent -------------------------------------------------------------------

CREATE_URL = "https://bolna.example/v2/agent"


@respx.mock
def test_create_agent_returns_the_new_agent_id(client):
    route = respx.post(CREATE_URL).mock(
        return_value=httpx.Response(201, json={"agent_id": "agent-xyz", "state": "created"})
    )
    assert client.create_agent({"agent_name": "kalpa-test"}) == "agent-xyz"
    sent = route.calls.last.request
    assert sent.headers["authorization"] == "Bearer bn-secret"
    expected = httpx.Request("POST", CREATE_URL, json={"agent_name": "kalpa-test"})
    assert sent.content == expected.content


@respx.mock
def test_create_agent_raises_on_a_bad_request(client):
    respx.post(CREATE_URL).mock(return_value=httpx.Response(422, json={"error": "bad toolchain"}))
    with pytest.raises(httpx.HTTPStatusError):
        client.create_agent({})


# --- get_execution -------------------------------------------------------------------

EXEC_URL = "https://bolna.example/executions/exec-1"


@respx.mock
def test_get_execution_returns_the_payload_unchanged(client):
    payload = {"status": "completed", "conversation_duration": 42.0, "total_cost": 0.5}
    route = respx.get(EXEC_URL).mock(return_value=httpx.Response(200, json=payload))
    assert client.get_execution("exec-1") == payload
    assert route.calls.last.request.headers["authorization"] == "Bearer bn-secret"


@respx.mock
def test_get_execution_raises_when_not_found(client):
    respx.get(EXEC_URL).mock(return_value=httpx.Response(404, json={"error": "no such execution"}))
    with pytest.raises(httpx.HTTPStatusError):
        client.get_execution("exec-1")


# --- #3's linking fixture -------------------------------------------------------------


def test_execution_completed_fixture_has_linking_fields() -> None:
    import json
    from pathlib import Path

    fixture_path = Path(__file__).parent / "fixtures" / "bolna" / "execution_completed.json"
    assert fixture_path.exists(), "execution_completed.json fixture must exist"
    data = json.loads(fixture_path.read_text(encoding="utf-8"))

    assert data["status"] == "completed"
    assert data["conversation_duration"] > 0
    assert "agent_id" in data
    assert "user_number" in data
    assert "telephony_data" in data
    assert data["telephony_data"]["call_type"] == "inbound"
    assert "from_number" in data["telephony_data"]
    assert "to_number" in data["telephony_data"]
    assert "duration" in data["telephony_data"]
    assert "created_at" in data
