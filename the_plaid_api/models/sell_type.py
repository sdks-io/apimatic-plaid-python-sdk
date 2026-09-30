from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellType(SdkBaseModel):
    """Selling an investment"""

    distribution: Optional[str] = UNSET
    """Outflow of assets from a tax-advantaged account"""

    exercise: Optional[str] = UNSET
    """Exercise of an option or warrant contract"""

    sell: Optional[str] = UNSET
    """Sell to close or decrease an existing holding"""

    sell_short: Optional[str] = Field(default=UNSET, alias="sell short")
    """Sell to open a short position"""


class SellTypeDict(TypedDict):
    distribution: NotRequired[str]
    exercise: NotRequired[str]
    sell: NotRequired[str]
    sell_short: NotRequired[str]
