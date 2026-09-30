from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.available_balance import AvailableBalanceOrStr


class BankTransferReceiverDetails(SdkBaseModel):
    """The receiver details if the type of this event is ``reciever_pending`` or ``reciever_posted``. Null value
    otherwise."""

    available_balance: AvailableBalanceOrStr
    """The sign of the available balance for the receiver bank account associated with the receiver event at the time
    the matching transaction was found. Can be ``positive``, ``negative``, or null if the balance was not available at
    the time."""


class BankTransferReceiverDetailsDict(TypedDict):
    available_balance: AvailableBalanceOrStr
