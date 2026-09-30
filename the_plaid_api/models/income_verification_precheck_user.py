from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address_data1 import AddressData1, AddressData1Dict


class IncomeVerificationPrecheckUser(SdkBaseModel):
    first_name: OptionalNullable[str] = UNSET
    """The user's first name"""

    last_name: OptionalNullable[str] = UNSET
    """The user's last name"""

    email_address: OptionalNullable[str] = UNSET
    """The user's email address"""

    home_address: Optional[AddressData1] = UNSET
    """Data about the components comprising an address."""


class IncomeVerificationPrecheckUserDict(TypedDict):
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    home_address: NotRequired[AddressData1Dict]
