from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersAchnullable(SdkBaseModel):
    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The ACH account number for the account.

    Note that when using OAuth with Chase Bank (``ins_56``), Chase will issue "tokenized" routing and account numbers,
    which are not the user's actual account and routing numbers. These tokenized numbers should work identically to
    normal account and routing numbers. The digits returned in the mask field will continue to reflect the actual
    account number, rather than the tokenized account number. If a user revokes their permissions to your app, the
    tokenized numbers will continue to work for ACH deposits, but not withdrawals."""

    routing: str
    """The ACH routing number for the account. If the institution is ``ins_56``, this may be a tokenized routing number.
    For more information, see the description of the ``account`` field."""

    wire_routing: str | None
    """The wire transfer routing number for the account, if available"""


class NumbersAchnullableDict(TypedDict):
    account_id: str
    account: str
    routing: str
    wire_routing: str | None
