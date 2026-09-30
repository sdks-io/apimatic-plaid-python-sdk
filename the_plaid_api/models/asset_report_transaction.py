from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.transaction_type import TransactionTypeOrStr
from .payment_meta import PaymentMeta, PaymentMetaDict
from .transaction_location import TransactionLocation, TransactionLocationDict


class AssetReportTransaction(SdkBaseModel):
    transaction_type: Optional[TransactionTypeOrStr] = UNSET
    """Please use the ``payment_channel`` field, ``transaction_type`` will be deprecated in the future.

    ``digital:`` transactions that took place online.

    ``place:`` transactions that were made at a physical location.

    ``special:`` transactions that relate to banks, e.g. fees or deposits.

    ``unresolved:`` transactions that do not fit into the other three types."""

    pending_transaction_id: OptionalNullable[str] = UNSET
    """The ID of a posted transaction's associated pending transaction, where applicable."""

    category_id: OptionalNullable[str] = UNSET
    """The ID of the category to which this transaction belongs. See `Categories
    <https://plaid.com/docs/#category-overview>`__.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    category: Optional[list[str | None]] = UNSET
    """A hierarchical array of the categories to which this transaction belongs. See `Categories
    <https://plaid.com/docs/#category-overview>`__.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    location: Optional[TransactionLocation] = UNSET
    """A representation of where a transaction took place"""

    payment_meta: Optional[PaymentMeta] = UNSET
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all
    fields will be ``null``.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/get``, the
    ``payment_meta`` key will always appear, but no data elements are guaranteed. If the ``transactions`` object was
    returned by an Assets endpoint such as ``/asset_report/get/`` or ``/asset_report/pdf/get``, this field will only
    appear in an Asset Report with Insights."""

    account_owner: OptionalNullable[str] = UNSET
    """The name of the account owner. This field is not typically populated and only relevant when dealing with
    sub-accounts."""

    name: Optional[str] = UNSET
    """The merchant name or transaction description.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/get``, this field
    will always appear. If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/``
    or ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    original_description: str | None
    """The string returned by the financial institution to describe the transaction. For transactions returned by
    ``/transactions/get``, this field is in beta and will be omitted unless the client is both enrolled in the closed
    beta program and has set ``options.include_original_description`` to ``true``."""

    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: float
    """The settled value of the transaction, denominated in the account's currency, as stated in ``iso_currency_code``
    or ``unofficial_currency_code``. Positive values when money moves out of the account; negative values when money
    moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are
    negative."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the transaction. Always ``null`` if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the transaction. Always ``null`` if ``iso_currency_code`` is
    non-``null``. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such
    as cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``iso_currency_code``s."""

    date: Date
    """For pending transactions, the date that the transaction occurred; for posted transactions, the date that the
    transaction posted. Both dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DD`` )."""

    pending: bool
    """When ``true``, identifies the transaction as pending or unsettled. Pending transaction details (name, type,
    amount, category ID) may change before they are settled."""

    transaction_id: str
    """The unique ID of the transaction. Like all Plaid identifiers, the ``transaction_id`` is case sensitive."""

    date_transacted: OptionalNullable[str] = UNSET
    """The date on which the transaction took place, in IS0 8601 format."""


class AssetReportTransactionDict(TypedDict):
    transaction_type: NotRequired[TransactionTypeOrStr]
    pending_transaction_id: NotRequired[str | None]
    category_id: NotRequired[str | None]
    category: NotRequired[list[str | None]]
    location: NotRequired[TransactionLocationDict]
    payment_meta: NotRequired[PaymentMetaDict]
    account_owner: NotRequired[str | None]
    name: NotRequired[str]
    original_description: str | None
    account_id: str
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    date: Date
    pending: bool
    transaction_id: str
    date_transacted: NotRequired[str | None]
