from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AvailableBalance(str, Enum):
    """The sign of the available balance for the receiver bank account associated with the receiver event at the time
    the matching transaction was found. Can be ``positive``, ``negative``, or null if the balance was not available at
    the time."""

    POSITIVE = "positive"
    NEGATIVE = "negative"

    __str__ = str.__str__


AvailableBalanceOrStr: TypeAlias = Annotated[AvailableBalance | str, open_enum_validator(AvailableBalance)]
