from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .recipient_bacsnullable import RecipientBacsnullable, RecipientBacsnullableDict


class ExternalPaymentRefundDetails(SdkBaseModel):
    name: str
    """The name of the account holder."""

    iban: str | None
    """The International Bank Account Number (IBAN) for the account."""

    bacs: RecipientBacsnullable


class ExternalPaymentRefundDetailsDict(TypedDict):
    name: str
    iban: str | None
    bacs: RecipientBacsnullableDict
