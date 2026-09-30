from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict


class LiabilitiesDefaultUpdateWebhook(SdkBaseModel):
    """The webhook of type ``LIABILITIES`` and code ``DEFAULT_UPDATE`` will be fired when new or updated liabilities
    have been detected on a liabilities item."""

    webhook_type: str
    """``LIABILITIES``"""

    webhook_code: str
    """``DEFAULT_UPDATE``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Error
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    account_ids_with_new_liabilities: list[str]
    """An array of ``account_id``'s for accounts that contain new liabilities."""

    account_ids_with_updated_liabilities: dict[str, Any]
    """An object with keys of ``account_id``'s that are mapped to their respective liabilities fields that changed.

    Example: ``{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["past_amount_due"] }``"""


class LiabilitiesDefaultUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: ErrorDict
    account_ids_with_new_liabilities: list[str]
    account_ids_with_updated_liabilities: dict[str, Any]
