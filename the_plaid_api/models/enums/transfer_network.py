from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferNetwork(str, Enum):
    """The network or rails used for the transfer. Valid options are ``ach`` or ``same-day-ach``."""

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"

    __str__ = str.__str__


TransferNetworkOrStr: TypeAlias = Annotated[TransferNetwork | str, open_enum_validator(TransferNetwork)]
