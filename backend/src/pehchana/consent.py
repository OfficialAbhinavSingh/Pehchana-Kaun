"""Pre-launch check of the recorded consent notice (``pk check-consent``).

Every call starts by playing ``CONSENT_AUDIO_URL`` before anyone answers. Plivo's docs do
not say what happens when that file cannot be fetched, so a bad URL could mean callers
get silence or no game. This fetches the file the way the vendor will and reports what
is wrong, so it is found before launch and not by the first caller.

It checks the file is reachable, over https, audio, and a sane size. It cannot hear the
notice: listen to it, and time it, yourself (docs/consent-audio.md).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from urllib.parse import urlparse

import httpx

# Plivo's <Play> limit is 10 MB; anything under a few KB is an empty or truncated file.
MAX_BYTES = 10_000_000
MIN_BYTES = 4_000
AUDIO_TYPES = ("audio/mpeg", "audio/mp3", "audio/wav", "audio/x-wav", "audio/wave")


@dataclass
class ConsentCheck:
    problems: list[str] = field(default_factory=list)
    size: int | None = None
    content_type: str | None = None

    @property
    def ok(self) -> bool:
        return not self.problems


def looks_like_audio(head: bytes) -> bool:
    """MP3 (ID3 tag or an MPEG frame sync) or WAV, judged from the first bytes."""
    if head[:3] == b"ID3":
        return True
    if len(head) >= 2 and head[0] == 0xFF and head[1] & 0xE0 == 0xE0:
        return True
    return head[:4] == b"RIFF" and head[8:12] == b"WAVE"


def check_consent_audio(url: str, *, client: httpx.Client | None = None) -> ConsentCheck:
    result = ConsentCheck()
    if urlparse(url).scheme != "https":
        result.problems.append("the URL must be https:// (Plivo only plays audio over https)")
    owns_client = client is None
    client = client or httpx.Client(timeout=10, follow_redirects=True, max_redirects=3)
    try:
        with client.stream("GET", url) as response:
            if response.status_code != 200:
                result.problems.append(f"the URL answered {response.status_code}, not 200")
                return result
            result.content_type = response.headers.get("content-type", "").split(";")[0].strip()
            if result.content_type.lower() not in AUDIO_TYPES:
                result.problems.append(
                    f"content type is {result.content_type or 'missing'}, expected audio/mpeg"
                )
            body = b""
            for chunk in response.iter_bytes():
                body += chunk
                if len(body) > MAX_BYTES:
                    break
    except httpx.HTTPError as e:
        result.problems.append(f"could not fetch the URL: {e}")
        return result
    finally:
        if owns_client:
            client.close()
    result.size = len(body)
    if len(body) > MAX_BYTES:
        result.problems.append("the file is over 10 MB, Plivo's limit for <Play>")
    elif len(body) < MIN_BYTES:
        result.problems.append(f"the file is only {len(body)} bytes: empty or truncated?")
    elif not looks_like_audio(body[:12]):
        result.problems.append("the file does not look like MP3 or WAV audio")
    return result
