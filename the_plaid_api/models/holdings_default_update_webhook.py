from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class HoldingsDefaultUpdateWebhook(SdkBaseModel):
    """Fired when new or updated holdings have been detected on an investment account. The webhook typically fires once
    per day, after market close, in response to any newly added holdings or price changes to existing holdings."""

    webhook_type: str
    """``HOLDINGS``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    new_holdings: float
    """The number of new holdings reported since the last time this webhook was fired."""

    updated_holdings: float
    """The number of updated holdings reported since the last time this webhook was fired."""


class HoldingsDefaultUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: NotRequired[ErrorDict]
    new_holdings: float
    updated_holdings: float
