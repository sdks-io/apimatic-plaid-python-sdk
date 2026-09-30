from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Confidence(str, Enum):
    """The confidence that Plaid can support the user in the income verification flow. One of the following:

    ``"HIGH"``: This precheck information submitted is definitively tied to a Plaid-supported integration.

    "``LOW``": This precheck information submitted is known not to be supported by Plaid.

    ``"UNKNOWN"``: It was not possible to determine if the user is supportable with the information passed."""

    HIGH = "HIGH"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"

    __str__ = str.__str__


ConfidenceOrStr: TypeAlias = Annotated[Confidence | str, open_enum_validator(Confidence)]
