from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_account import CreditAccount, CreditAccountDict
from .depository_account import DepositoryAccount, DepositoryAccountDict
from .investment_account_subtype import InvestmentAccountSubtype, InvestmentAccountSubtypeDict
from .loan_account import LoanAccount, LoanAccountDict


class StandaloneAccountType(SdkBaseModel):
    """The schema below describes the various ``types`` and corresponding ``subtypes`` that Plaid recognizes and reports
    for financial institution accounts."""

    depository: DepositoryAccount
    """An account type holding cash, in which funds are deposited. Supported products for ``depository`` accounts are:
    Auth, Balance, Transactions, Identity, Payment Initiation, and Assets."""

    credit: CreditAccount
    """A credit card type account. Supported products for ``credit`` accounts are: Balance, Transactions, Identity, and
    Liabilities."""

    loan: LoanAccount
    """A loan type account. Supported products for ``loan`` accounts are: Balance, Liabilities, and Transactions."""

    investment: InvestmentAccountSubtype
    """An investment account. Supported products for ``investment`` accounts are: Balance and Investments."""

    other: str
    """Other or unknown account type. Supported products for ``other`` accounts are: Balance, Transactions, Identity,
    and Assets."""


class StandaloneAccountTypeDict(TypedDict):
    depository: DepositoryAccountDict
    credit: CreditAccountDict
    loan: LoanAccountDict
    investment: InvestmentAccountSubtypeDict
    other: str
