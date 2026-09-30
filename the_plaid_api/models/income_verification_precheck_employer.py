from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class IncomeVerificationPrecheckEmployer(SdkBaseModel):
    name: OptionalNullable[str] = UNSET
    """The employer's name"""

    tax_id: OptionalNullable[str] = UNSET
    """The employer's tax id"""


class IncomeVerificationPrecheckEmployerDict(TypedDict):
    name: NotRequired[str | None]
    tax_id: NotRequired[str | None]
