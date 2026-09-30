from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .pay import Pay, PayDict


class DistributionDetails(SdkBaseModel):
    """An object representing information about a distribution from the paycheck (for example, the amount distributed to
    a specific checking account, or to a retirement plan)."""

    account_number: OptionalNullable[str] = UNSET
    """The account number of the account being deposited to."""

    bank_account_type: OptionalNullable[str] = UNSET
    """The type of bank account (e.g. Checking or Savings)"""

    bank_name: OptionalNullable[str] = UNSET
    """The name of the bank that the payment is being deposited to."""

    current_pay: Optional[Pay] = UNSET
    """An object representing a monetary amount."""

    description: OptionalNullable[str] = UNSET
    """A description of the distribution type."""


class DistributionDetailsDict(TypedDict):
    account_number: NotRequired[str | None]
    bank_account_type: NotRequired[str | None]
    bank_name: NotRequired[str | None]
    current_pay: NotRequired[PayDict]
    description: NotRequired[str | None]
