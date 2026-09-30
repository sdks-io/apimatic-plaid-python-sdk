from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .enums.subtype import SubtypeOrStr
from .enums.type4 import Type4OrStr


class InvestmentTransaction(SdkBaseModel):
    """A transaction within an investment account."""

    investment_transaction_id: str
    """The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the
    ``investment_transaction_id`` is case sensitive."""

    cancel_transaction_id: OptionalNullable[str] = UNSET
    """A legacy field formerly used internally by Plaid to identify certain canceled transactions."""

    account_id: str
    """The ``account_id`` of the account against which this transaction posted."""

    security_id: str | None
    """The ``security_id`` to which this transaction is related."""

    date: Date
    """The `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ posting date for the transaction, or transacted date for
    pending transactions."""

    name: str
    """The institution’s description of the transaction."""

    quantity: float
    """The number of units of the security involved in this transaction."""

    amount: float
    """The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative
    values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated
    with securities."""

    price: float
    """The price of the security at which this transaction occurred."""

    fees: float | None
    """The combined value of all fees applied to this transaction"""

    type_: Type4OrStr = Field(alias="type")
    """Value is one of the following: ``buy``: Buying an investment ``sell``: Selling an investment ``cancel``: A
    cancellation of a pending transaction ``cash``: Activity that modifies a cash position ``fee``: A fee on the account
    ``transfer``: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio
    transfer

    For descriptions of possible transaction types and subtypes, see the `Investment transaction types schema
    <https://plaid.com/docs/api/accounts/#investment-transaction-types-schema>`__."""

    subtype: SubtypeOrStr
    """For descriptions of possible transaction types and subtypes, see the `Investment transaction types schema
    <https://plaid.com/docs/api/accounts/#investment-transaction-types-schema>`__."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the transaction. Always ``null`` if ``unofficial_currency_code`` is
    non-``null``."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the holding. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``iso_currency_code``s."""


class InvestmentTransactionDict(TypedDict):
    investment_transaction_id: str
    cancel_transaction_id: NotRequired[str | None]
    account_id: str
    security_id: str | None
    date: Date
    name: str
    quantity: float
    amount: float
    price: float
    fees: float | None
    type_: Type4OrStr
    subtype: SubtypeOrStr
    iso_currency_code: str | None
    unofficial_currency_code: str | None
