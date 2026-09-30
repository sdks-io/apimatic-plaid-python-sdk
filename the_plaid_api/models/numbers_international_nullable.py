from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersInternationalNullable(SdkBaseModel):
    account_id: str
    """The Plaid account ID associated with the account numbers"""

    iban: str
    """The International Bank Account Number (IBAN) for the account"""

    bic: str
    """The Bank Identifier Code (BIC) for the account"""


class NumbersInternationalNullableDict(TypedDict):
    account_id: str
    iban: str
    bic: str
