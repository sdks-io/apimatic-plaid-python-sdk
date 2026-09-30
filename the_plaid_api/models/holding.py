from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Holding(SdkBaseModel):
    """A securities holding at an institution."""

    account_id: str
    """The Plaid ``account_id`` associated with the holding."""

    security_id: str
    """The Plaid ``security_id`` associated with the holding."""

    institution_price: float
    """The last price given by the institution for this security."""

    institution_price_as_of: Date | None
    """The date at which ``institution_price`` was current."""

    institution_value: float
    """The value of the holding, as reported by the institution."""

    cost_basis: float | None
    """The cost basis of the holding."""

    quantity: float
    """The total quantity of the asset held, as reported by the financial institution. If the security is an option,
    ``quantity`` will reflect the total number of options (typically the number of contracts multiplied by 100), not the
    number of contracts."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the holding. Always ``null`` if ``unofficial_currency_code`` is non-``null``."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the holding. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``iso_currency_code``s."""


class HoldingDict(TypedDict):
    account_id: str
    security_id: str
    institution_price: float
    institution_price_as_of: Date | None
    institution_value: float
    cost_basis: float | None
    quantity: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
