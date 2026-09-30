from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_event import TransferEvent, TransferEventDict


class TransferEventSyncResponse(SdkBaseModel):
    """Defines the response schema for ``/transfer/event/sync``"""

    transfer_events: list[TransferEvent]
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransferEventSyncResponseDict(TypedDict):
    transfer_events: list[TransferEventDict]
    request_id: str
