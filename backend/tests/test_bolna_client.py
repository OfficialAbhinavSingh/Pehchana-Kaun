"""BolnaClient.mint_web_call_session: the only BolnaClient method WS3's #25 needs."""

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
