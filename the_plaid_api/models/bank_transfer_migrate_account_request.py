from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BankTransferMigrateAccountRequest(SdkBaseModel):
    """Defines the request schema for ``/bank_transfer/migrate_account``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    account_number: str
    """The user's account number."""

    routing_number: str
    """The user's routing number."""

    account_type: str
    """The type of the bank account (``checking`` or ``savings``)."""


class BankTransferMigrateAccountRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    account_number: str
    routing_number: str
    account_type: str
