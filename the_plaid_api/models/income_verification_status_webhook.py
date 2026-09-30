from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class IncomeVerificationStatusWebhook(SdkBaseModel):
    """Fired when the status of an income verification instance has changed. It will typically take several minutes for
    this webhook to fire after the end user has uploaded their documents in the Document Income flow."""

    webhook_type: str
    """``"INCOME"``"""

    webhook_code: str
    """``income_verification``"""

    income_verification_id: str
    """The ``income_verification_id`` of the verification instance whose status is being reported."""

    verification_status: str
    """``VERIFICATION_STATUS_PROCESSING_COMPLETE``: The income verification status processing has completed.

    ``VERIFICATION_STATUS_UPLOAD_ERROR``: An upload error occurred when the end user attempted to upload their
    verification documentation.

    ``VERIFICATION_STATUS_INVALID_TYPE``: The end user attempted to upload verification documentation in an unsupported
    file format.

    ``VERIFICATION_STATUS_DOCUMENT_REJECTED``: The documentation uploaded by the end user was recognized as a supported
    file format, but not recognized as a valid paystub.

    ``VERIFICATION_STATUS_PROCESSING_FAILED``: A failure occurred when attempting to process the verification
    documentation."""


class IncomeVerificationStatusWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    income_verification_id: str
    verification_status: str
