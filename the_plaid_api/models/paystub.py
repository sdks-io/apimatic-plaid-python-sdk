from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .deductions import Deductions, DeductionsDict
from .earnings import Earnings, EarningsDict
from .employee import Employee, EmployeeDict
from .employer2 import Employer2, Employer2Dict
from .employment_details import EmploymentDetails, EmploymentDetailsDict
from .income_breakdown import IncomeBreakdown, IncomeBreakdownDict
from .net_pay import NetPay, NetPayDict
from .pay_period_details import PayPeriodDetails, PayPeriodDetailsDict
from .paystub_details import PaystubDetails, PaystubDetailsDict
from .paystub_ytddetails import PaystubYtddetails, PaystubYtddetailsDict


class Paystub(SdkBaseModel):
    """An object representing data extracted from the end user's paystub."""

    deductions: Optional[Deductions] = UNSET
    """An object with the deduction information found on a paystub."""

    doc_id: Optional[str] = UNSET
    """An identifier of the document referenced by the document metadata."""

    earnings: Optional[Earnings] = UNSET
    """An object representing both a breakdown of earnings on a paystub and the total earnings."""

    employer: Employer2
    employee: Employee
    """Data about the employee."""

    employment_details: Optional[EmploymentDetails] = UNSET
    """An object representing employment details found on a paystub."""

    net_pay: Optional[NetPay] = UNSET
    """An object representing information about the net pay amount on the paystub."""

    pay_period_details: PayPeriodDetails
    """Details about the pay period."""

    paystub_details: Optional[PaystubDetails] = UNSET
    """An object representing details that can be found on the paystub."""

    income_breakdown: list[IncomeBreakdown]
    ytd_earnings: PaystubYtddetails
    """The amount of income earned year to date, as based on paystub data."""


class PaystubDict(TypedDict):
    deductions: NotRequired[DeductionsDict]
    doc_id: NotRequired[str]
    earnings: NotRequired[EarningsDict]
    employer: Employer2Dict
    employee: EmployeeDict
    employment_details: NotRequired[EmploymentDetailsDict]
    net_pay: NotRequired[NetPayDict]
    pay_period_details: PayPeriodDetailsDict
    paystub_details: NotRequired[PaystubDetailsDict]
    income_breakdown: list[IncomeBreakdownDict]
    ytd_earnings: PaystubYtddetailsDict
