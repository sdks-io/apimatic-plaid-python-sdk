from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class InitialUpdateWebhook(SdkBaseModel):
    """Fired when an Item's initial transaction pull is completed. Once this webhook has been fired, transaction data
    for the most recent 30 days can be fetched for the Item. If `Account Select v2
    <https://plaid.com/docs/link/customization/#account-select>`__ is enabled, this webhook will also be fired if
    account selections for the Item are updated, with ``num_transactions`` set to the number of net new transactions
    pulled after the account selection update."""

    webhook_type: str
    """``TRANSACTIONS``"""

    webhook_code: str
    """``INITIAL_UPDATE``"""

    error: OptionalNullable[str] = UNSET
    """The error code associated with the webhook."""

    new_transactions: float
    """The number of new, unfetched transactions available."""

    item_id: str
    """The ``item_id`` of the Item associated with this webhook, warning, or error"""


class InitialUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    error: NotRequired[str | None]
    new_transactions: float
    item_id: str
