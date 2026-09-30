from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.payment_channel import PaymentChannelOrStr
from .enums.transaction_code import TransactionCodeOrStr
from .enums.transaction_type import TransactionTypeOrStr
from .payment_meta import PaymentMeta, PaymentMetaDict
from .personal_finance_category2 import PersonalFinanceCategory2, PersonalFinanceCategory2Dict
from .transaction_location import TransactionLocation, TransactionLocationDict


class Transaction(SdkBaseModel):
    """A representation of a transaction"""

    transaction_type: Optional[TransactionTypeOrStr] = UNSET
    """Please use the ``payment_channel`` field, ``transaction_type`` will be deprecated in the future.

    ``digital:`` transactions that took place online.

    ``place:`` transactions that were made at a physical location.

    ``special:`` transactions that relate to banks, e.g. fees or deposits.

    ``unresolved:`` transactions that do not fit into the other three types."""

    pending_transaction_id: str | None
    """The ID of a posted transaction's associated pending transaction, where applicable."""

    category_id: str | None
    """The ID of the category to which this transaction belongs. See `Categories
    <https://plaid.com/docs/#category-overview>`__.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    category: list[str | None]
    """A hierarchical array of the categories to which this transaction belongs. See `Categories
    <https://plaid.com/docs/#category-overview>`__.

    If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/`` or
    ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    location: TransactionLocation
    """A representation of where a transaction took place"""

    payment_meta: PaymentMeta
    """Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all
    fields will be ``null``.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/get``, the
    ``payment_meta`` key will always appear, but no data elements are guaranteed. If the ``transactions`` object was
    returned by an Assets endpoint such as ``/asset_report/get/`` or ``/asset_report/pdf/get``, this field will only
    appear in an Asset Report with Insights."""

    account_owner: str | None
    """The name of the account owner. This field is not typically populated and only relevant when dealing with
    sub-accounts."""

    name: str
    """The merchant name or transaction description.

    If the ``transactions`` object was returned by a Transactions endpoint such as ``/transactions/get``, this field
    will always appear. If the ``transactions`` object was returned by an Assets endpoint such as ``/asset_report/get/``
    or ``/asset_report/pdf/get``, this field will only appear in an Asset Report with Insights."""

    original_description: OptionalNullable[str] = UNSET
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

    payment_channel: PaymentChannelOrStr
    """The channel used to make a payment. ``online:`` transactions that took place online.

    ``in store:`` transactions that were made at a physical location.

    ``other:`` transactions that relate to banks, e.g. fees or deposits.

    This field replaces the ``transaction_type`` field."""

    merchant_name: str | None
    """The merchant name, as extracted by Plaid from the ``name`` field."""

    authorized_date: Date | None
    """The date that the transaction was authorized. Dates are returned in an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format ( ``YYYY-MM-DD`` )."""

    authorized_datetime: RFC3339DateTime | None
    """Date and time when a transaction was authorized in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` ).

    This field is only populated for UK institutions. For institutions in other countries, will be ``null``."""

    datetime: RFC3339DateTime | None
    """Date and time when a transaction was posted in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (
    ``YYYY-MM-DDTHH:mm:ssZ`` ).

    This field is only populated for UK institutions. For institutions in other countries, will be ``null``."""

    check_number: str | None
    """The check number of the transaction. This field is only populated for check transactions."""

    transaction_code: TransactionCodeOrStr
    """An identifier classifying the transaction type.

    This field is only populated for European institutions. For institutions in the US and Canada, this field is set to
    ``null``.

    ``adjustment:`` Bank adjustment

    ``atm:`` Cash deposit or withdrawal via an automated teller machine

    ``bank charge:`` Charge or fee levied by the institution

    ``bill payment``: Payment of a bill

    ``cash:`` Cash deposit or withdrawal

    ``cashback:`` Cash withdrawal while making a debit card purchase

    ``cheque:`` Document ordering the payment of money to another person or organization

    ``direct debit:`` Automatic withdrawal of funds initiated by a third party at a regular interval

    ``interest:`` Interest earned or incurred

    ``purchase:`` Purchase made with a debit or credit card

    ``standing order:`` Payment instructed by the account holder to a third party at a regular interval

    ``transfer:`` Transfer of money between accounts"""

    personal_finance_category: Optional[PersonalFinanceCategory2] = UNSET


class TransactionDict(TypedDict):
    transaction_type: NotRequired[TransactionTypeOrStr]
    pending_transaction_id: str | None
    category_id: str | None
    category: list[str | None]
    location: TransactionLocationDict
    payment_meta: PaymentMetaDict
    account_owner: str | None
    name: str
    original_description: NotRequired[str | None]
    account_id: str
    amount: float
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    date: Date
    pending: bool
    transaction_id: str
    payment_channel: PaymentChannelOrStr
    merchant_name: str | None
    authorized_date: Date | None
    authorized_datetime: RFC3339DateTime | None
    datetime: RFC3339DateTime | None
    check_number: str | None
    transaction_code: TransactionCodeOrStr
    personal_finance_category: NotRequired[PersonalFinanceCategory2Dict]
