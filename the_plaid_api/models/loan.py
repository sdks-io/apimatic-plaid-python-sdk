from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.account_subtype import AccountSubtypeOrStr


class Loan(SdkBaseModel):
    """A filter to apply to ``loan``-type accounts"""

    account_subtypes: Optional[list[AccountSubtypeOrStr]] = UNSET
    """An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full
    list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#accounts-schema>`__."""


class LoanDict(TypedDict):
    account_subtypes: NotRequired[list[AccountSubtypeOrStr]]
