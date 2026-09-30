from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferDirection1(str, Enum):
    """Indicates the direction of the transfer: ``outbound``: for API-initiated transfers ``inbound``: for payments
    received by the FBO account."""

    INBOUND = "inbound"
    OUTBOUND = "outbound"

    __str__ = str.__str__


BankTransferDirection1OrStr: TypeAlias = Annotated[
    BankTransferDirection1 | str, open_enum_validator(BankTransferDirection1)
]
