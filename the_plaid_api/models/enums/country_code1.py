from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CountryCode1(str, Enum):
    """ISO-3166-1 alpha-2 country code standard."""

    US = "US"
    CA = "CA"

    __str__ = str.__str__


CountryCode1OrStr: TypeAlias = Annotated[CountryCode1 | str, open_enum_validator(CountryCode1)]
