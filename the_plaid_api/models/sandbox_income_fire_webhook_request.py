from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.verification_status3 import VerificationStatus3OrStr


class SandboxIncomeFireWebhookRequest(SdkBaseModel):
    """SandboxIncomeFireWebhookRequest defines the request schema for ``/sandbox/income/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    income_verification_id: str
    """The ID of the verification."""

    webhook: str
    """The URL to which the webhook should be sent."""

    verification_status: VerificationStatus3OrStr
    """``VERIFICATION_STATUS_PROCESSING_COMPLETE``: The income verification status processing has completed.

    ``VERIFICATION_STATUS_DOCUMENT_REJECTED``: The documentation uploaded by the end user was recognized as a supported
    file format, but not recognized as a valid paystub.

    ``VERIFICATION_STATUS_PROCESSING_FAILED``: A failure occurred when attempting to process the verification
    documentation."""


class SandboxIncomeFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    income_verification_id: str
    webhook: str
    verification_status: VerificationStatus3OrStr
