from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountSubtype1(str, Enum):
    """The account subtype of the account, either ``checking`` or ``savings``."""

    CHECKING = "checking"
    SAVINGS = "savings"

    __str__ = str.__str__


AccountSubtype1OrStr: TypeAlias = Annotated[AccountSubtype1 | str, open_enum_validator(AccountSubtype1)]
