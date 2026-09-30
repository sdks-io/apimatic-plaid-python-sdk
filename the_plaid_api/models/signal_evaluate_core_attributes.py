from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class SignalEvaluateCoreAttributes(SdkBaseModel):
    """The core attributes object contains additional data that can be used to assess the ACH return risk, such as past
    ACH return events, balance/transaction history, the Item’s connection history in the Plaid network, and identity
    change history."""

    unauthorized_transactions_count_7d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 7 days from the account that will be debited."""

    unauthorized_transactions_count_30d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 30 days from the account that will be debited."""

    unauthorized_transactions_count_60d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 60 days from the account that will be debited."""

    unauthorized_transactions_count_90d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    unauthorized transactions over the past 90 days from the account that will be debited."""

    nsf_overdraft_transactions_count_7d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 7 days from the account that will be debited."""

    nsf_overdraft_transactions_count_30d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 30 days from the account that will be debited."""

    nsf_overdraft_transactions_count_60d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 60 days from the account that will be debited."""

    nsf_overdraft_transactions_count_90d: Optional[int] = UNSET
    """We parse and analyze historical transaction metadata to identify the number of possible past returns due to
    non-sufficient funds/overdrafts over the past 90 days from the account that will be debited."""

    days_since_first_plaid_connection: OptionalNullable[int] = UNSET
    """The number of days since the first time the Item was connected to an application via Plaid"""

    plaid_connections_count_7d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 7 days"""

    plaid_connections_count_30d: OptionalNullable[int] = UNSET
    """The number of times the Item has been connected to applications via Plaid over the past 30 days"""

    total_plaid_connections_count: OptionalNullable[int] = UNSET
    """The total number of times the Item has been connected to applications via Plaid"""

    is_savings_or_money_market_account: Optional[bool] = UNSET
    """Indicates if the ACH transaction funding account is a savings/money market account"""

    total_credit_transactions_amount_10d: Optional[float] = UNSET
    """The total credit (inflow) transaction amount over the past 10 days from the account that will be debited"""

    total_debit_transactions_amount_10d: Optional[float] = UNSET
    """The total debit (outflow) transaction amount over the past 10 days from the account that will be debited"""

    p50_credit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p50_debit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p95_credit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    p95_debit_transactions_amount_28d: OptionalNullable[float] = UNSET
    """The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will
    be debited"""

    days_with_negative_balance_count_90d: OptionalNullable[int] = UNSET
    """The number of days within the past 90 days when the account that will be debited had a negative end-of-day
    available balance"""

    p90_eod_balance_30d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be
    debited"""

    p90_eod_balance_60d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be
    debited"""

    p90_eod_balance_90d: OptionalNullable[float] = UNSET
    """The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be
    debited"""

    p10_eod_balance_30d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be
    debited"""

    p10_eod_balance_60d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be
    debited"""

    p10_eod_balance_90d: OptionalNullable[float] = UNSET
    """The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be
    debited"""

    available_balance: OptionalNullable[float] = UNSET
    """Available balance, as of the ``balance_last_updated`` time. The available balance is the current balance less any
    outstanding holds or debits that have not yet posted to the account."""

    current_balance: OptionalNullable[float] = UNSET
    """Current balance, as of the ``balance_last_updated`` time. The current balance is the total amount of funds in the
    account."""

    balance_last_updated: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DDTHH:mm:ssZ) indicating the last
    time that the balance for the given account has been updated."""

    phone_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 28 days"""

    phone_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's phone numbers on file have changed over the past 90 days"""

    email_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 28 days"""

    email_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's email addresses on file have changed over the past 90 days"""

    address_change_count_28d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 28 days"""

    address_change_count_90d: OptionalNullable[int] = UNSET
    """The number of times the account's addresses on file have changed over the past 90 days"""


class SignalEvaluateCoreAttributesDict(TypedDict):
    unauthorized_transactions_count_7d: NotRequired[int]
    unauthorized_transactions_count_30d: NotRequired[int]
    unauthorized_transactions_count_60d: NotRequired[int]
    unauthorized_transactions_count_90d: NotRequired[int]
    nsf_overdraft_transactions_count_7d: NotRequired[int]
    nsf_overdraft_transactions_count_30d: NotRequired[int]
    nsf_overdraft_transactions_count_60d: NotRequired[int]
    nsf_overdraft_transactions_count_90d: NotRequired[int]
    days_since_first_plaid_connection: NotRequired[int | None]
    plaid_connections_count_7d: NotRequired[int | None]
    plaid_connections_count_30d: NotRequired[int | None]
    total_plaid_connections_count: NotRequired[int | None]
    is_savings_or_money_market_account: NotRequired[bool]
    total_credit_transactions_amount_10d: NotRequired[float]
    total_debit_transactions_amount_10d: NotRequired[float]
    p50_credit_transactions_amount_28d: NotRequired[float | None]
    p50_debit_transactions_amount_28d: NotRequired[float | None]
    p95_credit_transactions_amount_28d: NotRequired[float | None]
    p95_debit_transactions_amount_28d: NotRequired[float | None]
    days_with_negative_balance_count_90d: NotRequired[int | None]
    p90_eod_balance_30d: NotRequired[float | None]
    p90_eod_balance_60d: NotRequired[float | None]
    p90_eod_balance_90d: NotRequired[float | None]
    p10_eod_balance_30d: NotRequired[float | None]
    p10_eod_balance_60d: NotRequired[float | None]
    p10_eod_balance_90d: NotRequired[float | None]
    available_balance: NotRequired[float | None]
    current_balance: NotRequired[float | None]
    balance_last_updated: NotRequired[RFC3339DateTime | None]
    phone_change_count_28d: NotRequired[int | None]
    phone_change_count_90d: NotRequired[int | None]
    email_change_count_28d: NotRequired[int | None]
    email_change_count_90d: NotRequired[int | None]
    address_change_count_28d: NotRequired[int | None]
    address_change_count_90d: NotRequired[int | None]
