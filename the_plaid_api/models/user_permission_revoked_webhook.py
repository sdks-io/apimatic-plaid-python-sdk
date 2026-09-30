from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class UserPermissionRevokedWebhook(SdkBaseModel):
    """The ``USER_PERMISSION_REVOKED`` webhook is fired to when an end user has used the `my.plaid.com portal
    <https://my.plaid.com>`__ to revoke the permission that they previously granted to access an Item. Once access to an
    Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must
    be created for the user."""

    webhook_type: str
    """``ITEM``"""

    webhook_code: str
    """``USER_PERMISSION_REVOKED``"""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Optional[Error] = UNSET
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class UserPermissionRevokedWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    item_id: str
    error: NotRequired[ErrorDict]
