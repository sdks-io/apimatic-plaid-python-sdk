from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class HistoricalUpdateWebhook(SdkBaseModel):
    """Fired when an Item's historical transaction pull is completed and Plaid has prepared as much historical
    transaction data as possible for the Item. Once this webhook has been fired, transaction data beyond the most recent
    30 days can be fetched for the Item. If `Account Select v2
    <https://plaid.com/docs/link/customization/#account-select>`__ is enabled, this webhook will also be fired if
    account selections for the Item are updated, with ``num_transactions`` set to the number of net new transactions
    pulled after the account selection update."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``HISTORICAL_UPDATE``"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    new_transactions: float
    """The number of new, unfetched transactions available"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class HistoricalUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[ErrorDict]
    new_transactions: float
    item_id: str
