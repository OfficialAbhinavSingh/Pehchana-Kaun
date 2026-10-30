"""Thin Bolna REST client.  Owner: WS2 (Agents & analysis).

Verified gotchas (https://www.bolna.ai/docs/AGENTS.md, read 2026-10-21):
- Base URL ``https://api.bolna.ai``, header ``Authorization: Bearer <key>``.
- ``POST /v2/agent`` returns **201** with ``{agent_id, state}`` (not ``status``).
- ``toolchain.pipelines`` is an **array of arrays**: ``[["transcriber","llm","synthesizer"]]``.
- Execution fields (duration, cost, recording, transcript) are only final once status
  is terminal; wait for ``completed``, not ``call-disconnected``.
- ``completed`` does not mean anyone talked: check ``conversation_duration > 0``.
- Webhooks fire several times per call: be idempotent on ``id``.
- Bolna's ``transcript`` has **no timestamps** ("speaker: text" lines) and
  ``tool_call_logs`` is always empty in the API, which is why timing comes from our
  own Deepgram pass on the Plivo recording (docs/architecture.md#timing).
- Webhooks and function calls come from 13.203.39.153, 13.126.9.249, 13.202.133.53.
- Web Call SDK: the browser never sees the key; our backend mints a session via
  ``POST /web-call/session`` with ``{agent_id, user_data}``.
"""

from __future__ import annotations

from typing import Any

import httpx

TERMINAL_STATUSES = frozenset(
    {"completed", "no-answer", "busy", "failed", "canceled", "stopped", "error", "balance-low"}
)

# Connect/write/pool, then a per-chunk read cap; mint is a single small POST.
_TIMEOUT = httpx.Timeout(10.0, read=20.0)


class BolnaClient:
    def __init__(self, api_key: str, base_url: str = "https://api.bolna.ai") -> None:
        self.api_key = api_key
        self.base_url = base_url

    def create_agent(self, body: dict[str, Any]) -> str:
        """POST /v2/agent -> the new agent's id.

        201 on success, with ``{agent_id, state}`` (the field is ``state``, not
        ``status``; the v1 ``/agent`` endpoint returns 200, this one is v2 and
        returns 201 -- both verified against Bolna's docs, not just inferred).
        """
        with httpx.Client(base_url=self.base_url, timeout=_TIMEOUT) as client:
            response = client.post(
                "/v2/agent", json=body, headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return str(response.json()["agent_id"])

    def update_agent(self, agent_id: str, body: dict[str, Any]) -> str:
        """PUT /v2/agent/{agent_id} -> updated agent's id."""
        with httpx.Client(base_url=self.base_url, timeout=_TIMEOUT) as client:
            response = client.put(
                f"/v2/agent/{agent_id}",
                json=body,
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            res = response.json()
            return str(res.get("agent_id") or res.get("id") or agent_id)

    def get_agent(self, agent_id: str) -> dict[str, Any]:
        """GET /v2/agent/{agent_id} -> agent config dict."""
        with httpx.Client(base_url=self.base_url, timeout=_TIMEOUT) as client:
            response = client.get(
                f"/v2/agent/{agent_id}",
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return dict(response.json())

    def get_execution(self, execution_id: str) -> dict[str, Any]:
        """GET /executions/{id}: conversation time, status, telephony data.

        Duration, cost, recording and transcript fields are only final once
        ``status`` is a terminal one (see ``TERMINAL_STATUSES``); the caller decides
        what to do with a non-terminal response, this just returns it unchanged.
        """
        with httpx.Client(base_url=self.base_url, timeout=_TIMEOUT) as client:
            response = client.get(
                f"/executions/{execution_id}", headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return dict(response.json())

    def mint_web_call_session(self, agent_id: str, user_data: dict[str, Any] | None = None) -> Any:
        """POST /web-call/session for the browser SDK.

        Returns Bolna's JSON unchanged; the caller (webcall.py) passes it straight to
        the browser. Raises on any non-2xx response or network failure -- the caller
        turns every such exception into a 502 without leaking it, so this never needs
        to interpret Bolna's error body itself.
        """
        body: dict[str, Any] = {"agent_id": agent_id}
        if user_data is not None:
            body["user_data"] = user_data
        with httpx.Client(base_url=self.base_url, timeout=_TIMEOUT) as client:
            response = client.post(
                "/web-call/session",
                json=body,
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json()


def build_agent_payload(
    arm: dict[str, Any],
    *,
    public_base_url: str,
    bolna_shared_secret: str,
    persona_prompt: str,
    accuse_tool: dict[str, Any],
) -> dict[str, Any]:
    """Build the Bolna agent creation/update body from an AI arm entry in arms.yaml."""
    arm_id = arm["id"]
    stack = arm.get("stack", {})
    tts = stack.get("tts", {})
    stt = stack.get("stt", {})

    # Synthesizer config
    synth_provider = tts.get("provider", "kalpa")
    synth_model = tts.get("model", "kalpa-tts-1")
    synth_config: dict[str, Any] = {"model": synth_model}
    if synth_provider == "kalpa":
        synth_config["voice"] = "Kiara"

    # Transcriber config
    stt_provider = stt.get("provider", "deepgram")
    stt_model = stt.get("model", "nova-3")
    trans_config: dict[str, Any] = {"model": stt_model}
    if stt.get("language"):
        trans_config["language"] = stt["language"]

    # Tool config with substituted URLs and secrets
    import json

    tool_str = json.dumps(accuse_tool)
    tool_str = tool_str.replace("${PUBLIC_BASE_URL}", public_base_url.rstrip("/"))
    tool_str = tool_str.replace("${BOLNA_SHARED_SECRET}", bolna_shared_secret)
    resolved_tool = json.loads(tool_str)

    return {
        "agent_config": {
            "agent_name": f"pehchana-kaun-{arm_id}",
            "agent_welcome_message": "Haan hello? Kaun bol raha hai?",
            "webhook_url": f"{public_base_url.rstrip('/')}/bolna/webhook",
            "tasks": [
                {
                    "task_type": "conversation",
                    "toolchain": {
                        "execution": "parallel",
                        "pipelines": [["transcriber", "llm", "synthesizer"]],
                    },
                    "tools_config": {
                        "llm_agent": {
                            "agent_type": "simple_llm_agent",
                            "agent_flow_type": "streaming",
                            "llm_config": {
                                "provider": "openai",
                                "model": "gpt-4.1-mini",
                                "max_tokens": 120,
                                "temperature": 0.7,
                            },
                        },
                        "synthesizer": {
                            "provider": synth_provider,
                            "provider_config": synth_config,
                            "stream": True,
                        },
                        "transcriber": {
                            "provider": stt_provider,
                            "provider_config": trans_config,
                            "stream": True,
                        },
                        "input": {"provider": "plivo", "format": "wav"},
                        "output": {"provider": "plivo", "format": "wav"},
                        "api_tools": {"tools": [resolved_tool]},
                    },
                    "task_config": {
                        "call_terminate": 300,
                        "hangup_after_silence": 15,
                    },
                }
            ],
        },
        "agent_prompts": {
            "task_1": {
                "system_prompt": persona_prompt,
            }
        },
    }
