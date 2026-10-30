"""tagging.tag_call: heuristic giveaway tags from word timings (#18)."""

from datetime import UTC, datetime

import pytest

from pehchana import db
from pehchana.models import (
    Accusation,
    AccusationSource,
    Call,
    CallStatus,
    Channel,
    Giveaway,
    Source,
)
from pehchana.tagging import (
    GiveawayTag,
    LLMGiveawayItem,
    LLMTaggerResponse,
    tag_call,
    tag_call_llm,
)


def make_call(
    *,
    transcript: list[dict] | None,
    caller_channel: int = 0,
    duration_s: float | None = None,
    accused_at: float | None = None,
) -> Call:
    call = Call(
        channel=Channel.PHONE,
        source=Source.REAL,
        status=CallStatus.PROCESSED,
        arm_id="kalpa",
        arm_kind="ai",
        caller_hash="hash1",
        started_at=datetime.now(UTC),
        answered_at=datetime.now(UTC),
        recording_caller_channel=caller_channel,
        duration_s=duration_s,
        transcript=transcript,
    )
    with db.get_sessionmaker()() as s:
        s.add(call)
        s.commit()
        if accused_at is not None:
            s.add(
                Accusation(
                    call_id=call.id, source=AccusationSource.TRANSCRIPT, at_s=accused_at, phrase="x"
                )
            )
            s.commit()
        s.refresh(call)
        s.expunge(call)
    return call


def words(*items: tuple[str, float, float]) -> list[dict]:
    return [{"text": t, "start": s, "end": e} for t, s, e in items]


def tags_for(call_id: str) -> dict[str, list[Giveaway]]:
    with db.get_sessionmaker()() as s:
        rows = s.query(Giveaway).filter(Giveaway.call_id == call_id).all()
        out: dict[str, list[Giveaway]] = {}
        for r in rows:
            out.setdefault(r.tag, []).append(r)
        return out


@pytest.fixture(autouse=True)
def _db_ready(client):
    """``client`` creates the schema; these tests talk to the DB directly."""


# --- slow_reply --------------------------------------------------------------------


def test_slow_reply_past_the_threshold(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 3.0, 3.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 6.0, 6.5))},  # 2.5s gap
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    tags = tags_for(call.id)
    assert GiveawayTag.SLOW_REPLY.value in tags
    assert "2.5s gap" in tags[GiveawayTag.SLOW_REPLY.value][0].evidence


def test_no_slow_reply_under_the_threshold(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 3.0, 3.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 4.0, 4.5))},  # 0.5s gap
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.SLOW_REPLY.value not in tags_for(call.id)


# --- talked_over ---------------------------------------------------------------------


def test_talked_over_mid_caller_utterance(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 5.0, 7.0))},
        {"channel": 1, "language": "hi", "words": words(("haan", 6.0, 6.3))},  # starts mid-"hello"
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.TALKED_OVER.value in tags_for(call.id)


def test_no_talked_over_when_arm_waits(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 5.0, 7.0))},
        {"channel": 1, "language": "hi", "words": words(("haan", 7.1, 7.4))},
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.TALKED_OVER.value not in tags_for(call.id)


# --- number_reading --------------------------------------------------------------------


def test_number_reading_digits_and_words(client):
    transcript = [
        {"channel": 0, "language": "en", "words": words(("hi", 1.0, 1.2))},
        {
            "channel": 1,
            "language": "en",
            "words": words(("it's", 2.0, 2.2), ("42", 2.2, 2.5), ("twenty", 2.5, 2.8)),
        },
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    hits = tags_for(call.id)[GiveawayTag.NUMBER_READING.value]
    assert len(hits) == 2  # "42" and "twenty", not "it's"


# --- wrong_language --------------------------------------------------------------------


def test_wrong_language_when_channels_differ(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 1.0, 1.2))},
        {"channel": 1, "language": "en", "words": words(("yes", 2.0, 2.2))},
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.WRONG_LANGUAGE.value in tags_for(call.id)


def test_no_wrong_language_when_channels_match(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 1.0, 1.2))},
        {"channel": 1, "language": "hi", "words": words(("haan", 2.0, 2.2))},
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.WRONG_LANGUAGE.value not in tags_for(call.id)


# --- window bounding --------------------------------------------------------------------


def test_words_outside_the_window_are_ignored(client):
    # accusation at 100s -> window is [70, 100]; this gap is at t=10, well before it.
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 10.0, 10.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 13.0, 13.5))},
    ]
    call = make_call(transcript=transcript, accused_at=100.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert tags_for(call.id) == {}


def test_no_accusation_uses_call_duration_as_the_window_end(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 28.0, 28.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 31.0, 31.5))},  # within last 30s
    ]
    call = make_call(transcript=transcript, duration_s=32.0, accused_at=None)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.SLOW_REPLY.value in tags_for(call.id)


# --- idempotency and errors --------------------------------------------------------------


def test_rerun_replaces_heuristic_tags_not_llm_ones(client):
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("tum", 3.0, 3.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 6.0, 6.5))},
    ]
    call = make_call(transcript=transcript, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        s.add(Giveaway(call_id=call.id, tag="flat_emotion", method="llm", confidence=0.8))
        s.commit()

    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)  # rerun

    with db.get_sessionmaker()() as s:
        rows = s.query(Giveaway).filter(Giveaway.call_id == call.id).all()
        methods = {r.method for r in rows}
        assert methods == {"heuristic", "llm"}
        assert len([r for r in rows if r.method == "heuristic" and r.tag == "slow_reply"]) == 1


