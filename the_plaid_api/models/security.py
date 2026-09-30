from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Security(SdkBaseModel):
    """Contains details about a security"""

    security_id: str
    """A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid
    identifiers, the ``security_id`` is case sensitive."""

    isin: str | None
    """12-character ISIN, a globally unique securities identifier."""

    cusip: str | None
    """9-character CUSIP, an identifier assigned to North American securities."""

    sedol: str | None
    """7-character SEDOL, an identifier assigned to securities in the UK."""

    institution_security_id: str | None
    """An identifier given to the security by the institution"""

    institution_id: str | None
    """If ``institution_security_id`` is present, this field indicates the Plaid ``institution_id`` of the institution
    to whom the identifier belongs."""

    proxy_security_id: str | None
    """In certain cases, Plaid will provide the ID of another security whose performance resembles this security,
    typically when the original security has low volume, or when a private security can be modeled with a publicly
    traded security."""

    name: str | None
    """A descriptive name for the security, suitable for display."""

    ticker_symbol: str | None
    """The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available."""

    is_cash_equivalent: bool | None
    """Indicates that a security is a highly liquid asset and can be treated like cash."""

    type_: str | None = Field(alias="type")
    """The security type of the holding. Valid security types are:

    ``cash``: Cash, currency, and money market funds

    ``derivative``: Options, warrants, and other derivative instruments

    ``equity``: Domestic and foreign equities

    ``etf``: Multi-asset exchange-traded investment funds

    ``fixed income``: Bonds and certificates of deposit (CDs)

    ``loan``: Loans and loan receivables.

    ``mutual fund``: Open- and closed-end vehicles pooling funds of multiple investors.

    ``other``: Unknown or other investment types"""

    close_price: float | None
    """Price of the security at the close of the previous trading session. ``null`` for non-public securities. If the
    security is a foreign currency or a cryptocurrency this field will be updated daily and will be priced in USD."""

    close_price_as_of: Date | None
    """Date for which ``close_price`` is accurate. Always ``null`` if ``close_price`` is ``null``."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the price given. Always ``null`` if ``unofficial_currency_code`` is
    non-``null``."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the security. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``iso_currency_code``s."""


class SecurityDict(TypedDict):
    security_id: str
    isin: str | None
    cusip: str | None
    sedol: str | None
    institution_security_id: str | None
    institution_id: str | None
    proxy_security_id: str | None
    name: str | None
    ticker_symbol: str | None
    is_cash_equivalent: bool | None
    type_: str | None
    close_price: float | None
    close_price_as_of: Date | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
