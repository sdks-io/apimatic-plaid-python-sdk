from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class SandboxPublicTokenCreateRequestOptionsTransactions(SdkBaseModel):
    """SandboxPublicTokenCreateRequestOptionsTransactions is an optional set of parameters corresponding to transactions
    options."""

    start_date: Optional[Date] = UNSET
    """The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""

    end_date: Optional[Date] = UNSET
    """The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD."""


class SandboxPublicTokenCreateRequestOptionsTransactionsDict(TypedDict):
    start_date: NotRequired[Date]
    end_date: NotRequired[Date]
