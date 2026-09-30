from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_status_investments import ItemStatusInvestments, ItemStatusInvestmentsDict
from .item_status_last_webhook import ItemStatusLastWebhook, ItemStatusLastWebhookDict
from .item_status_transactions import ItemStatusTransactions, ItemStatusTransactionsDict


class ItemStatus(SdkBaseModel):
    """An object with information about the status of the Item."""

    investments: Optional[ItemStatusInvestments] = UNSET
    """Information about the last successful and failed investments update for the Item."""

    transactions: Optional[ItemStatusTransactions] = UNSET
    """Information about the last successful and failed transactions update for the Item."""

    last_webhook: Optional[ItemStatusLastWebhook] = UNSET
    """Information about the last webhook fired for the Item."""


class ItemStatusDict(TypedDict):
    investments: NotRequired[ItemStatusInvestmentsDict]
    transactions: NotRequired[ItemStatusTransactionsDict]
    last_webhook: NotRequired[ItemStatusLastWebhookDict]
