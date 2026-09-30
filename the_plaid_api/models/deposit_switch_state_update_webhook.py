from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DepositSwitchStateUpdateWebhook(SdkBaseModel):
    """Fired when the status of a deposit switch request has changed."""

    webhook_type: Optional[str] = UNSET
    """``"DEPOSIT_SWITCH"``"""

    webhook_code: Optional[str] = UNSET
    """``"SWITCH_STATE_UPDATE"``"""

    state: Optional[str] = UNSET
    """The state, or status, of the deposit switch.

    ``initialized``: The deposit switch has been initialized with the user entering the information required to submit
    the deposit switch request.

    ``processing``: The deposit switch request has been submitted and is being processed.

    ``completed``: The user's employer has fulfilled and completed the deposit switch request.

    ``error``: There was an error processing the deposit switch request.

    For more information, see the `Deposit Switch API reference </docs/api/products#deposit_switchget>`__."""

    deposit_switch_id: Optional[str] = UNSET
    """The ID of the deposit switch."""


class DepositSwitchStateUpdateWebhookDict(TypedDict):
    webhook_type: NotRequired[str]
    webhook_code: NotRequired[str]
    state: NotRequired[str]
    deposit_switch_id: NotRequired[str]
