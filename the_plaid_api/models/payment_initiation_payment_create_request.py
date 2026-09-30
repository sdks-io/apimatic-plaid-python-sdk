from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .external_payment_schedule_request import ExternalPaymentScheduleRequest, ExternalPaymentScheduleRequestDict
from .payment_amount import PaymentAmount, PaymentAmountDict
from .payment_options import PaymentOptions, PaymentOptionsDict


class PaymentInitiationPaymentCreateRequest(SdkBaseModel):
    """PaymentInitiationPaymentCreateRequest defines the request schema for ``/payment_initiation/payment/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    recipient_id: str
    """The ID of the recipient the payment is for."""

    reference: str
    """A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain
    any special characters (since not all institutions support them)."""

    amount: PaymentAmount
    """The amount and currency of a payment"""

    schedule: Optional[ExternalPaymentScheduleRequest] = UNSET
    """The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up
    as a standing order. If no schedule is specified, the payment will be executed only once."""

    options: Optional[PaymentOptions] = UNSET
    """Additional payment options"""


class PaymentInitiationPaymentCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    recipient_id: str
    reference: str
    amount: PaymentAmountDict
    schedule: NotRequired[ExternalPaymentScheduleRequestDict]
    options: NotRequired[PaymentOptionsDict]
