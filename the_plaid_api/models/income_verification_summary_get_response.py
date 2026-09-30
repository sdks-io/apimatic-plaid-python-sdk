from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .income_summary import IncomeSummary, IncomeSummaryDict


class IncomeVerificationSummaryGetResponse(SdkBaseModel):
    """IncomeVerificationSummaryGetResponse defines the response schema for ``/income/verification/summary/get``."""

    income_summaries: list[IncomeSummary]
    """A list of income summaries."""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IncomeVerificationSummaryGetResponseDict(TypedDict):
    income_summaries: list[IncomeSummaryDict]
    error: NotRequired[ErrorDict]
    request_id: str
