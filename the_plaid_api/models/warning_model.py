from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cause import Cause, CauseDict


class WarningModel(SdkBaseModel):
    """It is possible for an Asset Report to be returned with missing account owner information. In such cases, the
    Asset Report will contain warning data in the response, indicating why obtaining the owner information failed."""

    warning_type: str
    """The warning type, which will always be ``ASSET_REPORT_WARNING``"""

    warning_code: str
    """The warning code identifies a specific kind of warning. Currently, the only possible warning code is
    ``OWNERS_UNAVAILABLE``, which indicates that account-owner information is not available."""

    cause: Cause
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""


class WarningModelDict(TypedDict):
    warning_type: str
    warning_code: str
    cause: CauseDict
