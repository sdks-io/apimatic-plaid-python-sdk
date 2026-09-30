from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.status2 import Status2OrStr
from .payment_amount import PaymentAmount, PaymentAmountDict


class PaymentInitiationRefund(SdkBaseModel):
    """PaymentInitiationRefund defines a payment initiation refund"""

    refund_id: str
    """The ID of the refund. Like all Plaid identifiers, the ``refund_id`` is case sensitive."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    status: Status2OrStr
    """The status of the refund.

    ``PROCESSING``: The refund is currently being processed. The refund will automatically exit this state when
    processing is complete.

    ``INITIATED``: The refund has been successfully initiated.

    ``EXECUTED``: Indicates that the refund has been successfully executed.

    ``FAILED``: The refund has failed to be executed. This error is retryable once the root cause is resolved."""

    last_status_update: RFC3339DateTime
    """The date and time of the last time the ``status`` was updated, in IS0 8601 format"""


class PaymentInitiationRefundDict(TypedDict):
    refund_id: str
    amount: PaymentAmountDict
    status: Status2OrStr
    last_status_update: RFC3339DateTime
