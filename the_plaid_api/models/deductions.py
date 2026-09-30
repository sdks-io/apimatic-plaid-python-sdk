from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .total import Total, TotalDict


class Deductions(SdkBaseModel):
    """An object with the deduction information found on a paystub."""

    subtotals: Optional[list[Total]] = UNSET
    totals: Optional[list[Total]] = UNSET


class DeductionsDict(TypedDict):
    subtotals: NotRequired[list[TotalDict]]
    totals: NotRequired[list[TotalDict]]
