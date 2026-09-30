from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .paystub_override import PaystubOverride, PaystubOverrideDict


class IncomeOverride(SdkBaseModel):
    """Specify payroll data on the account."""

    paystubs: Optional[list[PaystubOverride]] = UNSET
    """A list of paystubs associated with the account."""


class IncomeOverrideDict(TypedDict):
    paystubs: NotRequired[list[PaystubOverrideDict]]
