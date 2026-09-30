from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductDataType(str, Enum):
    ACCOUNT_BALANCE = "ACCOUNT_BALANCE"
    ACCOUNT_USER_INFO = "ACCOUNT_USER_INFO"
    ACCOUNT_TRANSACTIONS = "ACCOUNT_TRANSACTIONS"

    __str__ = str.__str__


ProductDataTypeOrStr: TypeAlias = Annotated[ProductDataType | str, open_enum_validator(ProductDataType)]
