from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferType1(str, Enum):
    """The type of bank transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money
    into your origination account; a ``credit`` indicates a transfer of money out of your origination account."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


BankTransferType1OrStr: TypeAlias = Annotated[BankTransferType1 | str, open_enum_validator(BankTransferType1)]
