from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Branch(str, Enum):
    """If the user is currently serving in the US military, the branch of the military they are serving in"""

    AIR_FORCE = "AIR FORCE"
    ARMY = "ARMY"
    COAST_GUARD = "COAST GUARD"
    MARINES = "MARINES"
    NAVY = "NAVY"

    __str__ = str.__str__


BranchOrStr: TypeAlias = Annotated[Branch | str, open_enum_validator(Branch)]
