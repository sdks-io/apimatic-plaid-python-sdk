from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status2(str, Enum):
    """The status of the refund.

    ``PROCESSING``: The refund is currently being processed. The refund will automatically exit this state when
    processing is complete.

    ``INITIATED``: The refund has been successfully initiated.

    ``EXECUTED``: Indicates that the refund has been successfully executed.

    ``FAILED``: The refund has failed to be executed. This error is retryable once the root cause is resolved."""

    PROCESSING = "PROCESSING"
    EXECUTED = "EXECUTED"
    INITIATED = "INITIATED"
    FAILED = "FAILED"

    __str__ = str.__str__


Status2OrStr: TypeAlias = Annotated[Status2 | str, open_enum_validator(Status2)]
