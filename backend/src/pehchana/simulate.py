"""Rehearse the phone flow without a phone: ``pk simulate-call``.

Plays the part of the telephony vendor. It sends correctly signed ``answer``,
``dial-status`` and ``recording`` webhooks to a running backend, one scenario at a time,
and checks every response. Run it before launch, and again after each deploy, as the
smoke test in docs/runbook.md.

What it proves: signature checks, routing, the answer XML, the call life cycle,
idempotent retries, and the refusals (bad signature, other call's id, untrusted recording
URL). What it cannot prove: that Plivo's real field names and recording host match what
we assume (that needs the first real call, WS1-02), or that audio is processed (the
recording URL is made up; nothing is downloaded until the pipeline exists).

Calls use a reserved caller prefix, so the backend stores them as DEMO rows: they never
count in the public stats and never skew the balance between arms.

Everything vendor-specific (form fields, signing, answer XML) lives in a ``Dialect``, one
per vendor, picked from ``TELEPHONY_PROVIDER`` or ``--provider``. The scenarios and checks
are vendor-neutral. Plivo's dialect uses its documented field names, the same as
``telephony/plivo.py``; replace them with the real payloads once WS1-02 has captured some.
"""

from __future__ import annotations

import uuid
import xml.etree.ElementTree as ET
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Protocol
from urllib.parse import parse_qs, urlparse

import httpx
from plivo.utils.signature_v3 import construct_post_url, get_signature_v3
from sqlalchemy import select
from sqlalchemy.orm import Session

from pehchana.arms import Arm
from pehchana.config import Settings
from pehchana.models import Call, CallStatus, Source
from pehchana.telephony.call_flow import SIMULATED_CALLER_PREFIX

SCENARIOS = ("happy", "retries", "no-answer", "bad-signature", "bad-recording", "mismatch")
UNTRUSTED_RECORDING = "https://untrusted.example/rec.mp3"
CALL_SECONDS = 75.0


@dataclass
class Step:
    name: str
    ok: bool
    detail: str = ""


@dataclass
class Report:
    scenario: str
    steps: list[Step] = field(default_factory=list)
    call_id: str | None = None
    arm_id: str | None = None  # the arm whose dial numbers the answer XML carried

    @property
    def ok(self) -> bool:
        return all(s.ok for s in self.steps)

    def check(self, name: str, ok: bool, detail: str = "") -> bool:
        self.steps.append(Step(name, ok, "" if ok else detail))
        return ok


def arm_for_numbers(arms: Sequence[Arm], numbers: Sequence[str]) -> str | None:
    """Which configured arm owns these dial numbers (the answer XML carries them)."""
    wanted = set(numbers)
    return next((a.id for a in arms if wanted and wanted <= set(a.dial_numbers)), None)


@dataclass(frozen=True)
class Answer:
    call_id: str | None
    dial_numbers: tuple[str, ...]
    has_record: bool


def _query_param(url: str, name: str) -> str | None:
    return parse_qs(urlparse(url).query).get(name, [None])[0]


class UnknownDialect(LookupError):
    """No simulator exists for this telephony provider."""


class Dialect(Protocol):
    """How one vendor's webhooks look: the only vendor-specific part of the simulator."""

    name: str

    def token(self, settings: Settings) -> str:
        """The secret the backend verifies signatures with."""

    def sign(self, url: str, form: Mapping[str, str], token: str) -> dict[str, str]:
        """Request headers proving the vendor sent ``form`` to the public ``url``."""

    def answer_form(self, caller: str, call_uuid: str) -> dict[str, str]: ...

    def dial_status_form(
        self, call_uuid: str, *, answered: bool, duration_s: float | None = None
    ) -> dict[str, str]: ...

    def recording_form(self, url: str) -> dict[str, str]: ...

    def parse_answer(self, body: str) -> Answer:
        """Read the call id, the numbers dialled and the recording flag from the reply."""


class PlivoDialect:
    name = "plivo"

    def token(self, settings: Settings) -> str:
        return settings.plivo_auth_token

    def sign(self, url: str, form: Mapping[str, str], token: str) -> dict[str, str]:
        nonce = uuid.uuid4().hex
        signature = get_signature_v3(
            token.encode(), construct_post_url(url, dict(form)).decode(), nonce.encode()
        )
        return {
            "X-Plivo-Signature-V3": signature.decode(),
            "X-Plivo-Signature-V3-Nonce": nonce,
        }

    def answer_form(self, caller: str, call_uuid: str) -> dict[str, str]:
        return {"From": caller, "CallUUID": call_uuid}

    def dial_status_form(
        self, call_uuid: str, *, answered: bool, duration_s: float | None = None
    ) -> dict[str, str]:
        form = {"DialALegUUID": call_uuid, "DialBLegStatus": "hangup" if answered else "no-answer"}
        if duration_s is not None:
            form["DialBLegDuration"] = str(int(duration_s))
        return form

    def recording_form(self, url: str) -> dict[str, str]:
        return {"RecordUrl": url}

    def parse_answer(self, body: str) -> Answer:
        root = ET.fromstring(body)  # our own backend's reply
        dial = root.find("Dial")
        if dial is None:
            return Answer(None, (), root.find("Record") is not None)
        numbers = tuple((n.text or "").strip() for n in dial.findall("Number"))
        return Answer(
            _query_param(dial.get("action", ""), "call_id"),
            numbers,
            root.find("Record") is not None,
        )


