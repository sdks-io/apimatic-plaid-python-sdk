from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CashType(SdkBaseModel):
    """Activity that modifies a cash position"""

    account_fee: Optional[str] = Field(default=UNSET, alias="account fee")
    """Fees paid for account maintenance"""

    contribution: Optional[str] = UNSET
    """Inflow of assets into a tax-advantaged account"""

    deposit: Optional[str] = UNSET
    """Inflow of cash into an account"""

    dividend: Optional[str] = UNSET
    """Inflow of cash from a dividend"""

    stock_distribution: Optional[str] = Field(default=UNSET, alias="stock distribution")
    """Inflow of stock from a distribution"""

    interest: Optional[str] = UNSET
    """Inflow of cash from interest"""

    legal_fee: Optional[str] = Field(default=UNSET, alias="legal fee")
    """Fees paid for legal charges or services"""

    long_term_capital_gain: Optional[str] = Field(default=UNSET, alias="long-term capital gain")
    """Long-term capital gain received as cash"""

    management_fee: Optional[str] = Field(default=UNSET, alias="management fee")
    """Fees paid for investment management of a mutual fund or other pooled investment vehicle"""

    margin_expense: Optional[str] = Field(default=UNSET, alias="margin expense")
    """Fees paid for maintaining margin debt"""

    non_qualified_dividend: Optional[str] = Field(default=UNSET, alias="non-qualified dividend")
    """Inflow of cash from a non-qualified dividend"""

    non_resident_tax: Optional[str] = Field(default=UNSET, alias="non-resident tax")
    """Taxes paid on behalf of the investor for non-residency in investment jurisdiction"""

    pending_credit: Optional[str] = Field(default=UNSET, alias="pending credit")
    """Pending inflow of cash"""

    pending_debit: Optional[str] = Field(default=UNSET, alias="pending debit")
    """Pending outflow of cash"""

    qualified_dividend: Optional[str] = Field(default=UNSET, alias="qualified dividend")
    """Inflow of cash from a qualified dividend"""

    short_term_capital_gain: Optional[str] = Field(default=UNSET, alias="short-term capital gain")
    """Short-term capital gain received as cash"""

    tax: Optional[str] = UNSET
    """Taxes paid on behalf of the investor"""

    tax_withheld: Optional[str] = Field(default=UNSET, alias="tax withheld")
    """Taxes withheld on behalf of the customer"""

    transfer_fee: Optional[str] = Field(default=UNSET, alias="transfer fee")
    """Fees incurred for transfer of a holding or account"""

    trust_fee: Optional[str] = Field(default=UNSET, alias="trust fee")
    """Fees related to adminstration of a trust account"""

    unqualified_gain: Optional[str] = Field(default=UNSET, alias="unqualified gain")
    """Unqualified capital gain received as cash"""

    withdrawal: Optional[str] = UNSET
    """Outflow of cash from an account"""


class CashTypeDict(TypedDict):
    account_fee: NotRequired[str]
    contribution: NotRequired[str]
    deposit: NotRequired[str]
    dividend: NotRequired[str]
    stock_distribution: NotRequired[str]
    interest: NotRequired[str]
    legal_fee: NotRequired[str]
    long_term_capital_gain: NotRequired[str]
    management_fee: NotRequired[str]
    margin_expense: NotRequired[str]
    non_qualified_dividend: NotRequired[str]
    non_resident_tax: NotRequired[str]
    pending_credit: NotRequired[str]
    pending_debit: NotRequired[str]
    qualified_dividend: NotRequired[str]
    short_term_capital_gain: NotRequired[str]
    tax: NotRequired[str]
    tax_withheld: NotRequired[str]
    transfer_fee: NotRequired[str]
    trust_fee: NotRequired[str]
    unqualified_gain: NotRequired[str]
    withdrawal: NotRequired[str]
