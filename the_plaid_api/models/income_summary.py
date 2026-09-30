from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .employee_income_summary_field_string import EmployeeIncomeSummaryFieldString, EmployeeIncomeSummaryFieldStringDict
from .employer_income_summary_field_string import EmployerIncomeSummaryFieldString, EmployerIncomeSummaryFieldStringDict
from .pay_frequency import PayFrequency, PayFrequencyDict
from .projected_income_summary_field_number import (
    ProjectedIncomeSummaryFieldNumber,
    ProjectedIncomeSummaryFieldNumberDict,
)
from .transaction_data import TransactionData, TransactionDataDict
from .ytdgross_income_summary_field_number import YtdgrossIncomeSummaryFieldNumber, YtdgrossIncomeSummaryFieldNumberDict
from .ytdnet_income_summary_field_number import YtdnetIncomeSummaryFieldNumber, YtdnetIncomeSummaryFieldNumberDict


class IncomeSummary(SdkBaseModel):
    """The verified fields from a paystub verification. All fields are provided as reported on the paystub."""

    employer_name: EmployerIncomeSummaryFieldString
    employee_name: EmployeeIncomeSummaryFieldString
    ytd_gross_income: YtdgrossIncomeSummaryFieldNumber
    ytd_net_income: YtdnetIncomeSummaryFieldNumber
    pay_frequency: PayFrequency
    projected_wage: ProjectedIncomeSummaryFieldNumber
    verified_transaction: TransactionData
    """Information about the matched direct deposit transaction used to verify a user's payroll information."""


class IncomeSummaryDict(TypedDict):
    employer_name: EmployerIncomeSummaryFieldStringDict
    employee_name: EmployeeIncomeSummaryFieldStringDict
    ytd_gross_income: YtdgrossIncomeSummaryFieldNumberDict
    ytd_net_income: YtdnetIncomeSummaryFieldNumberDict
    pay_frequency: PayFrequencyDict
    projected_wage: ProjectedIncomeSummaryFieldNumberDict
    verified_transaction: TransactionDataDict
