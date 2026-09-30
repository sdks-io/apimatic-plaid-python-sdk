from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class WebhookUpdateAcknowledgedWebhook(SdkBaseModel):
    """Fired when an Item's webhook is updated. This will be sent to the newly specified webhook."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``WEBHOOK_UPDATE_ACKNOWLEDGED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    new_webhook_url: str
    """The new webhook URL"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class WebhookUpdateAcknowledgedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    new_webhook_url: str
    error: NotRequired[ErrorDict]
