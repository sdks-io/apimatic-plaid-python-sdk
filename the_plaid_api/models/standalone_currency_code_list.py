from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unofficial_currency_code_list import UnofficialCurrencyCodeList, UnofficialCurrencyCodeListDict


class StandaloneCurrencyCodeList(SdkBaseModel):
    """The following currency codes are supported by Plaid."""

    iso_currency_code: str
    """Plaid supports all ISO 4217 currency codes."""

    unofficial_currency_code: UnofficialCurrencyCodeList
    """List of unofficial currency codes"""


class StandaloneCurrencyCodeListDict(TypedDict):
    iso_currency_code: str
    unofficial_currency_code: UnofficialCurrencyCodeListDict
