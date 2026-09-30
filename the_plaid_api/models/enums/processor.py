from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Processor(str, Enum):
    """The processor you are integrating with."""

    ACHQ = "achq"
    ALPACA = "alpaca"
    ASTRA = "astra"
    CHECK = "check"
    CHECKBOOK = "checkbook"
    CIRCLE = "circle"
    DRIVEWEALTH = "drivewealth"
    DWOLLA = "dwolla"
    GALILEO = "galileo"
    LITHIC = "lithic"
    MODERN_TREASURY = "modern_treasury"
    MOOV = "moov"
    OCROLUS = "ocrolus"
    PRIME_TRUST = "prime_trust"
    RIZE = "rize"
    SILA_MONEY = "sila_money"
    SVB_API = "svb_api"
    TREASURY_PRIME = "treasury_prime"
    UNIT = "unit"
    VESTA = "vesta"
    VOPAY = "vopay"
    WYRE = "wyre"

    __str__ = str.__str__


ProcessorOrStr: TypeAlias = Annotated[Processor | str, open_enum_validator(Processor)]
