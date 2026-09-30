from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferStatus(str, Enum):
    """The status of the transfer."""

    PENDING = "pending"
    POSTED = "posted"
    CANCELLED = "cancelled"
    FAILED = "failed"
    REVERSED = "reversed"

    __str__ = str.__str__


TransferStatusOrStr: TypeAlias = Annotated[TransferStatus | str, open_enum_validator(TransferStatus)]
