from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BankTransferSweepGetRequest(SdkBaseModel):
    """BankTransferSweepGetRequest defines the request schema for ``/bank_transfer/sweep/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    sweep_id: int
    """Identifier of the sweep."""

    origination_account_id: OptionalNullable[str] = UNSET
    """If multiple origination accounts are available, ``origination_account_id`` must be used to specify the account
    that the sweep belongs to."""


class BankTransferSweepGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    sweep_id: int
    origination_account_id: NotRequired[str | None]
