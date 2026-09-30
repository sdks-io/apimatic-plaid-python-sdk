from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_balance import AccountBalance, AccountBalanceDict
from .enums.account_subtype import AccountSubtypeOrStr
from .enums.account_type import AccountTypeOrStr
from .enums.verification_status4 import VerificationStatus4OrStr
from .owner import Owner, OwnerDict


class AccountIdentity(SdkBaseModel):
    account_id: str
    """Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account
    with the data returned by the financial institution. This may occur, for example, when the name of the account
    changes. If this happens a new ``account_id`` will be assigned to the account.

    The ``account_id`` can also change if the ``access_token`` is deleted and the same credentials that were used to
    generate that ``access_token`` are used to generate a new ``access_token`` on a later date. In that case, the new
    ``account_id`` will be different from the old ``account_id``.

    If an account with a specific ``account_id`` disappears instead of changing, the account is likely closed. Closed
    accounts are not returned by the Plaid API.

    Like all Plaid identifiers, the ``account_id`` is case sensitive."""

    balances: AccountBalance
    """A set of fields describing the balance for an account. Balance information may be cached unless the balance
    object was returned by ``/accounts/balance/get``."""

    mask: str | None
    """The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be
    non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user."""

    name: str
    """The name of the account, either assigned by the user or by the financial institution itself"""

    official_name: str | None
    """The official name of the account as given by the financial institution"""

    type_: AccountTypeOrStr = Field(alias="type")
    """``investment:`` Investment account

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``brokerage``: An investment account. Used for ``/assets/`` endpoints only; other endpoints use ``investment``.

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    subtype: AccountSubtypeOrStr
    """See the `Account type schema <https://plaid.com/docs/api/accounts/#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    verification_status: Optional[VerificationStatus4OrStr] = UNSET
    """The current verification status of an Auth Item initiated through Automated or Manual micro-deposits. Returned
    for Auth Items only.

    ``pending_automatic_verification``: The Item is pending automatic verification

    ``pending_manual_verification``: The Item is pending manual micro-deposit verification. Items remain in this state
    until the user successfully verifies the two amounts.

    ``automatically_verified``: The Item has successfully been automatically verified

    ``manually_verified``: The Item has successfully been manually verified

    ``verification_expired``: Plaid was unable to automatically verify the deposit within 7 calendar days and will no
    longer attempt to validate the Item. Users may retry by submitting their information again through Link.

    ``verification_failed``: The Item failed manual micro-deposit verification because the user exhausted all 3
    verification attempts. Users may retry by submitting their information again through Link."""

    owners: list[Owner]
    """Data returned by the financial institution about the account owner or owners. Only returned by Identity or Assets
    endpoints. Multiple owners on a single account will be represented in the same ``owner`` object, not in multiple
    owner objects within the array."""


class AccountIdentityDict(TypedDict):
    account_id: str
    balances: AccountBalanceDict
    mask: str | None
    name: str
    official_name: str | None
    type_: AccountTypeOrStr
    subtype: AccountSubtypeOrStr
    verification_status: NotRequired[VerificationStatus4OrStr]
    owners: list[OwnerDict]
