from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.account_subtype1 import AccountSubtype1OrStr


class DepositSwitchTargetAccount(SdkBaseModel):
    account_number: str
    """Account number for deposit switch destination"""

    routing_number: str
    """Routing number for deposit switch destination"""

    account_name: str
    """The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch
    interface. It is not required to match the name used in online banking."""

    account_subtype: AccountSubtype1OrStr
    """The account subtype of the account, either ``checking`` or ``savings``."""


class DepositSwitchTargetAccountDict(TypedDict):
    account_number: str
    routing_number: str
    account_name: str
    account_subtype: AccountSubtype1OrStr
