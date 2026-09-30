from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditAccount(SdkBaseModel):
    """A credit card type account. Supported products for ``credit`` accounts are: Balance, Transactions, Identity, and
    Liabilities."""

    credit_card: str = Field(alias="credit card")
    """Bank-issued credit card"""

    paypal: str
    """PayPal-issued credit card"""


class CreditAccountDict(TypedDict):
    credit_card: str
    paypal: str
