from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee2 import Employee2, Employee2Dict
from .employer3 import Employer3, Employer3Dict
from .income_breakdown import IncomeBreakdown, IncomeBreakdownDict
from .pay_period_details import PayPeriodDetails, PayPeriodDetailsDict


class PaystubOverride(SdkBaseModel):
    """An object representing data from a paystub."""

    employer: Optional[Employer3] = UNSET
    """The employer on the paystub."""

    employee: Optional[Employee2] = UNSET
    """The employee on the paystub."""

    income_breakdown: Optional[list[IncomeBreakdown]] = UNSET
    pay_period_details: Optional[PayPeriodDetails] = UNSET
    """Details about the pay period."""


class PaystubOverrideDict(TypedDict):
    employer: NotRequired[Employer3Dict]
    employee: NotRequired[Employee2Dict]
    income_breakdown: NotRequired[list[IncomeBreakdownDict]]
    pay_period_details: NotRequired[PayPeriodDetailsDict]
