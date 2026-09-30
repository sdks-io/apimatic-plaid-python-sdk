from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IncomeVerificationDocumentsDownloadResponse(SdkBaseModel):
    """IncomeVerificationDocumentsDownloadResponse defines the response schema for
    ``/income/verification/documents/download``."""

    id: str


class IncomeVerificationDocumentsDownloadResponseDict(TypedDict):
    id: str
