from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_initiation_standing_order_metadata import (
    PaymentInitiationStandingOrderMetadata,
    PaymentInitiationStandingOrderMetadataDict,
)


class PaymentInitiationMetadata(SdkBaseModel):
    """Metadata that captures what specific payment configurations an institution supports when making Payment
    Initiation requests."""

    supports_international_payments: bool
    """Indicates whether the institution supports payments from a different country."""

    maximum_payment_amount: dict[str, str]
    """A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the
    insitution.

    Example: ``{"GBP": "10000"}``"""

    supports_refund_details: bool
    """Indicates whether the institution supports returning refund details when initiating a payment."""

    standing_order_metadata: PaymentInitiationStandingOrderMetadata
    """Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""


class PaymentInitiationMetadataDict(TypedDict):
    supports_international_payments: bool
    maximum_payment_amount: dict[str, str]
    supports_refund_details: bool
    standing_order_metadata: PaymentInitiationStandingOrderMetadataDict
