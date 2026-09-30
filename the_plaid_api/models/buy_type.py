from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BuyType(SdkBaseModel):
    """Buying an investment"""

    assignment: Optional[str] = UNSET
    """Assignment of short option holding"""

    contribution: Optional[str] = UNSET
    """Inflow of assets into a tax-advantaged account"""

    buy: Optional[str] = UNSET
    """Purchase to open or increase a position"""

    buy_to_cover: Optional[str] = Field(default=UNSET, alias="buy to cover")
    """Purchase to close a short position"""

    dividend_reinvestment: Optional[str] = Field(default=UNSET, alias="dividend reinvestment")
    """Purchase using proceeds from a cash dividend"""

    interest_reinvestment: Optional[str] = Field(default=UNSET, alias="interest reinvestment")
    """Purchase using proceeds from a cash interest payment"""

    long_term_capital_gain_reinvestment: Optional[str] = Field(
        default=UNSET, alias="long-term capital gain reinvestment"
    )
    """Purchase using long-term capital gain cash proceeds"""

    short_term_capital_gain_reinvestment: Optional[str] = Field(
        default=UNSET, alias="short-term capital gain reinvestment"
    )
    """Purchase using short-term capital gain cash proceeds"""


class BuyTypeDict(TypedDict):
    assignment: NotRequired[str]
    contribution: NotRequired[str]
    buy: NotRequired[str]
    buy_to_cover: NotRequired[str]
    dividend_reinvestment: NotRequired[str]
    interest_reinvestment: NotRequired[str]
    long_term_capital_gain_reinvestment: NotRequired[str]
    short_term_capital_gain_reinvestment: NotRequired[str]
