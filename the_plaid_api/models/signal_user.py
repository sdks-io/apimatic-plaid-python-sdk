from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address_data1 import AddressData1, AddressData1Dict
from .signal_person_name import SignalPersonName, SignalPersonNameDict


class SignalUser(SdkBaseModel):
    """Details about the end user initiating the transaction (i.e., the account holder)."""

    name: Optional[SignalPersonName] = UNSET
    """The user's legal name"""

    phone_number: OptionalNullable[str] = UNSET
    """The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567"
    """

    email_address: OptionalNullable[str] = UNSET
    """The user's email address."""

    address: Optional[AddressData1] = UNSET
    """Data about the components comprising an address."""


class SignalUserDict(TypedDict):
    name: NotRequired[SignalPersonNameDict]
    phone_number: NotRequired[str | None]
    email_address: NotRequired[str | None]
    address: NotRequired[AddressData1Dict]
