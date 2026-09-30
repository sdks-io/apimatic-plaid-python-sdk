from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferType(SdkBaseModel):
    """Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""

    assignment: Optional[str] = UNSET
    """Assignment of short option holding"""

    adjustment: Optional[str] = UNSET
    """Increase or decrease in quantity of item"""

    exercise: Optional[str] = UNSET
    """Exercise of an option or warrant contract"""

    expire: Optional[str] = UNSET
    """Expiration of an option or warrant contract"""

    merger: Optional[str] = UNSET
    """Stock exchanged at a pre-defined ratio as part of a merger between companies"""

    spin_off: Optional[str] = Field(default=UNSET, alias="spin off")
    """Inflow of stock from spin-off transaction of an existing holding"""

    split: Optional[str] = UNSET
    """Inflow of stock from a forward split of an existing holding"""

    transfer: Optional[str] = UNSET
    """Movement of assets into or out of an account"""


class TransferTypeDict(TypedDict):
    assignment: NotRequired[str]
    adjustment: NotRequired[str]
    exercise: NotRequired[str]
    expire: NotRequired[str]
    merger: NotRequired[str]
    spin_off: NotRequired[str]
    split: NotRequired[str]
    transfer: NotRequired[str]
