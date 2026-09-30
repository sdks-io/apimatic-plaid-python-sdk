from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class ItemProductReadyWebhook(SdkBaseModel):
    """Fired once Plaid calculates income from an Item."""

    webhook_type: str
    """``INCOME``"""

    webhook_code: str
    """``PRODUCT_READY``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class ItemProductReadyWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: NotRequired[ErrorDict]
