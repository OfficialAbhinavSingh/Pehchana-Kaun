"""integrations/deepgram.transcribe_url.

Not live-verified (no Deepgram key available): the response shape here is built from
Deepgram's own docs, not a real call, unlike integrations/bolna.py's tests. Replace
this fixture with a real redacted response once #12 runs against actual call audio.
"""

import httpx
import pytest
import respx

from pehchana.integrations.deepgram import transcribe_url

URL = "https://api.deepgram.com/v1/listen"

RESPONSE = {
    "metadata": {"duration": 42.5},
    "results": {
        "channels": [
            {
                "detected_language": "hi",
                "alternatives": [
                    {
                        "words": [
                            {"word": "tum", "start": 12.0, "end": 12.2, "confidence": 0.98},
                            {"word": "bot", "start": 12.2, "end": 12.4, "confidence": 0.95},
                            {"word": "ho", "start": 12.4, "end": 12.6, "confidence": 0.97},
                        ]
                    }
                ],
            },
            {
                "detected_language": "en",
                "alternatives": [
                    {
                        "words": [
                            {"word": "yes", "start": 12.8, "end": 13.0, "confidence": 0.99},
                        ]
                    }
                ],
            },
        ]
    },
}


@respx.mock
def test_transcribes_both_channels_with_words_and_language():
    route = respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    result = transcribe_url("https://recordings.example/call.wav", api_key="dg-secret")

    assert result.duration_s == 42.5
    assert len(result.channels) == 2
    caller, arm = result.channels
    assert caller.language == "hi"
    assert [w.text for w in caller.words] == ["tum", "bot", "ho"]
    assert caller.words[0].start == 12.0 and caller.words[0].end == 12.2
    assert arm.language == "en"

    sent = route.calls.last.request
    assert sent.headers["authorization"] == "Token dg-secret"
    assert "model=nova-3" in str(sent.url)
    assert "language=multi" in str(sent.url)
    assert "multichannel=true" in str(sent.url)


@respx.mock
def test_model_and_language_can_be_overridden_for_the_spike():
    respx.post(URL).mock(return_value=httpx.Response(200, json=RESPONSE))
    transcribe_url(
        "https://recordings.example/call.wav", api_key="dg-secret", model="nova-2", language="hi"
    )
    sent = respx.calls.last.request
    assert "model=nova-2" in str(sent.url)
    assert "language=hi" in str(sent.url)


@respx.mock
def test_missing_duration_and_empty_channels_do_not_crash():
    respx.post(URL).mock(return_value=httpx.Response(200, json={"results": {"channels": []}}))
    result = transcribe_url("https://recordings.example/call.wav", api_key="dg-secret")
    assert result.duration_s is None and result.channels == []


@respx.mock
def test_never_leaks_the_api_key_on_failure():
    respx.post(URL).mock(return_value=httpx.Response(401, json={"error": "bad key"}))
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        transcribe_url("https://recordings.example/call.wav", api_key="dg-secret")
    assert "dg-secret" not in str(exc_info.value)
