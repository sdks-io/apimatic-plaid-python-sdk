from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error import Error, ErrorDict


class Cause(SdkBaseModel):
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""

    error: Error
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""


class CauseDict(TypedDict):
    item_id: str
    error: ErrorDict
