from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class PendingExpirationWebhook(SdkBaseModel):
    """Fired when an Item’s access consent is expiring in 7 days. Some Items have explicit expiration times and we try
    to relay this when possible to reduce service disruption. This can be resolved by having the user go through Link’s
    update mode."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``PENDING_EXPIRATION``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    consent_expiration_time: RFC3339DateTime
    """The date and time at which the Item's access consent will expire, in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format"""


class PendingExpirationWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    consent_expiration_time: RFC3339DateTime
