from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class NewAccountsAvailableWebhook(SdkBaseModel):
    """Fired when Plaid detects a new account for Items created or updated with `Account Select v2
    <https://plaid.com/docs/link/customization/#account-select>`__. Upon receiving this webhook, you can prompt your
    users to share new accounts with you through `Account Select v2 update mode
    <https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts>`__."""

    webhook_type: Optional[str] = UNSET
    """``ITEM``"""

    webhook_code: Optional[str] = UNSET
    """``NEW_ACCOUNTS_AVAILABLE``"""

    item_id: Optional[str] = UNSET
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class NewAccountsAvailableWebhookDict(TypedDict):
    webhook_type: NotRequired[str]
    webhook_code: NotRequired[str]
    item_id: NotRequired[str]
    error: NotRequired[ErrorDict]
