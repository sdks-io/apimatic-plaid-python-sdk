from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .bank_transfer_sweep_account import BankTransferSweepAccount, BankTransferSweepAccountDict


class BankTransferSweep(SdkBaseModel):
    """BankTransferSweep describes a sweep transfer."""

    id: int
    """Identifier of the sweep."""

    transfer_id: str | None
    """Identifier of the sweep transfer."""

    created_at: RFC3339DateTime
    """The datetime when the sweep occurred, in RFC 3339 format."""

    amount: str
    """The amount of the sweep."""

    iso_currency_code: str
    """The currency of the sweep, e.g. "USD"."""

    sweep_account: BankTransferSweepAccount
    """The account where the funds are swept to."""


class BankTransferSweepDict(TypedDict):
    id: int
    transfer_id: str | None
    created_at: RFC3339DateTime
    amount: str
    iso_currency_code: str
    sweep_account: BankTransferSweepAccountDict
