from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class NumbersBacsnullable(SdkBaseModel):
    account_id: str
    """The Plaid account ID associated with the account numbers"""

    account: str
    """The BACS account number for the account"""

    sort_code: str
    """The BACS sort code for the account"""


class NumbersBacsnullableDict(TypedDict):
    account_id: str
    account: str
    sort_code: str
