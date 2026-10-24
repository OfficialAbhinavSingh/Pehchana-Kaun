"""Telephony webhooks, one route set per registered provider.  Owner: WS1 (Calls).

Routes are generated from the provider registry, so ``/telephony/plivo/*`` exists today
and a new vendor gets its own ``/telephony/<name>/*`` the moment it is registered.
Every handler authenticates through the provider before trusting the request; all
logic lives in ``telephony/call_flow.py``.
"""

import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request, Response, status

from pehchana import pipeline
from pehchana.api.deps import ArmsDep, SessionDep, SettingsDep
from pehchana.models import Call
from pehchana.telephony import call_flow
from pehchana.telephony.base import ProviderResponse, TelephonyProvider, WebhookRequest
from pehchana.telephony.registry import get_provider, provider_names

log = logging.getLogger(__name__)


async def _authenticated_form(
    request: Request, provider: TelephonyProvider, public_base_url: str
) -> dict[str, str]:
    form = {k: str(v) for k, v in (await request.form()).items()}
    # Vendors sign the URL they called, so rebuild it from our public base URL; behind a
    # proxy or tunnel request.url would hold the internal host.
    url = public_base_url.rstrip("/") + request.url.path
    if request.url.query:
        url += "?" + request.url.query
    headers = {k.lower(): v for k, v in request.headers.items()}
    if not provider.verify(WebhookRequest(request.method, url, headers, form)):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="bad webhook signature")
    return form


def _get_call(session: SessionDep, call_id: str) -> Call:
    call = session.get(Call, call_id)
    if call is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="unknown call")
    return call


def _respond(r: ProviderResponse) -> Response:
    return Response(content=r.body, media_type=r.media_type)


def _mismatch(error: call_flow.CallMismatch) -> HTTPException:
    return HTTPException(status.HTTP_409_CONFLICT, detail=str(error))


def _process(call_id: str) -> None:
    try:
        pipeline.process_call(call_id)
    except NotImplementedError:
        log.warning("pipeline not implemented yet; call %s left unprocessed", call_id)
    except Exception:
        log.exception("processing failed for call %s", call_id)


def _provider_router(name: str) -> APIRouter:
    router = APIRouter(prefix=f"/telephony/{name}", tags=["telephony"])

    @router.post("/answer")
    async def answer(
        request: Request, session: SessionDep, settings: SettingsDep, arms: ArmsDep
    ) -> Response:
        """Caller dialled in. Create a Call, choose an arm, return answer XML
        (consent -> stereo session recording -> Dial arm). If no arm: busy XML."""
        provider = get_provider(name, settings)
        form = await _authenticated_form(request, provider, settings.public_base_url)
        return _respond(
            call_flow.start_call(
                session=session, provider=provider, settings=settings, arms=arms, form=form
            )
        )

    @router.post("/dial-status")
    async def dial_status(
        request: Request, call_id: str, session: SessionDep, settings: SettingsDep
    ) -> Response:
        """Dial finished. Record answered/ended times and duration; mark FAILED if the
        arm never picked up (that call must not count in the stats)."""
        provider = get_provider(name, settings)
        form = await _authenticated_form(request, provider, settings.public_base_url)
        try:
            call_flow.finish_dial(
                session=session, provider=provider, call=_get_call(session, call_id), form=form
            )
        except call_flow.CallMismatch as e:
            raise _mismatch(e) from e
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @router.post("/recording")
    async def recording(
        request: Request,
        call_id: str,
        background: BackgroundTasks,
        session: SessionDep,
        settings: SettingsDep,
    ) -> Response:
        """Session recording is ready. Store recording_url and queue pipeline.process_call."""
        provider = get_provider(name, settings)
        form = await _authenticated_form(request, provider, settings.public_base_url)
        call = _get_call(session, call_id)
        try:
            queue = call_flow.attach_recording(
                session=session, provider=provider, call=call, form=form
            )
        except call_flow.CallMismatch as e:
            raise _mismatch(e) from e
        if queue:
            background.add_task(_process, call.id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router


router = APIRouter()
for _name in provider_names():
    router.include_router(_provider_router(_name))
