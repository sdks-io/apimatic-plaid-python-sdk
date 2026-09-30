from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.transfer_event_type import TransferEventTypeOrStr
from .enums.transfer_type1 import TransferType1OrStr
from .transfer_failure import TransferFailure, TransferFailureDict


class TransferEvent(SdkBaseModel):
    """Represents an event in the Transfers API."""

    event_id: int
    """Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers."""

    timestamp: RFC3339DateTime
    """The datetime when this event occurred. This will be of the form ``2006-01-02T15:04:05Z``."""

    event_type: TransferEventTypeOrStr
    """The type of event that this transfer represents.

    ``pending``: A new transfer was created; it is in the pending state.

    ``cancelled``: The transfer was cancelled by the client.

    ``failed``: The transfer failed, no funds were moved.

    ``posted``: The transfer has been successfully submitted to the payment network.

    ``reversed``: A posted transfer was reversed."""

    account_id: str
    """The account ID associated with the transfer."""

    transfer_id: str
    """Plaid’s unique identifier for a transfer."""

    origination_account_id: str | None
    """The ID of the origination account that this balance belongs to."""

    transfer_type: TransferType1OrStr
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    transfer_amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. “10.00”)."""

    failure_reason: TransferFailure
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""


class TransferEventDict(TypedDict):
    event_id: int
    timestamp: RFC3339DateTime
    event_type: TransferEventTypeOrStr
    account_id: str
    transfer_id: str
    origination_account_id: str | None
    transfer_type: TransferType1OrStr
    transfer_amount: str
    failure_reason: TransferFailureDict
