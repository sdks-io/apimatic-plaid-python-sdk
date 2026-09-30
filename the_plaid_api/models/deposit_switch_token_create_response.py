from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DepositSwitchTokenCreateResponse(SdkBaseModel):
    """DepositSwitchTokenCreateResponse defines the response schema for ``/deposit_switch/token/create``"""

    deposit_switch_token: str
    """Deposit switch token, used to initialize Link for the Deposit Switch product"""

    deposit_switch_token_expiration_time: str
    """Expiration time of the token, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class DepositSwitchTokenCreateResponseDict(TypedDict):
    deposit_switch_token: str
    deposit_switch_token_expiration_time: str
    request_id: str
