from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SignalEvaluateDevice(SdkBaseModel):
    """Details about the end user's device"""

    ip_address: OptionalNullable[str] = UNSET
    """The IP address of the device that initiated the transaction"""

    user_agent: OptionalNullable[str] = UNSET
    """The user agent of the device that initiated the transaction (e.g. "Mozilla/5.0")"""


class SignalEvaluateDeviceDict(TypedDict):
    ip_address: NotRequired[str | None]
    user_agent: NotRequired[str | None]
