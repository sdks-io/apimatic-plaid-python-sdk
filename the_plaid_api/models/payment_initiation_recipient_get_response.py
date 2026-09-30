from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class PaymentInitiationRecipientGetResponse(SdkBaseModel):
    """PaymentInitiationRecipientGetResponse defines the response schema for ``/payment_initiation/recipient/get``"""

    recipient_id: str
    """The ID of the recipient."""

    name: str
    """The name of the recipient."""

    address: Optional[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient. This object is not currently required to make payments from UK
    institutions and should not be populated, though may be necessary for future European expansion."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the recipient."""

    bacs: Optional[RecipientBacsnullable] = UNSET
    emi_recipient_id: OptionalNullable[str] = UNSET
    """The EMI (E-Money Institution) recipient that this recipient is associated with, if any. This EMI recipient is
    used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation
    requests."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class PaymentInitiationRecipientGetResponseDict(TypedDict):
    recipient_id: str
    name: str
    address: NotRequired[PaymentInitiationAddressDict]
    iban: NotRequired[str | None]
    bacs: NotRequired[RecipientBacsnullableDict]
    emi_recipient_id: NotRequired[str | None]
    request_id: str
