from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_failure import TransferFailure, TransferFailureDict


class SandboxTransferSimulateRequest(SdkBaseModel):
    """Defines the request schema for ``/sandbox/transfer/simulate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: str
    """Plaid’s unique identifier for a transfer."""

    event_type: str
    """The asynchronous event to be simulated. May be: ``posted``, ``failed``, or ``reversed``.

    An error will be returned if the event type is incompatible with the current transfer status. Compatible status -->
    event type transitions include:

    ``pending`` --> ``failed``

    ``pending`` --> ``posted``

    ``posted`` --> ``reversed``"""

    failure_reason: Optional[TransferFailure] = UNSET
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""


class SandboxTransferSimulateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: str
    event_type: str
    failure_reason: NotRequired[TransferFailureDict]
