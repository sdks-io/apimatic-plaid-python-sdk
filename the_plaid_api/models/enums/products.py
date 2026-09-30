from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Products(str, Enum):
    """A list of products that an institution can support. All Items must be initialized with at least one product. The
    Balance product is always available and does not need to be specified during initialization."""

    ASSETS = "assets"
    AUTH = "auth"
    BALANCE = "balance"
    IDENTITY = "identity"
    INVESTMENTS = "investments"
    LIABILITIES = "liabilities"
    PAYMENT_INITIATION = "payment_initiation"
    TRANSACTIONS = "transactions"
    CREDIT_DETAILS = "credit_details"
    INCOME = "income"
    INCOME_VERIFICATION = "income_verification"
    DEPOSIT_SWITCH = "deposit_switch"
    STANDING_ORDERS = "standing_orders"
    TRANSFER = "transfer"

    __str__ = str.__str__


ProductsOrStr: TypeAlias = Annotated[Products | str, open_enum_validator(Products)]
