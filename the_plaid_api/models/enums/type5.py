from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type5(str, Enum):
    """The type of income. Possible values include:
      ``"regular"``: regular income
      ``"overtime"``: overtime income
      ``"bonus"``: bonus income"""

    BONUS = "bonus"
    OVERTIME = "overtime"
    REGULAR = "regular"

    __str__ = str.__str__


Type5OrStr: TypeAlias = Annotated[Type5 | str, open_enum_validator(Type5)]
