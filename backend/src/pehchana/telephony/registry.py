"""Provider registry: the only place that knows which vendors exist.

To add a vendor: implement ``TelephonyProvider`` in ``telephony/<vendor>.py``, then
add one entry to ``_FACTORIES``.
"""

from __future__ import annotations

from collections.abc import Callable

from pehchana.config import Settings, get_settings
from pehchana.telephony.base import TelephonyProvider, UnknownProvider
from pehchana.telephony.plivo import PlivoProvider

_FACTORIES: dict[str, Callable[[Settings], TelephonyProvider]] = {
    "plivo": PlivoProvider.from_settings,
}


def get_provider(name: str | None = None, settings: Settings | None = None) -> TelephonyProvider:
    settings = settings or get_settings()
    key = name or settings.telephony_provider
    try:
        factory = _FACTORIES[key]
    except KeyError:
        raise UnknownProvider(key) from None
    return factory(settings)


def provider_names() -> list[str]:
    return sorted(_FACTORIES)
