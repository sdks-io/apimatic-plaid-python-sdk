from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.confidence import ConfidenceOrStr


class IncomeVerificationPrecheckResponse(SdkBaseModel):
    """IncomeVerificationPrecheckResponse defines the response schema for ``/income/verification/precheck``."""

    precheck_id: str
    """ID of the precheck."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    confidence: ConfidenceOrStr
    """The confidence that Plaid can support the user in the income verification flow. One of the following:

    ``"HIGH"``: This precheck information submitted is definitively tied to a Plaid-supported integration.

    "``LOW``": This precheck information submitted is known not to be supported by Plaid.

    ``"UNKNOWN"``: It was not possible to determine if the user is supportable with the information passed."""


class IncomeVerificationPrecheckResponseDict(TypedDict):
    precheck_id: str
    request_id: str
    confidence: ConfidenceOrStr
