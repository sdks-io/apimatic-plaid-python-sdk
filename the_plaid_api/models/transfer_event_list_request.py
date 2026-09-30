from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.transfer_event_type import TransferEventTypeOrStr
from .enums.transfer_type2 import TransferType2OrStr


class TransferEventListRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/event/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    start_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The start datetime of transfers to list. This should be in RFC 3339 format (i.e. ``2019-12-06T22:35:49Z``)"""

    end_date: OptionalNullable[RFC3339DateTime] = UNSET
    """The end datetime of transfers to list. This should be in RFC 3339 format (i.e. ``2019-12-06T22:35:49Z``)"""

    transfer_id: OptionalNullable[str] = UNSET
    """Plaid’s unique identifier for a transfer."""

    account_id: OptionalNullable[str] = UNSET
    """The account ID to get events for all transactions to/from an account."""

    transfer_type: Optional[TransferType2OrStr] = UNSET
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    your origination account; a ``credit`` indicates a transfer of money out of your origination account."""

    event_types: Optional[list[TransferEventTypeOrStr]] = UNSET
    """Filter events by event type."""

    count: int | None = 25
    """The maximum number of transfer events to return. If the number of events matching the above parameters is greater
    than ``count``, the most recent events will be returned."""

    offset: int | None = 0
    """The offset into the list of transfer events. When ``count``=25 and ``offset``=0, the first 25 events will be
    returned. When ``count``=25 and ``offset``=25, the next 25 bank transfer events will be returned."""

    origination_account_id: OptionalNullable[str] = UNSET
    """The origination account ID to get events for transfers from a specific origination account."""


class TransferEventListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    start_date: NotRequired[RFC3339DateTime | None]
    end_date: NotRequired[RFC3339DateTime | None]
    transfer_id: NotRequired[str | None]
    account_id: NotRequired[str | None]
    transfer_type: NotRequired[TransferType2OrStr]
    event_types: NotRequired[list[TransferEventTypeOrStr]]
    count: NotRequired[int | None]
    offset: NotRequired[int | None]
    origination_account_id: NotRequired[str | None]
