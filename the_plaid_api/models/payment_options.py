from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_initiation_optional_restriction_bacs import (
    PaymentInitiationOptionalRestrictionBacs,
    PaymentInitiationOptionalRestrictionBacsDict,
)


class PaymentOptions(SdkBaseModel):
    """Additional payment options"""

    request_refund_details: OptionalNullable[bool] = UNSET
    """When ``true``, Plaid will attempt to request refund details from the payee's financial institution. Support
    varies between financial institutions and will not always be available. If refund details could be retrieved, they
    will be available in the ``/payment_initiation/payment/get`` response."""

    iban: OptionalNullable[str] = UNSET
    """The International Bank Account Number (IBAN) for the payer's account. If provided, the end user will be able to
    send payments only from the specified bank account."""

    bacs: Optional[PaymentInitiationOptionalRestrictionBacs] = UNSET
    emi_account_id: OptionalNullable[str] = UNSET
    """The EMI (E-Money Institution) account that this payment is associated with, if any. This EMI account is used as
    an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests."""


class PaymentOptionsDict(TypedDict):
    request_refund_details: NotRequired[bool | None]
    iban: NotRequired[str | None]
    bacs: NotRequired[PaymentInitiationOptionalRestrictionBacsDict]
    emi_account_id: NotRequired[str | None]
