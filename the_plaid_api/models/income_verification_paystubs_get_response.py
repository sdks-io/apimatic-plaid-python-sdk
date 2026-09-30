from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document_metadata import DocumentMetadata, DocumentMetadataDict
from .error import Error, ErrorDict
from .paystub import Paystub, PaystubDict


class IncomeVerificationPaystubsGetResponse(SdkBaseModel):
    """IncomeVerificationPaystubsGetResponse defines the response schema for ``/income/verification/paystubs/get``."""

    paystubs: list[Paystub]
    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    document_metadata: Optional[list[DocumentMetadata]] = UNSET
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IncomeVerificationPaystubsGetResponseDict(TypedDict):
    paystubs: list[PaystubDict]
    error: NotRequired[ErrorDict]
    document_metadata: NotRequired[list[DocumentMetadataDict]]
    request_id: str
