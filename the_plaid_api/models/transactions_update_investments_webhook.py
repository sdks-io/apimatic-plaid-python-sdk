from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class TransactionsUpdateInvestmentsWebhook(SdkBaseModel):
    """Fired when new or canceled transactions have been detected on an investment account."""

    webhook_type: str
    """``INVESTMENTS_TRANSACTIONS``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    new_investments_transactions: float
    """The number of new transactions reported since the last time this webhook was fired."""

    canceled_investments_transactions: float
    """The number of canceled transactions reported since the last time this webhook was fired."""


class TransactionsUpdateInvestmentsWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: NotRequired[ErrorDict]
    new_investments_transactions: float
    canceled_investments_transactions: float
