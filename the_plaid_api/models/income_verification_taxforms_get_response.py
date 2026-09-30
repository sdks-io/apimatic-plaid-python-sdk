from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .document_metadata import DocumentMetadata, DocumentMetadataDict
from .error import Error, ErrorDict
from .taxform import Taxform, TaxformDict


class IncomeVerificationTaxformsGetResponse(SdkBaseModel):
    """IncomeVerificationTaxformsGetResponse defines the response schema for ``/income/verification/taxforms/get``"""

    request_id: Optional[str] = UNSET
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    taxforms: list[Taxform]
    """A list of taxforms."""

    document_metadata: list[DocumentMetadata]
    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class IncomeVerificationTaxformsGetResponseDict(TypedDict):
    request_id: NotRequired[str]
    taxforms: list[TaxformDict]
    document_metadata: list[DocumentMetadataDict]
    error: NotRequired[ErrorDict]
