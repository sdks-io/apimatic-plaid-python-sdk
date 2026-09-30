from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status2 import Status2OrStr


class PaymentInitiationPaymentReverseResponse(SdkBaseModel):
    """PaymentInitiationPaymentReverseResponse defines the response schema for ``/payment_initation/payment/reverse``"""

    refund_id: str
    """A unique ID identifying the refund"""

    status: Status2OrStr
    """The status of the refund.

    ``PROCESSING``: The refund is currently being processed. The refund will automatically exit this state when
    processing is complete.

    ``INITIATED``: The refund has been successfully initiated.

    ``EXECUTED``: Indicates that the refund has been successfully executed.

    ``FAILED``: The refund has failed to be executed. This error is retryable once the root cause is resolved."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationPaymentReverseResponseDict(TypedDict):
    refund_id: str
    status: Status2OrStr
    request_id: str
