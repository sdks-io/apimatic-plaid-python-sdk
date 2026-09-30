from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_subtype import AccountSubtypeOrStr


class InstitutionsSearchAccountFilter(SdkBaseModel):
    loan: Optional[list[AccountSubtypeOrStr]] = UNSET
    depository: Optional[list[AccountSubtypeOrStr]] = UNSET
    credit: Optional[list[AccountSubtypeOrStr]] = UNSET
    investment: Optional[list[AccountSubtypeOrStr]] = UNSET


class InstitutionsSearchAccountFilterDict(TypedDict):
    loan: NotRequired[list[AccountSubtypeOrStr]]
    depository: NotRequired[list[AccountSubtypeOrStr]]
    credit: NotRequired[list[AccountSubtypeOrStr]]
    investment: NotRequired[list[AccountSubtypeOrStr]]