def test_respects_recording_caller_channel(client):
    # caller is channel 1 here, not the default 0
    transcript = [
        {"channel": 0, "language": "en", "words": words(("haan", 6.0, 6.5))},
        {"channel": 1, "language": "hi", "words": words(("tum", 3.0, 3.5))},
    ]
    call = make_call(transcript=transcript, caller_channel=1, accused_at=20.0)
    with db.get_sessionmaker()() as s:
        tag_call(call.id, session=s)
    assert GiveawayTag.SLOW_REPLY.value in tags_for(call.id)


def test_no_transcript_raises_value_error(client):
    call = make_call(transcript=None)
    with db.get_sessionmaker()() as s, pytest.raises(ValueError):
        tag_call(call.id, session=s)


def test_unknown_call_id_raises_lookup_error(client):
    with db.get_sessionmaker()() as s, pytest.raises(LookupError):
        tag_call("no-such-call", session=s)


# --- LLM Tagging (Issue #19) ----------------------------------------------------------


class FakeParsedResponse:
    def __init__(self, giveaways):
        self.parsed_output = LLMTaggerResponse(giveaways=giveaways)
        self.stop_reason = "end_turn"


class FakeAnthropicClient:
    def __init__(self, giveaways=None, raises=False):
        self.giveaways = giveaways or []
        self.raises = raises
        self.beta = self
        self.messages = self

    def parse(self, **kwargs):
        if self.raises:
            raise RuntimeError("API rate limited or down")
        return FakeParsedResponse(self.giveaways)


def test_llm_tagging_skips_non_accused_call():
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 1.0, 1.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 2.0, 2.5))},
    ]
    # No accusation
    call = make_call(transcript=transcript, accused_at=None)
    fake_client = FakeAnthropicClient(
        [LLMGiveawayItem(tag=GiveawayTag.FLAT_EMOTION, evidence="haan")]
    )

    with db.get_sessionmaker()() as s:
        rows = tag_call_llm(call.id, session=s, client=fake_client)
    assert rows == []


def test_llm_tagging_stores_giveaways_with_mocked_client():
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 1.0, 1.5))},
        {
            "channel": 1,
            "language": "hi",
            "words": words(("aur", 2.0, 2.2), ("kuch", 2.3, 2.5), ("jaan", 2.6, 2.8)),
        },
    ]
    call = make_call(transcript=transcript, accused_at=10.0)
    fake_client = FakeAnthropicClient(
        [
            LLMGiveawayItem(tag=GiveawayTag.CONTENT, evidence="aur kuch jaan", confidence=0.95),
            LLMGiveawayItem(tag=GiveawayTag.FLAT_EMOTION, evidence="aur kuch", confidence=0.8),
        ]
    )

    with db.get_sessionmaker()() as s:
        rows = tag_call_llm(call.id, session=s, client=fake_client)

    assert len(rows) == 2
    assert {r.tag for r in rows} == {"content", "flat_emotion"}
    assert all(r.method == "llm" for r in rows)
    assert any(r.evidence == "aur kuch jaan" for r in rows)


def test_llm_tagging_idempotent_replaces_only_llm_rows():
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 1.0, 1.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 2.0, 2.5))},
    ]
    call = make_call(transcript=transcript, accused_at=10.0)

    # First add a heuristic giveaway
    with db.get_sessionmaker()() as s:
        s.add(
            Giveaway(
                call_id=call.id,
                tag="slow_reply",
                method="heuristic",
                evidence="pause",
                confidence=1.0,
            )
        )
        s.commit()

    fake_client1 = FakeAnthropicClient(
        [LLMGiveawayItem(tag=GiveawayTag.TOO_PERFECT, evidence="haan")]
    )
    with db.get_sessionmaker()() as s:
        tag_call_llm(call.id, session=s, client=fake_client1)

    fake_client2 = FakeAnthropicClient(
        [LLMGiveawayItem(tag=GiveawayTag.FLAT_EMOTION, evidence="haan")]
    )
    with db.get_sessionmaker()() as s:
        tag_call_llm(call.id, session=s, client=fake_client2)

    with db.get_sessionmaker()() as s:
        all_rows = s.query(Giveaway).filter(Giveaway.call_id == call.id).all()
        methods = {r.method: r.tag for r in all_rows}
        assert "heuristic" in methods and methods["heuristic"] == "slow_reply"
        assert "llm" in methods and methods["llm"] == "flat_emotion"
        assert len([r for r in all_rows if r.method == "llm"]) == 1


def test_llm_tagging_failure_never_crashes():
    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 1.0, 1.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 2.0, 2.5))},
    ]
    call = make_call(transcript=transcript, accused_at=10.0)
    failing_client = FakeAnthropicClient(raises=True)

    with db.get_sessionmaker()() as s:
        result = tag_call_llm(call.id, session=s, client=failing_client)
    assert result == []


def test_llm_tagging_missing_key_gracefully_skips(monkeypatch):
    from pehchana.config import Settings

    transcript = [
        {"channel": 0, "language": "hi", "words": words(("hello", 1.0, 1.5))},
        {"channel": 1, "language": "hi", "words": words(("haan", 2.0, 2.5))},
    ]
    call = make_call(transcript=transcript, accused_at=10.0)
    empty_settings = Settings(anthropic_api_key="", groq_api_key="", gemini_api_key="")

    with db.get_sessionmaker()() as s:
        result = tag_call_llm(call.id, session=s, settings=empty_settings)
    assert result == []
