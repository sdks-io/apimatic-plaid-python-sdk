from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentsTransactionsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/investments/transactions/get`` results. If provided, must be non-``null``."""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids`` to retrieve for the Item."""

    count: int = 100
    """The number of transactions to fetch."""

    offset: int = 0
    """The number of transactions to skip when fetching transaction history"""


class InvestmentsTransactionsGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
    count: NotRequired[int]
    offset: NotRequired[int]
