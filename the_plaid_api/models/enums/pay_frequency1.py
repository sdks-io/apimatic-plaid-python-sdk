from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayFrequency1(str, Enum):
    """The frequency at which the employee is paid. Possible values: ``MONTHLY``, ``BI-WEEKLY``, ``WEEKLY``,
    ``SEMI-MONTHLY``."""

    MONTHLY = "MONTHLY"
    BI_WEEKLY = "BI-WEEKLY"
    WEEKLY = "WEEKLY"
    SEMI_MONTHLY = "SEMI-MONTHLY"

    __str__ = str.__str__


PayFrequency1OrStr: TypeAlias = Annotated[PayFrequency1 | str, open_enum_validator(PayFrequency1)]
