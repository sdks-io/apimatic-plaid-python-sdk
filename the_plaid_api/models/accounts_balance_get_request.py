from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accounts_balance_get_request_options import AccountsBalanceGetRequestOptions, AccountsBalanceGetRequestOptionsDict


class AccountsBalanceGetRequest(SdkBaseModel):
    """AccountsBalanceGetRequest defines the request schema for ``/accounts/balance/get``"""

    access_token: str
    """The access token associated with the Item data is being requested for."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    options: Optional[AccountsBalanceGetRequestOptions] = UNSET
    """An optional object to filter ``/accounts/balance/get`` results."""


class AccountsBalanceGetRequestDict(TypedDict):
    access_token: str
    secret: NotRequired[str]
    client_id: NotRequired[str]
    options: NotRequired[AccountsBalanceGetRequestOptionsDict]
