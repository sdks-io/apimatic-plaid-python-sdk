from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Code(str, Enum):
    """A code representing the rationale for permitting or declining the proposed transfer. Possible values are:

    ``NSF`` – Transaction likely to result in a return due to insufficient funds.

    ``RISK`` - Transaction is high-risk.

    ``MANUALLY_VERIFIED_ITEM`` – Item created via same-day micro deposits, limited information available. Plaid can only
    offer ``permitted`` as a transaction decision.

    ``LOGIN_REQUIRED`` – Unable to collect the account information required for an authorization decision due to Item
    staleness. Can be rectified using Link update mode.

    ``ERROR`` – Unable to collect the account information required for an authorization decision due to an error."""

    NSF = "NSF"
    RISK = "RISK"
    MANUALLY_VERIFIED_ITEM = "MANUALLY_VERIFIED_ITEM"
    LOGIN_REQUIRED = "LOGIN_REQUIRED"
    ERROR = "ERROR"

    __str__ = str.__str__


CodeOrStr: TypeAlias = Annotated[Code | str, open_enum_validator(Code)]
