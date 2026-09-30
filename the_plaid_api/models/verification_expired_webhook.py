from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VerificationExpiredWebhook(SdkBaseModel):
    """Fired when an Item was not verified via automated micro-deposits after ten days since the automated micro-deposit
    was made."""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``VERIFICATION_EXPIRED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    account_id: str
    """The ``account_id`` of the account associated with the webhook"""


class VerificationExpiredWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    account_id: str
