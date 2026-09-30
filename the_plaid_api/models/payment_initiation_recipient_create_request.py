from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class PaymentInitiationRecipientCreateRequest(SdkBaseModel):
    """PaymentInitiationRecipientCreateRequest defines the request schema for
    ``/payment_initiation/recipient/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    name: str
    """The name of the recipient"""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is
    required."""

    bacs: Optional[RecipientBacsnullable] = UNSET
    address: Optional[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient. This object is not currently required to make payments from UK
    institutions and should not be populated, though may be necessary for future European expansion."""


class PaymentInitiationRecipientCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    name: str
    iban: NotRequired[str | None]
    bacs: NotRequired[RecipientBacsnullableDict]
    address: NotRequired[PaymentInitiationAddressDict]
