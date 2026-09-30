from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.currency import CurrencyOrStr


class PaymentAmount(SdkBaseModel):
    """The amount and currency of a payment"""

    currency: CurrencyOrStr
    """The ISO-4217 currency code of the payment. For standing orders, ``"GBP"`` must be used."""

    value: float
    """The amount of the payment. Must contain at most two digits of precision e.g. ``1.23``. Minimum accepted value is
    ``1``."""


class PaymentAmountDict(TypedDict):
    currency: CurrencyOrStr
    value: float
