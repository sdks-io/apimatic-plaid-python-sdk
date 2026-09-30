from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferType2(str, Enum):
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    your origination account; a ``credit`` indicates a transfer of money out of your origination account."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


TransferType2OrStr: TypeAlias = Annotated[TransferType2 | str, open_enum_validator(TransferType2)]
