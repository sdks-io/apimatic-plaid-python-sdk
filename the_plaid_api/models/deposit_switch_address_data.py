from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DepositSwitchAddressData(SdkBaseModel):
    """The user's address."""

    city: str
    """The full city name"""

    region: str
    """The region or state Example: ``"NC"``"""

    street: str
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    postal_code: str
    """The postal code"""

    country: str
    """The ISO 3166-1 alpha-2 country code"""


class DepositSwitchAddressDataDict(TypedDict):
    city: str
    region: str
    street: str
    postal_code: str
    country: str
