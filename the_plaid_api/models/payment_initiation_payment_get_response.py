from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.status3 import Status3OrStr
from .external_payment_refund_details import ExternalPaymentRefundDetails, ExternalPaymentRefundDetailsDict
from .external_payment_schedule_get import ExternalPaymentScheduleGet, ExternalPaymentScheduleGetDict
from .payment_amount import PaymentAmount, PaymentAmountDict
from .payment_initiation_refund import PaymentInitiationRefund, PaymentInitiationRefundDict
from .sender_bacsnullable import SenderBacsnullable, SenderBacsnullableDict


class PaymentInitiationPaymentGetResponse(SdkBaseModel):
    """PaymentInitiationPaymentGetResponse defines the response schema for ``/payment_initation/payment/get``"""

    payment_id: str
    """The ID of the payment. Like all Plaid identifiers, the ``payment_id`` is case sensitive."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    status: Status3OrStr
    """The status of the payment.

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

    recipient_id: str
    """The ID of the recipient"""

    reference: str
    """A reference for the payment."""

    adjusted_reference: OptionalNullable[str] = UNSET
    """The value of the reference sent to the bank after adjustment to pass bank validation rules."""

    last_status_update: RFC3339DateTime
    """The date and time of the last time the ``status`` was updated, in IS0 8601 format"""

    schedule: Optional[ExternalPaymentScheduleGet] = UNSET
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up
    as a standing order. If no schedule is specified, the payment will be executed only once."""

    refund_details: Optional[ExternalPaymentRefundDetails] = UNSET
    bacs: SenderBacsnullable
    iban: str | None
    """The International Bank Account Number (IBAN) for the sender, if specified in the
    ``/payment_initiation/payment/create`` call."""

    initiated_refunds: Optional[list[PaymentInitiationRefund]] = UNSET
    """Initiated refunds associated with the payment."""

    emi_account_id: OptionalNullable[str] = UNSET
    """The EMI (E-Money Institution) account that this payment is associated with, if any. This EMI account is used as
    an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationPaymentGetResponseDict(TypedDict):
    payment_id: str
    amount: PaymentAmountDict
    status: Status3OrStr
    recipient_id: str
    reference: str
    adjusted_reference: NotRequired[str | None]
    last_status_update: RFC3339DateTime
    schedule: NotRequired[ExternalPaymentScheduleGetDict]
    refund_details: NotRequired[ExternalPaymentRefundDetailsDict]
    bacs: SenderBacsnullableDict
    iban: str | None
    initiated_refunds: NotRequired[list[PaymentInitiationRefundDict]]
    emi_account_id: NotRequired[str | None]
    request_id: str
