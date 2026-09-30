from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AutomaticallyVerifiedWebhook(SdkBaseModel):
    """Fired when an Item is verified via automated micro-deposits. We recommend communicating to your users when this
    event is received to notify them that their account is verified and ready for use."""

    webhook_type: str
    """``AUTH``"""

    webhook_code: str
    """``AUTOMATICALLY_VERIFIED``"""

    account_id: str
    """The ``account_id`` of the account associated with the webhook"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class AutomaticallyVerifiedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    account_id: str
    item_id: str
