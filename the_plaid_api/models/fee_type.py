from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeeType(SdkBaseModel):
    """Fees on the account, e.g. commission, bookkeeping, options-related."""

    account_fee: Optional[str] = Field(default=UNSET, alias="account fee")
    """Fees paid for account maintenance"""

    adjustment: Optional[str] = UNSET
    """Increase or decrease in quantity of item"""

    dividend: Optional[str] = UNSET
    """Inflow of cash from a dividend"""

    interest: Optional[str] = UNSET
    """Inflow of cash from interest"""

    interest_receivable: Optional[str] = Field(default=UNSET, alias="interest receivable")
    """Inflow of cash from interest receivable"""

    long_term_capital_gain: Optional[str] = Field(default=UNSET, alias="long-term capital gain")
    """Long-term capital gain received as cash"""

    legal_fee: Optional[str] = Field(default=UNSET, alias="legal fee")
    """Fees paid for legal charges or services"""

    management_fee: Optional[str] = Field(default=UNSET, alias="management fee")
    """Fees paid for investment management of a mutual fund or other pooled investment vehicle"""

    margin_expense: Optional[str] = Field(default=UNSET, alias="margin expense")
    """Fees paid for maintaining margin debt"""

    non_qualified_dividend: Optional[str] = Field(default=UNSET, alias="non-qualified dividend")
    """Inflow of cash from a non-qualified dividend"""

    non_resident_tax: Optional[str] = Field(default=UNSET, alias="non-resident tax")
    """Taxes paid on behalf of the investor for non-residency in investment jurisdiction"""

    qualified_dividend: Optional[str] = Field(default=UNSET, alias="qualified dividend")
    """Inflow of cash from a qualified dividend"""

    return_of_principal: Optional[str] = Field(default=UNSET, alias="return of principal")
    """Repayment of loan principal"""

    short_term_capital_gain: Optional[str] = Field(default=UNSET, alias="short-term capital gain")
    """Short-term capital gain received as cash"""

    stock_distribution: Optional[str] = Field(default=UNSET, alias="stock distribution")
    """Inflow of stock from a distribution"""

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


class FeeTypeDict(TypedDict):
    account_fee: NotRequired[str]
    adjustment: NotRequired[str]
    dividend: NotRequired[str]
    interest: NotRequired[str]
    interest_receivable: NotRequired[str]
    long_term_capital_gain: NotRequired[str]
    legal_fee: NotRequired[str]
    management_fee: NotRequired[str]
    margin_expense: NotRequired[str]
    non_qualified_dividend: NotRequired[str]
    non_resident_tax: NotRequired[str]
    qualified_dividend: NotRequired[str]
    return_of_principal: NotRequired[str]
    short_term_capital_gain: NotRequired[str]
    stock_distribution: NotRequired[str]
    tax: NotRequired[str]
    tax_withheld: NotRequired[str]
    transfer_fee: NotRequired[str]
    trust_fee: NotRequired[str]
    unqualified_gain: NotRequired[str]
