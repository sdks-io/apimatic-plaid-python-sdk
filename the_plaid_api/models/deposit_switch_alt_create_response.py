from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DepositSwitchAltCreateResponse(SdkBaseModel):
    """DepositSwitchAltCreateResponse defines the response schema for ``/deposit_switch/alt/create``"""

    deposit_switch_id: str
    """ID of the deposit switch. This ID is persisted throughout the lifetime of the deposit switch."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class DepositSwitchAltCreateResponseDict(TypedDict):
    deposit_switch_id: str
    request_id: str
