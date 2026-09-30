from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deposit_switch_create_request_options import (
    DepositSwitchCreateRequestOptions,
    DepositSwitchCreateRequestOptionsDict,
)
from .deposit_switch_target_account import DepositSwitchTargetAccount, DepositSwitchTargetAccountDict
from .deposit_switch_target_user import DepositSwitchTargetUser, DepositSwitchTargetUserDict
from .enums.country_code1 import CountryCode1OrStr


class DepositSwitchAltCreateRequest(SdkBaseModel):
    """DepositSwitchAltCreateRequest defines the request schema for ``/deposit_switch/alt/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    target_account: DepositSwitchTargetAccount
    target_user: DepositSwitchTargetUser
    options: Optional[DepositSwitchCreateRequestOptions] = UNSET
    """Options to configure the ``/deposit_switch/create`` request. If provided, cannot be ``null``."""

    country_code: Optional[CountryCode1OrStr] = UNSET
    """ISO-3166-1 alpha-2 country code standard."""


class DepositSwitchAltCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    target_account: DepositSwitchTargetAccountDict
    target_user: DepositSwitchTargetUserDict
    options: NotRequired[DepositSwitchCreateRequestOptionsDict]
    country_code: NotRequired[CountryCode1OrStr]
