from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferGetRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transfer_id: str
    """Plaid’s unique identifier for a transfer."""


class TransferGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transfer_id: str
