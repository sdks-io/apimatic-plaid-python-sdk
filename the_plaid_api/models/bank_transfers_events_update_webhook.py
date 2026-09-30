from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BankTransfersEventsUpdateWebhook(SdkBaseModel):
    """Fired when new bank transfer events are available. Receiving this webhook indicates you should fetch the new
    events from ``/bank_transfer/event/sync``."""

    webhook_type: str
    """``BANK_TRANSFERS``"""

    webhook_code: str
    """``BANK_TRANSFERS_EVENTS_UPDATE``"""


class BankTransfersEventsUpdateWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
