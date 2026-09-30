from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .distribution_details import DistributionDetails, DistributionDetailsDict
from .total import Total, TotalDict


class NetPay(SdkBaseModel):
    """An object representing information about the net pay amount on the paystub."""

    distribution_details: Optional[list[DistributionDetails]] = UNSET
    total: Optional[Total] = UNSET
    """An object representing both the current pay period and year to date amount for a category."""


class NetPayDict(TypedDict):
    distribution_details: NotRequired[list[DistributionDetailsDict]]
    total: NotRequired[TotalDict]
