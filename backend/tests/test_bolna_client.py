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


# --- update_agent & get_agent ---------------------------------------------------------

UPDATE_URL = "https://bolna.example/v2/agent/agent-xyz"


@respx.mock
def test_update_agent_returns_the_agent_id(client):
    route = respx.put(UPDATE_URL).mock(
        return_value=httpx.Response(200, json={"agent_id": "agent-xyz", "state": "updated"})
    )
    assert client.update_agent("agent-xyz", {"agent_name": "kalpa-test-updated"}) == "agent-xyz"
    sent = route.calls.last.request
    assert sent.headers["authorization"] == "Bearer bn-secret"
    expected = httpx.Request("PUT", UPDATE_URL, json={"agent_name": "kalpa-test-updated"})
    assert sent.content == expected.content


@respx.mock
def test_get_agent_returns_agent_config(client):
    route = respx.get(UPDATE_URL).mock(
        return_value=httpx.Response(200, json={"agent_id": "agent-xyz", "agent_name": "kalpa"})
    )
    assert client.get_agent("agent-xyz") == {"agent_id": "agent-xyz", "agent_name": "kalpa"}
    assert route.calls.last.request.headers["authorization"] == "Bearer bn-secret"


# --- build_agent_payload --------------------------------------------------------------


def test_build_agent_payload_renders_toolchain_and_substitutions():
    from pehchana.integrations.bolna import build_agent_payload

    arm = {
        "id": "kalpa",
        "stack": {
            "tts": {"provider": "kalpa", "model": "kalpa-tts-1"},
            "stt": {"provider": "deepgram", "model": "nova-3", "language": "multi"},
        },
    }
    tool = {
        "name": "accuse_bot",
        "url": "${PUBLIC_BASE_URL}/bolna/fn/accuse",
        "token": "${BOLNA_SHARED_SECRET}",
    }
    payload = build_agent_payload(
        arm,
        public_base_url="https://api.example.com",
        bolna_shared_secret="secret-123",
        persona_prompt="You are Priya",
        accuse_tool=tool,
    )

    assert payload["agent_config"]["agent_name"] == "pehchana-kaun-kalpa"
    assert payload["agent_config"]["webhook_url"] == "https://api.example.com/bolna/webhook"
    task = payload["agent_config"]["tasks"][0]
    # toolchain.pipelines must be an array of arrays
    assert task["toolchain"]["pipelines"] == [["transcriber", "llm", "synthesizer"]]

    # Synthesizer & transcriber stack
    assert task["tools_config"]["synthesizer"]["provider"] == "kalpa"
    assert task["tools_config"]["synthesizer"]["provider_config"]["model"] == "kalpa-tts-1"
    assert task["tools_config"]["synthesizer"]["provider_config"]["voice"] == "Kiara"
    assert task["tools_config"]["transcriber"]["provider"] == "deepgram"
    assert task["tools_config"]["transcriber"]["provider_config"]["model"] == "nova-3"
    assert task["tools_config"]["transcriber"]["provider_config"]["language"] == "multi"

    # API tools substituted
    resolved_tool = task["tools_config"]["api_tools"]["tools"][0]
    assert resolved_tool["url"] == "https://api.example.com/bolna/fn/accuse"
    assert resolved_tool["token"] == "secret-123"

    # Persona
    assert payload["agent_prompts"]["task_1"]["system_prompt"] == "You are Priya"


# --- CLI sync-agents -----------------------------------------------------------------


def test_cli_sync_agents_dry_run():
    from typer.testing import CliRunner

    from pehchana.cli import app

    runner = CliRunner()
    result = runner.invoke(app, ["sync-agents", "--dry-run"])
    assert result.exit_code == 0
    assert "kalpa" in result.stdout
    assert "cartesia" in result.stdout
    assert "sarvam" in result.stdout
    assert "pipelines" in result.stdout


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
