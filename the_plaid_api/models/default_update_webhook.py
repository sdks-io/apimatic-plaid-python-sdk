from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DefaultUpdateWebhook(SdkBaseModel):
    """Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data
    several times a day."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    new_transactions: float
    """The number of new transactions detected since the last time this webhook was fired."""

    item_id: str
    """The ``item_id`` of the Item the webhook relates to."""


class DefaultUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[ErrorDict]
    new_transactions: float
    item_id: str
