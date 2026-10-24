"""Recording URL validation and the guarded downloader."""

from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
import respx

from pehchana.config import Settings
from pehchana.telephony import recordings
from pehchana.telephony.recordings import (
    InvalidRecording,
    RecordingDownloadError,
    download_recording,
    validate_recording_url,
)

HOSTS = ["media.plivo.com"]
URL = "https://media.plivo.com/Account/Recording/abc.mp3"
SETTINGS = Settings(recording_host_allowlist=HOSTS, recording_max_bytes=1000)


def test_a_plivo_https_url_is_accepted():
    validate_recording_url(URL, HOSTS)
    validate_recording_url("https://MEDIA.plivo.com./x.mp3", HOSTS)  # case, trailing dot
    validate_recording_url("https://media.plivo.com:443/x.mp3", HOSTS)


@pytest.mark.parametrize(
    "url",
    [
        "http://media.plivo.com/x.mp3",  # not https
        "file:///etc/passwd",
        "ftp://media.plivo.com/x.mp3",
        "//media.plivo.com/x.mp3",
        "media.plivo.com/x.mp3",
        "",
        "https://",
        "https://evil.example/x.mp3",  # not on the list
        "https://media.plivo.com.evil.example/x.mp3",  # suffix trick
        "https://evil.example/https://media.plivo.com/x.mp3",
        "https://media.plivo.com@evil.example/x.mp3",  # real host is evil.example
        "https://user:pw@media.plivo.com/x.mp3",  # credentials
        "https://media.plivo.com:8443/x.mp3",  # non-default port
        "https://media.plivo.com:notaport/x.mp3",
        "https://sub.media.plivo.com/x.mp3",  # exact match only
        "https://169.254.169.254/latest/meta-data/",
        "https://127.0.0.1/x.mp3",
        "https://localhost/x.mp3",
        "https://[::1]/x.mp3",
    ],
)
def test_untrusted_urls_are_rejected(url):
    with pytest.raises(InvalidRecording):
        validate_recording_url(url, HOSTS)


def test_rejection_message_never_contains_the_url():
    secret = "https://evil.example/secret-token.mp3"
    with pytest.raises(InvalidRecording) as e:
        validate_recording_url(secret, HOSTS)
    assert "secret-token" not in str(e.value)


# --- downloader ---------------------------------------------------------------


@pytest.fixture
def public_dns(monkeypatch):
    def resolve(host, port, **kwargs):
        return [(2, 1, 6, "", ("93.184.216.34", port))]

    monkeypatch.setattr(recordings.socket, "getaddrinfo", resolve)


@respx.mock
def test_download_returns_the_bytes(public_dns):
    route = respx.get(URL).mock(return_value=httpx.Response(200, content=b"audio"))
    assert (
        download_recording(URL, settings=SETTINGS, headers={"Authorization": "Basic x"}) == b"audio"
    )
    assert route.calls.last.request.headers["authorization"] == "Basic x"


def test_download_refuses_an_untrusted_url_without_any_request():
    with respx.mock(assert_all_called=False) as router:
        any_call = router.route().mock(return_value=httpx.Response(200))
        with pytest.raises(RecordingDownloadError):
            download_recording("https://evil.example/x.mp3", settings=SETTINGS)
        assert not any_call.called


@pytest.mark.parametrize(
    "address", ["10.0.0.5", "127.0.0.1", "169.254.169.254", "192.168.1.1", "100.64.0.1", "::1"]
)
def test_download_refuses_hosts_that_resolve_to_non_public_addresses(monkeypatch, address):
    monkeypatch.setattr(
        recordings.socket, "getaddrinfo", lambda host, port, **kw: [(2, 1, 6, "", (address, port))]
    )
    with respx.mock(assert_all_called=False) as router:
        any_call = router.route().mock(return_value=httpx.Response(200, content=b"x"))
        with pytest.raises(RecordingDownloadError, match="non-public"):
            download_recording(URL, settings=SETTINGS)
        assert not any_call.called


