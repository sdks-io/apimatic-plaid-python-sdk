from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict


class AssetsErrorWebhook(SdkBaseModel):
    """Fired when Asset Report generation has failed. The resulting ``error`` will have an ``error_type`` of
    ``ASSET_REPORT_ERROR``."""

    webhook_type: str
    """``ASSETS``"""

    webhook_code: str
    """``ERROR``"""

    error: Error
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    asset_report_id: str
    """The ID associated with the Asset Report."""


class AssetsErrorWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: ErrorDict
    asset_report_id: str
