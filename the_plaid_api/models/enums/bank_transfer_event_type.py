from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferEventType(str, Enum):
    """The type of event that this bank transfer represents.

    ``pending``: A new transfer was created; it is in the pending state.

    ``cancelled``: The transfer was cancelled by the client.

    ``failed``: The transfer failed, no funds were moved.

    ``posted``: The transfer has been successfully submitted to the payment network.

    ``reversed``: A posted transfer was reversed.

    ``receiver_pending``: The matching transfer was found as a pending transaction in the receiver's account

    ``receiver_posted``: The matching transfer was found as a posted transaction in the receiver's account"""

    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    POSTED = "posted"
    REVERSED = "reversed"
    RECEIVER_PENDING = "receiver_pending"
    RECEIVER_POSTED = "receiver_posted"

    __str__ = str.__str__


BankTransferEventTypeOrStr: TypeAlias = Annotated[
    BankTransferEventType | str, open_enum_validator(BankTransferEventType)
]
