from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Currency(str, Enum):
    """The ISO-4217 currency code of the payment. For standing orders, ``"GBP"`` must be used."""

    GBP = "GBP"
    EUR = "EUR"

    __str__ = str.__str__


CurrencyOrStr: TypeAlias = Annotated[Currency | str, open_enum_validator(Currency)]
