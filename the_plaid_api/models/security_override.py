from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SecurityOverride(SdkBaseModel):
    """Specify the security associated with the holding or investment transaction. When inputting custom security data
    to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the
    data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a
    security identifier (``ticker_symbol``, ``cusip``, ``isin``, or ``sedol``) are required."""

    isin: Optional[str] = UNSET
    """12-character ISIN, a globally unique securities identifier."""

    cusip: Optional[str] = UNSET
    """9-character CUSIP, an identifier assigned to North American securities."""

    sedol: Optional[str] = UNSET
    """7-character SEDOL, an identifier assigned to securities in the UK."""

    name: Optional[str] = UNSET
    """A descriptive name for the security, suitable for display."""

    ticker_symbol: Optional[str] = UNSET
    """The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available."""

    currency: Optional[str] = UNSET
    """Either a valid ``iso_currency_code`` or ``unofficial_currency_code``"""


class SecurityOverrideDict(TypedDict):
    isin: NotRequired[str]
    cusip: NotRequired[str]
    sedol: NotRequired[str]
    name: NotRequired[str]
    ticker_symbol: NotRequired[str]
    currency: NotRequired[str]
