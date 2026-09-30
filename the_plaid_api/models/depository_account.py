from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DepositoryAccount(SdkBaseModel):
    """An account type holding cash, in which funds are deposited. Supported products for ``depository`` accounts are:
    Auth, Balance, Transactions, Identity, Payment Initiation, and Assets."""

    checking: str
    """Checking account"""

    savings: str
    """Savings account"""

    hsa: str
    """Health Savings Account (US only) that can only hold cash"""

    cd: str
    """Certificate of deposit account"""

    money_market: str = Field(alias="money market")
    """Money market account"""

    paypal: str
    """PayPal depository account"""

    prepaid: str
    """Prepaid debit card"""

    cash_management: str = Field(alias="cash management")
    """A cash management account, typically a cash account at a brokerage"""

    ebt: str
    """An Electronic Benefit Transfer (EBT) account, used by certain public assistance programs to distribute funds (US
    only)"""


class DepositoryAccountDict(TypedDict):
    checking: str
    savings: str
    hsa: str
    cd: str
    money_market: str
    paypal: str
    prepaid: str
    cash_management: str
    ebt: str
