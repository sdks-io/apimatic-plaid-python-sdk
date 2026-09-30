from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict


class ItemErrorWebhook(SdkBaseModel):
    """Fired when an error is encountered with an Item. The error can be resolved by having the user go through Link’s
    update mode."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``ERROR``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Error
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class ItemErrorWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: ErrorDict
