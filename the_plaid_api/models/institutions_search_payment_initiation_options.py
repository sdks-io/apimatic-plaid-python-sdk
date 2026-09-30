from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InstitutionsSearchPaymentInitiationOptions(SdkBaseModel):
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""

    payment_id: Optional[str] = UNSET
    """A unique ID identifying the payment"""


class InstitutionsSearchPaymentInitiationOptionsDict(TypedDict):
    payment_id: NotRequired[str]
