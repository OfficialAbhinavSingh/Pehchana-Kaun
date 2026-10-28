import httpx
import pytest
import respx
from typer.testing import CliRunner

from pehchana.cli import app
from pehchana.config import get_settings
from pehchana.consent import MAX_BYTES, check_consent_audio, looks_like_audio

URL = "https://site.example/consent.mp3"
MP3 = b"ID3\x04\x00\x00\x00\x00\x00\x00" + b"\x00" * 12_000
WAV = b"RIFF\x00\x00\x00\x00WAVEfmt " + b"\x00" * 12_000


def serve(body: bytes = MP3, *, status: int = 200, content_type: str = "audio/mpeg") -> None:
    respx.get(URL).mock(
        return_value=httpx.Response(status, content=body, headers={"content-type": content_type})
    )


@respx.mock
def test_a_good_mp3_passes():
    serve()
    result = check_consent_audio(URL)
    assert result.ok and result.size == len(MP3) and result.content_type == "audio/mpeg"


@respx.mock
def test_a_wav_with_a_charset_suffix_passes():
    serve(WAV, content_type="audio/wav; charset=binary")
    assert check_consent_audio(URL).ok


@respx.mock
def test_a_redirect_to_the_file_is_followed():
    respx.get(URL).mock(
        return_value=httpx.Response(302, headers={"location": "https://cdn.example/c.mp3"})
    )
    respx.get("https://cdn.example/c.mp3").mock(
        return_value=httpx.Response(200, content=MP3, headers={"content-type": "audio/mpeg"})
    )
    assert check_consent_audio(URL).ok


@respx.mock
@pytest.mark.parametrize(
    ("kwargs", "fragment"),
    [
        ({"status": 404, "body": b"nope"}, "answered 404"),
        ({"content_type": "text/html"}, "content type is text/html"),
        ({"body": b"ID3" + b"\x00" * 100}, "only"),
        ({"body": b"<html>" + b"x" * 12_000}, "does not look like"),
        ({"body": MP3 + b"\x00" * MAX_BYTES}, "over 10 MB"),
    ],
)
def test_each_problem_is_named(kwargs, fragment):
    serve(**kwargs)
    result = check_consent_audio(URL)
    assert not result.ok
    assert any(fragment in p for p in result.problems), result.problems


@respx.mock
def test_http_is_refused_even_if_it_answers():
    respx.get("http://site.example/consent.mp3").mock(
        return_value=httpx.Response(200, content=MP3, headers={"content-type": "audio/mpeg"})
    )
    result = check_consent_audio("http://site.example/consent.mp3")
    assert any("https" in p for p in result.problems)


@respx.mock
def test_an_unreachable_host_is_reported_not_raised():
    respx.get(URL).mock(side_effect=httpx.ConnectError("no route"))
    result = check_consent_audio(URL)
    assert any("could not fetch" in p for p in result.problems)


def test_audio_sniffing():
    assert looks_like_audio(b"ID3\x04")
    assert looks_like_audio(b"\xff\xfb\x90\x00")
    assert looks_like_audio(b"RIFF\x00\x00\x00\x00WAVE")
    assert not looks_like_audio(b"<html>")
    assert not looks_like_audio(b"")


@pytest.fixture
def consent_env(monkeypatch):
    def apply(value: str) -> None:
        monkeypatch.setenv("CONSENT_AUDIO_URL", value)
        get_settings.cache_clear()

    yield apply
    monkeypatch.undo()
    get_settings.cache_clear()


def test_cli_unset_fails_unless_tts_is_accepted(consent_env):
    consent_env("")
    runner = CliRunner()
    assert runner.invoke(app, ["check-consent"]).exit_code == 1
    ok = runner.invoke(app, ["check-consent", "--allow-tts"])
    assert ok.exit_code == 0 and "text-to-speech" in ok.output


@respx.mock
def test_cli_reports_a_good_and_a_bad_file(consent_env):
    consent_env(URL)
    runner = CliRunner()
    serve()
    good = runner.invoke(app, ["check-consent"])
    assert good.exit_code == 0 and "reachable" in good.output
    respx.reset()
    serve(status=404, body=b"x")
    bad = runner.invoke(app, ["check-consent"])
    assert bad.exit_code == 1 and "404" in bad.output
