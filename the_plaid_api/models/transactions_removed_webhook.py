from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class TransactionsRemovedWebhook(SdkBaseModel):
    """Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook
    payload. Plaid will typically check for deleted transaction data several times a day."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``TRANSACTIONS_REMOVED``"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    removed_transactions: list[str]
    """An array of ``transaction_ids`` corresponding to the removed transactions"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class TransactionsRemovedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[ErrorDict]
    removed_transactions: list[str]
    item_id: str