def test_download_refuses_ipv4_mapped_private_addresses(monkeypatch):
    monkeypatch.setattr(
        recordings.socket,
        "getaddrinfo",
        lambda host, port, **kw: [(10, 1, 6, "", ("::ffff:10.0.0.5", port, 0, 0))],
    )
    with pytest.raises(RecordingDownloadError, match="non-public"):
        download_recording(URL, settings=SETTINGS)


def test_download_refuses_when_any_resolved_address_is_private(monkeypatch):
    monkeypatch.setattr(
        recordings.socket,
        "getaddrinfo",
        lambda host, port, **kw: [
            (2, 1, 6, "", ("93.184.216.34", port)),
            (2, 1, 6, "", ("10.0.0.5", port)),
        ],
    )
    with pytest.raises(RecordingDownloadError, match="non-public"):
        download_recording(URL, settings=SETTINGS)


def test_download_fails_cleanly_when_the_host_does_not_resolve(monkeypatch):
    def fail(host, port, **kwargs):
        raise OSError("nope")

    monkeypatch.setattr(recordings.socket, "getaddrinfo", fail)
    with pytest.raises(RecordingDownloadError, match="did not resolve"):
        download_recording(URL, settings=SETTINGS)


@respx.mock
def test_download_does_not_follow_redirects(public_dns):
    respx.get(URL).mock(
        return_value=httpx.Response(302, headers={"location": "http://169.254.169.254/"})
    )
    other = respx.get("http://169.254.169.254/").mock(return_value=httpx.Response(200))
    with pytest.raises(RecordingDownloadError, match="302"):
        download_recording(URL, settings=SETTINGS)
    assert not other.called


@respx.mock
def test_download_rejects_a_declared_size_over_the_limit(public_dns):
    respx.get(URL).mock(
        return_value=httpx.Response(200, headers={"content-length": "1001"}, content=b"x")
    )
    with pytest.raises(RecordingDownloadError, match="size limit"):
        download_recording(URL, settings=SETTINGS)


@respx.mock
def test_download_stops_at_the_size_limit_even_without_content_length(public_dns):
    respx.get(URL).mock(return_value=httpx.Response(200, content=b"x" * 1001))
    with pytest.raises(RecordingDownloadError, match="size limit"):
        download_recording(URL, settings=SETTINGS)


@respx.mock
def test_download_accepts_exactly_the_limit(public_dns):
    respx.get(URL).mock(return_value=httpx.Response(200, content=b"x" * 1000))
    assert len(download_recording(URL, settings=SETTINGS)) == 1000


@respx.mock
def test_download_reports_server_errors_and_timeouts_without_leaking_the_url(public_dns):
    respx.get(URL).mock(return_value=httpx.Response(404))
    with pytest.raises(RecordingDownloadError, match="404"):
        download_recording(URL, settings=SETTINGS)

    respx.get(URL).mock(side_effect=httpx.ReadTimeout("slow"))
    with pytest.raises(RecordingDownloadError) as e:
        download_recording(URL, settings=SETTINGS)
    assert "abc.mp3" not in str(e.value)
    assert e.value.__cause__ is None


def test_download_gives_up_after_the_overall_deadline(public_dns, monkeypatch):
    clock = iter([0.0])  # first read sets the deadline, every later read is far past it
    fake_time = SimpleNamespace(monotonic=lambda: next(clock, 1000.0))
    monkeypatch.setattr(recordings, "time", fake_time)  # only this module's clock
    with respx.mock as router:
        router.get(URL).mock(return_value=httpx.Response(200, content=b"x" * 10))
        with pytest.raises(RecordingDownloadError, match="too long"):
            download_recording(URL, settings=SETTINGS)


def test_no_public_api_module_touches_recording_urls():
    # recording_url is a bearer secret. Only the telephony webhook (which stores it) and
    # the admin reprocess route may mention it; a leaderboard or webcall response must not.
    api = Path(recordings.__file__).resolve().parents[1] / "api"
    offenders = [
        f.name
        for f in api.glob("*.py")
        if f.name not in {"telephony.py", "admin.py"} and "recording" in f.read_text().lower()
    ]
    assert offenders == []
