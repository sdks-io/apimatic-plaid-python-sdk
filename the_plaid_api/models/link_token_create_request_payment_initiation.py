from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestPaymentInitiation(SdkBaseModel):
    """Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is
    required if ``payment_initiation`` is included in the ``products`` array."""

    payment_id: str
    """The ``payment_id`` provided by the ``/payment_initiation/payment/create`` endpoint."""


class LinkTokenCreateRequestPaymentInitiationDict(TypedDict):
    payment_id: str
