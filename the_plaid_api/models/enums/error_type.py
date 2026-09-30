from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorType(str, Enum):
    """A broad categorization of the error. Safe for programatic use."""

    INVALID_REQUEST = "INVALID_REQUEST"
    INVALID_RESULT = "INVALID_RESULT"
    INVALID_INPUT = "INVALID_INPUT"
    INSTITUTION_ERROR = "INSTITUTION_ERROR"
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"
    API_ERROR = "API_ERROR"
    ITEM_ERROR = "ITEM_ERROR"
    ASSET_REPORT_ERROR = "ASSET_REPORT_ERROR"
    RECAPTCHA_ERROR = "RECAPTCHA_ERROR"
    OAUTH_ERROR = "OAUTH_ERROR"
    PAYMENT_ERROR = "PAYMENT_ERROR"
    BANK_TRANSFER_ERROR = "BANK_TRANSFER_ERROR"

    __str__ = str.__str__


ErrorTypeOrStr: TypeAlias = Annotated[ErrorType | str, open_enum_validator(ErrorType)]
