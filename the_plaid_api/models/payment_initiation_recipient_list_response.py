from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_initiation_recipient import PaymentInitiationRecipient, PaymentInitiationRecipientDict


class PaymentInitiationRecipientListResponse(SdkBaseModel):
    """PaymentInitiationRecipientListResponse defines the response schema for ``/payment_initiation/recipient/list``"""

    recipients: list[PaymentInitiationRecipient]
    """An array of payment recipients created for Payment Initiation"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationRecipientListResponseDict(TypedDict):
    recipients: list[PaymentInitiationRecipientDict]
    request_id: str
