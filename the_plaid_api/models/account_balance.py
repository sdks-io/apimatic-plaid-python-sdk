from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class AccountBalance(SdkBaseModel):
    """A set of fields describing the balance for an account. Balance information may be cached unless the balance
    object was returned by ``/accounts/balance/get``."""

    available: float | None
    """The amount of funds available to be withdrawn from the account, as determined by the financial institution.

    For ``credit``-type accounts, the ``available`` balance typically equals the ``limit`` less the ``current`` balance,
    less any pending outflows plus any pending inflows.

    For ``depository``-type accounts, the ``available`` balance typically equals the ``current`` balance less any
    pending outflows plus any pending inflows. For ``depository``-type accounts, the ``available`` balance does not
    include the overdraft limit.

    For ``investment``-type accounts, the ``available`` balance is the total cash available to withdraw as presented by
    the institution.

    Note that not all institutions calculate the ``available`` balance. In the event that ``available`` balance is
    unavailable, Plaid will return an ``available`` balance value of ``null``.

    Available balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by
    ``/accounts/balance/get``.

    If ``current`` is ``null`` this field is guaranteed not to be ``null``."""

    current: float | None
    """The total amount of funds in or owed by the account.

    For ``credit``-type accounts, a positive balance indicates the amount owed; a negative amount indicates the lender
    owing the account holder.

    For ``loan``-type accounts, the current balance is the principal remaining on the loan, except in the case of
    student loan accounts at Sallie Mae (``ins_116944``). For Sallie Mae student loans, the account's balance includes
    both principal and any outstanding interest.

    For ``investment``-type accounts, the current balance is the total value of assets as presented by the institution.

    Note that balance information may be cached unless the value was returned by ``/accounts/balance/get``; if the Item
    is enabled for Transactions, the balance will be at least as recent as the most recent Transaction update. If you
    require realtime balance information, use the ``available`` balance as provided by ``/accounts/balance/get``.

    When returned by ``/accounts/balance/get``, this field may be ``null``. When this happens, ``available`` is
    guaranteed not to be ``null``."""

    limit: float | None
    """For ``credit``-type accounts, this represents the credit limit.

    For ``depository``-type accounts, this represents the pre-arranged overdraft limit, which is common for current
    (checking) accounts in Europe.

    In North America, this field is typically only available for ``credit``-type accounts."""

    iso_currency_code: str | None
    """The ISO-4217 currency code of the balance. Always null if ``unofficial_currency_code`` is non-null."""

    unofficial_currency_code: str | None
    """The unofficial currency code associated with the balance. Always null if ``iso_currency_code`` is non-null.
    Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as
    cryptocurrencies and the currencies of certain countries.

    See the `currency code schema <https://plaid.com/docs/api/accounts#currency-code-schema>`__ for a full listing of
    supported ``unofficial_currency_code``s."""

    last_updated_datetime: OptionalNullable[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    last time that the balance for the given account has been updated

    This is currently only provided when the ``min_last_updated_datetime`` is passed when calling
    ``/accounts/balance/get`` for ``ins_128026`` (Capital One)."""


class AccountBalanceDict(TypedDict):
    available: float | None
    current: float | None
    limit: float | None
    iso_currency_code: str | None
    unofficial_currency_code: str | None
    last_updated_datetime: NotRequired[RFC3339DateTime | None]
