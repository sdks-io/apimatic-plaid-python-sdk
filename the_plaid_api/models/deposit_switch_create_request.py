from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deposit_switch_create_request_options import (
    DepositSwitchCreateRequestOptions,
    DepositSwitchCreateRequestOptionsDict,
)
from .enums.country_code1 import CountryCode1OrStr


class DepositSwitchCreateRequest(SdkBaseModel):
    """DepositSwitchCreateRequest defines the request schema for ``/deposit_switch/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    target_access_token: str
    """Access token for the target Item, typically provided in the Import Item response."""

    target_account_id: str
    """Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's
    direct deposit."""

    country_code: Optional[CountryCode1OrStr] = UNSET
    """ISO-3166-1 alpha-2 country code standard."""

    options: Optional[DepositSwitchCreateRequestOptions] = UNSET
    """Options to configure the ``/deposit_switch/create`` request. If provided, cannot be ``null``."""


class DepositSwitchCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    target_access_token: str
    target_account_id: str
    country_code: NotRequired[CountryCode1OrStr]
    options: NotRequired[DepositSwitchCreateRequestOptionsDict]
