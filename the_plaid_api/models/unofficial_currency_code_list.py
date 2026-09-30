from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UnofficialCurrencyCodeList(SdkBaseModel):
    """List of unofficial currency codes"""

    ada: str = Field(alias="ADA")
    """Cardano"""

    bat: str = Field(alias="BAT")
    """Basic Attention Token"""

    bch: str = Field(alias="BCH")
    """Bitcoin Cash"""

    bnb: str = Field(alias="BNB")
    """Binance Coin"""

    btc: str = Field(alias="BTC")
    """Bitcoin"""

    btg: str = Field(alias="BTG")
    """Bitcoin Gold"""

    cnh: str = Field(alias="CNH")
    """Chinese Yuan (offshore)"""

    dash: str = Field(alias="DASH")
    """Dash"""

    doge: str = Field(alias="DOGE")
    """Dogecoin"""

    etc: str = Field(alias="ETC")
    """Ethereum Classic"""

    eth: str = Field(alias="ETH")
    """Ethereum"""

    gbx: str = Field(alias="GBX")
    """Pence sterling, i.e. British penny"""

    lsk: str = Field(alias="LSK")
    """Lisk"""

    neo: str = Field(alias="NEO")
    """Neo"""

    omg: str = Field(alias="OMG")
    """OmiseGO"""

    qtum: str = Field(alias="QTUM")
    """Qtum"""

    usdt: str = Field(alias="USDT")
    """TehterUS"""

    xlm: str = Field(alias="XLM")
    """Stellar Lumen"""

    xmr: str = Field(alias="XMR")
    """Monero"""

    xrp: str = Field(alias="XRP")
    """Ripple"""

    zec: str = Field(alias="ZEC")
    """Zcash"""

    zrx: str = Field(alias="ZRX")
    """0x"""


class UnofficialCurrencyCodeListDict(TypedDict):
    ada: str
    bat: str
    bch: str
    bnb: str
    btc: str
    btg: str
    cnh: str
    dash: str
    doge: str
    etc: str
    eth: str
    gbx: str
    lsk: str
    neo: str
    omg: str
    qtum: str
    usdt: str
    xlm: str
    xmr: str
    xrp: str
    zec: str
    zrx: str
