from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class DepositSwitchCreateRequestOptions(SdkBaseModel):
    """Options to configure the ``/deposit_switch/create`` request. If provided, cannot be ``null``."""

    webhook: OptionalNullable[str] = UNSET
    """The URL registered to receive webhooks when the status of a deposit switch request has changed."""

    transaction_item_access_tokens: Optional[list[str]] = UNSET
    """An array of access tokens corresponding to transaction items to use when attempting to match the user to their
    Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access
    to the transactions product."""


class DepositSwitchCreateRequestOptionsDict(TypedDict):
    webhook: NotRequired[str | None]
    transaction_item_access_tokens: NotRequired[list[str]]
