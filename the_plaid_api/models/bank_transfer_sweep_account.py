from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BankTransferSweepAccount(SdkBaseModel):
    """The account where the funds are swept to."""

    account_number: str
    routing_number: str


class BankTransferSweepAccountDict(TypedDict):
    account_number: str
    routing_number: str
