from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .paystub import Paystub, PaystubDict


class IncomeVerificationPaystubGetResponse(SdkBaseModel):
    """IncomeVerificationPaystubGetResponse defines the response schema for ``/income/verification/paystub/get``."""

    paystub: Paystub
    """An object representing data extracted from the end user's paystub."""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IncomeVerificationPaystubGetResponseDict(TypedDict):
    paystub: PaystubDict
    error: NotRequired[ErrorDict]
    request_id: str
