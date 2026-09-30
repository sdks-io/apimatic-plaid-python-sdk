from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.new_payment_status import NewPaymentStatusOrStr
from .enums.old_payment_status import OldPaymentStatusOrStr
from .error import Error, ErrorDict


class PaymentStatusUpdateWebhook(SdkBaseModel):
    """Fired when the status of a payment has changed."""

    webhook_type: str
    """``PAYMENT_INITIATION``"""

    webhook_code: str
    """``PAYMENT_STATUS_UPDATE``"""

    payment_id: str
    """The ``payment_id`` for the payment being updated"""

    new_payment_status: NewPaymentStatusOrStr
    """The new status of the payment.

    ``PAYMENT_STATUS_INPUT_NEEDED``: This is the initial state of all payments. It indicates that the payment is waiting
    on user input to continue processing. A payment may re-enter this state later on if further input is needed.

    ``PAYMENT_STATUS_PROCESSING``: The payment is currently being processed. The payment will automatically exit this
    state when processing is complete.

    ``PAYMENT_STATUS_INITIATED``: The payment has been successfully initiated and is considered complete.

    ``PAYMENT_STATUS_COMPLETED``: Indicates that the standing order has been successfully established. This state is
    only used for standing orders.

    ``PAYMENT_STATUS_INSUFFICIENT_FUNDS``: The payment has failed due to insufficient funds.

    ``PAYMENT_STATUS_FAILED``: The payment has failed to be initiated. This error is retryable once the root cause is
    resolved.

    ``PAYMENT_STATUS_BLOCKED``: The payment has been blocked. This is a retryable error.

    ``PAYMENT_STATUS_UNKNOWN``: The payment status is unknown."""

    old_payment_status: OldPaymentStatusOrStr
    """The previous status of the payment.

    ``PAYMENT_STATUS_INPUT_NEEDED``: This is the initial state of all payments. It indicates that the payment is waiting
    on user input to continue processing. A payment may re-enter this state later on if further input is needed.

    ``PAYMENT_STATUS_PROCESSING``: The payment is currently being processed. The payment will automatically exit this
    state when processing is complete.

    ``PAYMENT_STATUS_INITIATED``: The payment has been successfully initiated and is considered complete.

    ``PAYMENT_STATUS_COMPLETED``: Indicates that the standing order has been successfully established. This state is
    only used for standing orders.

    ``PAYMENT_STATUS_INSUFFICIENT_FUNDS``: The payment has failed due to insufficient funds.

    ``PAYMENT_STATUS_FAILED``: The payment has failed to be initiated. This error is retryable once the root cause is
    resolved.

    ``PAYMENT_STATUS_BLOCKED``: The payment has been blocked. This is a retryable error.

    ``PAYMENT_STATUS_UNKNOWN``: The payment status is unknown."""

    original_reference: str | None
    """The original value of the reference when creating the payment."""

    adjusted_reference: OptionalNullable[str] = UNSET
    """The value of the reference sent to the bank after adjustment to pass bank validation rules."""

    original_start_date: Date | None
    """The original value of the ``start_date`` provided during the creation of a standing order. If the payment is not
    a standing order, this field will be ``null``."""

    adjusted_start_date: Date | None
    """The start date sent to the bank after adjusting for holidays or weekends. Will be provided in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD). If the start date did not require adjustment, or if
    the payment is not a standing order, this field will be ``null``."""

    timestamp: RFC3339DateTime
    """The timestamp of the update, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format, e.g.
    ``"2017-09-14T14:42:19.350Z"``"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class PaymentStatusUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    payment_id: str
    new_payment_status: NewPaymentStatusOrStr
    old_payment_status: OldPaymentStatusOrStr
    original_reference: str | None
    adjusted_reference: NotRequired[str | None]
    original_start_date: Date | None
    adjusted_start_date: Date | None
    timestamp: RFC3339DateTime
    error: NotRequired[ErrorDict]
