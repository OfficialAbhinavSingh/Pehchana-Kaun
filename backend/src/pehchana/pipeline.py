"""Post-call processing.  Owner: WS2.

Triggered when Plivo reports the recording is ready (and re-runnable from the CLI):

    recording_url
      -> Deepgram (both channels, word timestamps)        integrations/deepgram.py
      -> accusations in the caller channel               detection.py
      -> merge with live accuse_bot function hits (AI arms)
      -> giveaway tags                                    tagging.py
      -> Call.status = processed

Must be idempotent: re-running on a call replaces its accusations and tags.
"""

from __future__ import annotations


def process_call(call_id: str) -> None:
    """TODO(WS2)"""
    raise NotImplementedError
