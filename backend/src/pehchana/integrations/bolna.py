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
        """POST /v2/agent -> agent_id. TODO(WS2)"""
        raise NotImplementedError

    def get_execution(self, execution_id: str) -> dict[str, Any]:
        """GET /executions/{id}. TODO(WS2)"""
        raise NotImplementedError

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