DIALECTS: dict[str, Dialect] = {"plivo": PlivoDialect()}


def get_dialect(name: str) -> Dialect:
    try:
        return DIALECTS[name]
    except KeyError:
        known = ", ".join(sorted(DIALECTS))
        raise UnknownDialect(f"no simulator for provider {name!r} (have: {known})") from None


class Simulator:
    """Sends signed webhooks through ``client`` (an httpx client whose base_url is the
    backend to test) and records what came back."""

    def __init__(
        self,
        client: httpx.Client,
        settings: Settings,
        arms: Sequence[Arm] = (),
        dialect: Dialect | None = None,
    ) -> None:
        self.client, self.settings, self.arms = client, settings, arms
        self.dialect = dialect or get_dialect(settings.telephony_provider)

    # -- plumbing ---------------------------------------------------------------------

    def _post(
        self, path: str, form: Mapping[str, str], *, token: str | None = None, sign: bool = True
    ) -> httpx.Response:
        headers: dict[str, str] = {}
        if sign:
            # The vendor signs the public URL it called, not the one we connect to.
            url = self.settings.public_base_url.rstrip("/") + path
            secret = token if token is not None else self.dialect.token(self.settings)
            headers = self.dialect.sign(url, form, secret)
        return self.client.post(path, data=dict(form), headers=headers)

    def _recording_url(self, call_uuid: str) -> str:
        host = self.settings.recording_host_allowlist[0]
        return f"https://{host}/simulated/{call_uuid}.mp3"

    @staticmethod
    def _new_call() -> tuple[str, str]:
        call_uuid = f"sim-{uuid.uuid4().hex[:12]}"
        return call_uuid, f"{SIMULATED_CALLER_PREFIX}{uuid.uuid4().int % 100:02d}"

    def _path(self, endpoint: str) -> str:
        return f"/telephony/{self.dialect.name}/{endpoint}"

    def _answer(self, report: Report, call_uuid: str, caller: str) -> Answer | None:
        r = self._post(self._path("answer"), self.dialect.answer_form(caller, call_uuid))
        if not report.check("answer returns 200", r.status_code == 200, f"got {r.status_code}"):
            return None
        try:
            answer = self.dialect.parse_answer(r.text)
        except ET.ParseError:
            report.check("answer is XML", False, r.text[:80])
            return None
        if not answer.dial_numbers:
            report.check(
                "an arm picked the call",
                False,
                "no <Dial>: busy message, nobody eligible (human arm outside live hours?)",
            )
            return None
        report.check("answer plays, records, dials", answer.has_record and bool(answer.call_id))
        report.call_id = answer.call_id
        report.arm_id = arm_for_numbers(self.arms, answer.dial_numbers)
        return answer

    def _dial_status(
        self,
        report: Report,
        call_id: str,
        call_uuid: str,
        *,
        answered: bool,
        duration_s: float | None = None,
        expect: int = 204,
    ) -> None:
        form = self.dialect.dial_status_form(call_uuid, answered=answered, duration_s=duration_s)
        r = self._post(self._path(f"dial-status?call_id={call_id}"), form)
        report.check(f"dial-status gets {expect}", r.status_code == expect, f"got {r.status_code}")

    def _hang_up(self, report: Report, call_id: str, call_uuid: str) -> None:
        """The arm talked for CALL_SECONDS and the call ended."""
        self._dial_status(report, call_id, call_uuid, answered=True, duration_s=CALL_SECONDS)

    def _recording(self, report: Report, call_id: str, url: str, expect: int = 204) -> None:
        r = self._post(self._path(f"recording?call_id={call_id}"), self.dialect.recording_form(url))
        report.check(f"recording gets {expect}", r.status_code == expect, f"got {r.status_code}")

    # -- scenarios --------------------------------------------------------------------

    def happy(self) -> Report:
        """A caller dials, the arm answers for 75 s, the recording arrives."""
        report = Report("happy")
        call_uuid, caller = self._new_call()
        answer = self._answer(report, call_uuid, caller)
        if answer and answer.call_id:
            self._hang_up(report, answer.call_id, call_uuid)
            self._recording(report, answer.call_id, self._recording_url(call_uuid))
        return report

    def retries(self) -> Report:
        """The vendor repeats every webhook: same arm, no duplicates, no second pipeline run."""
        report = Report("retries")
        call_uuid, caller = self._new_call()
        answer = self._answer(report, call_uuid, caller)
        if not (answer and answer.call_id):
            return report
        again = self._answer(Report("retries-replay"), call_uuid, caller)
        report.check(
            "answer retry replays the same arm and call",
            again is not None
            and again.dial_numbers == answer.dial_numbers
            and again.call_id == answer.call_id,
            "retry was routed somewhere else",
        )
        url = self._recording_url(call_uuid)
        for _ in range(2):
            self._hang_up(report, answer.call_id, call_uuid)
            self._recording(report, answer.call_id, url)
        report.call_id = answer.call_id
        return report

    def no_answer(self) -> Report:
        """The arm never picks up: the call must end FAILED and not be processed."""
        report = Report("no-answer")
        call_uuid, caller = self._new_call()
        answer = self._answer(report, call_uuid, caller)
        if answer and answer.call_id:
            self._dial_status(report, answer.call_id, call_uuid, answered=False)
        return report

    def bad_signature(self) -> Report:
        """Unsigned requests and requests signed with another token are refused."""
        report = Report("bad-signature")
        call_uuid, caller = self._new_call()
        form = self.dialect.answer_form(caller, call_uuid)
        path = self._path("answer")
        unsigned = self._post(path, form, sign=False)
        report.check(
            "unsigned answer refused", unsigned.status_code == 403, f"{unsigned.status_code}"
        )
        forged = self._post(path, form, token="not-the-token")
        report.check(
            "wrongly signed answer refused", forged.status_code == 403, f"{forged.status_code}"
        )
        return report

    def bad_recording(self) -> Report:
        """A recording URL on an unknown host is refused, and does not block a good one."""
        report = Report("bad-recording")
        call_uuid, caller = self._new_call()
        answer = self._answer(report, call_uuid, caller)
        if answer and answer.call_id:
            # The vendor sends the recording after hang-up, so the call has ended by then.
            self._hang_up(report, answer.call_id, call_uuid)
            self._recording(report, answer.call_id, UNTRUSTED_RECORDING, expect=400)
            self._recording(report, answer.call_id, self._recording_url(call_uuid))
        return report

    def mismatch(self) -> Report:
        """A dial-status that names another vendor call id must not touch this call."""
        report = Report("mismatch")
        call_uuid, caller = self._new_call()
        answer = self._answer(report, call_uuid, caller)
        if answer and answer.call_id:
            self._dial_status(
                report,
                answer.call_id,
                "someone-else",
                answered=True,
                duration_s=CALL_SECONDS,
                expect=409,
            )
        return report

    def run(self, scenario: str) -> Report:
        runners: dict[str, Callable[[], Report]] = {
            "happy": self.happy,
            "retries": self.retries,
            "no-answer": self.no_answer,
            "bad-signature": self.bad_signature,
            "bad-recording": self.bad_recording,
            "mismatch": self.mismatch,
        }
        return runners[scenario]()


