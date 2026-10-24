"""Safety checks for recording URLs.  Owner: WS1 (Calls).

A recording URL arrives in a webhook and is later fetched, by us or by Deepgram. The
webhook is signed, but the signature proves who sent it, not that the URL is safe, so a
bad or hijacked URL must not reach storage or a downloader.

``validate_recording_url`` runs when the callback is stored, for every provider.
``download_recording`` is for a pipeline that fetches the file itself (for example when
the vendor requires auth headers that Deepgram cannot send); it re-checks the URL and
adds network-level limits.

Recording URLs are bearer secrets (anyone holding one can play the call): never log
them, never return them from a public API.
"""

from __future__ import annotations

import ipaddress
import logging
import socket
import time
from collections.abc import Mapping, Sequence
from urllib.parse import urlsplit

import httpx

from pehchana.config import Settings

log = logging.getLogger(__name__)

# Seconds: connect/write/pool, read per chunk, and a hard cap on the whole download so a
# server that drips bytes cannot hold a worker.
_TIMEOUT = httpx.Timeout(10.0, read=20.0)
_DEADLINE_S = 60.0


class InvalidRecording(ValueError):
    """The recording callback is unusable. Messages never contain the URL."""


class RecordingDownloadError(Exception):
    """A recording could not be fetched safely. Messages never contain the URL."""


def validate_recording_url(url: str, allowed_hosts: Sequence[str]) -> None:
    """Raise ``InvalidRecording`` unless ``url`` is https on an allowed host.

    Hosts match exactly (``media.plivo.com`` does not allow ``x.media.plivo.com``); list
    each host that should be trusted. Credentials in the URL and non-default ports are
    refused.
    """
    try:
        parts = urlsplit(url)
        port = parts.port
    except ValueError:
        raise InvalidRecording("recording URL is malformed") from None
    if parts.scheme != "https":
        raise InvalidRecording("recording URL must use https")
    if parts.username is not None or parts.password is not None:
        raise InvalidRecording("recording URL must not contain credentials")
    if port not in (None, 443):
        raise InvalidRecording("recording URL must use the default https port")
    host = (parts.hostname or "").lower().rstrip(".")
    if host not in {h.lower().rstrip(".") for h in allowed_hosts}:
        log.warning("recording host %r is not in RECORDING_HOST_ALLOWLIST", host)
        raise InvalidRecording("recording host is not allowed")


def _assert_public_host(host: str) -> None:
    """Refuse hosts that resolve to private, loopback, link-local or reserved addresses."""
    try:
        infos = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    except OSError:
        raise RecordingDownloadError("recording host did not resolve") from None
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
            ip = ip.ipv4_mapped
        if not ip.is_global:
            raise RecordingDownloadError("recording host resolves to a non-public address")


def download_recording(
    url: str, *, settings: Settings, headers: Mapping[str, str] | None = None
) -> bytes:
    """Fetch a recording with the URL, address, redirect, size and time limits applied.

    Redirects are never followed (a redirect could leave the allowlist, and would carry
    ``headers`` with it). The host is resolved and checked just before connecting; the
    exact-host allowlist, not this check, is what stops DNS rebinding.
    """
    try:
        validate_recording_url(url, settings.recording_host_allowlist)
    except InvalidRecording as e:
        raise RecordingDownloadError(str(e)) from None
    host = (urlsplit(url).hostname or "").lower()
    _assert_public_host(host)

    limit = settings.recording_max_bytes
    deadline = time.monotonic() + _DEADLINE_S
    body = bytearray()
    try:
        with (
            httpx.Client(timeout=_TIMEOUT, follow_redirects=False) as client,
            client.stream("GET", url, headers=dict(headers or {})) as response,
        ):
            if response.status_code != 200:
                raise RecordingDownloadError(f"recording server answered {response.status_code}")
            declared = response.headers.get("content-length", "")
            if declared.isdigit() and int(declared) > limit:
                raise RecordingDownloadError("recording is larger than the size limit")
            for chunk in response.iter_bytes():
                body += chunk
                if len(body) > limit:
                    raise RecordingDownloadError("recording is larger than the size limit")
                if time.monotonic() > deadline:
                    raise RecordingDownloadError("recording download took too long")
    except httpx.HTTPError as e:
        # Not chained: httpx errors can carry the request, and with it the secret URL.
        raise RecordingDownloadError(f"recording download failed ({type(e).__name__})") from None
    return bytes(body)
