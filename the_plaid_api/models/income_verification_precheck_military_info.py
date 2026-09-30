from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.branch import BranchOrStr


class IncomeVerificationPrecheckMilitaryInfo(SdkBaseModel):
    is_active_duty: OptionalNullable[bool] = UNSET
    """Is the user currently active duty in the US military"""

    branch: Optional[BranchOrStr] = UNSET
    """If the user is currently serving in the US military, the branch of the military they are serving in"""


class IncomeVerificationPrecheckMilitaryInfoDict(TypedDict):
    is_active_duty: NotRequired[bool | None]
    branch: NotRequired[BranchOrStr]