# -- what the backend stored ---------------------------------------------------------------

EXPECTED_STATUS = {
    "happy": CallStatus.ENDED,
    "retries": CallStatus.ENDED,
    "no-answer": CallStatus.FAILED,
    "bad-recording": CallStatus.ENDED,
    "mismatch": CallStatus.ROUTED,
}


def verify_db(session: Session, report: Report) -> None:
    """Needs the same database as the backend: checks the row the scenario left behind.

    A call may already be PROCESSED once the pipeline exists; that is as good as ENDED.
    """
    if report.call_id is None or report.scenario not in EXPECTED_STATUS:
        return
    call = session.scalars(select(Call).where(Call.id == report.call_id)).first()
    if not report.check("call row exists", call is not None, "no such call in this database"):
        return
    assert call is not None
    wanted = EXPECTED_STATUS[report.scenario]
    allowed = {wanted, CallStatus.PROCESSED} if wanted == CallStatus.ENDED else {wanted}
    report.check(
        f"status is {wanted.value}", call.status in allowed, f"status is {call.status.value}"
    )
    report.check("stored as a rehearsal (DEMO)", call.source == Source.DEMO, call.source.value)
    if report.scenario in ("happy", "retries", "bad-recording"):
        report.check("duration stored", call.duration_s == CALL_SECONDS, f"{call.duration_s}")
    has_recording = report.scenario in ("happy", "retries", "bad-recording")
    report.check(
        "recording stored" if has_recording else "no recording stored",
        (call.recording_url is not None) == has_recording,
        f"recording_url is {call.recording_url!r}",
    )
