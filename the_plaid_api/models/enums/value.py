from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Value(str, Enum):
    """The frequency of the pay period."""

    MONTHLY = "monthly"
    SEMIMONTHLY = "semimonthly"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    UNKNOWN = "unknown"
    NULL = "null"

    __str__ = str.__str__


ValueOrStr: TypeAlias = Annotated[Value | str, open_enum_validator(Value)]
