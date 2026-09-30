from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IncomeVerificationRefreshResponse(SdkBaseModel):
    """IncomeVerificationRequestResponse defines the response schema for ``/income/verification/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    verification_refresh_status: str
    """The verification refresh status. One of the following:

    ``"VERIFICATION_REFRESH_STATUS_USER_PRESENCE_REQUIRED"`` User presence is required to refresh an income
    verification."""


class IncomeVerificationRefreshResponseDict(TypedDict):
    request_id: str
    verification_refresh_status: str
