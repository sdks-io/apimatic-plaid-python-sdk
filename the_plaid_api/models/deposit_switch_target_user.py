from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deposit_switch_address_data import DepositSwitchAddressData, DepositSwitchAddressDataDict


class DepositSwitchTargetUser(SdkBaseModel):
    given_name: str
    """The given name (first name) of the user."""

    family_name: str
    """The family name (last name) of the user."""

    phone: str
    """The phone number of the user. The endpoint can accept a variety of phone number formats, including E.164."""

    email: str
    """The email address of the user."""

    address: Optional[DepositSwitchAddressData] = UNSET
    """The user's address."""

    tax_payer_id: Optional[str] = UNSET
    """The taxpayer ID of the user, generally their SSN, EIN, or TIN."""


class DepositSwitchTargetUserDict(TypedDict):
    given_name: str
    family_name: str
    phone: str
    email: str
    address: NotRequired[DepositSwitchAddressDataDict]
    tax_payer_id: NotRequired[str]
