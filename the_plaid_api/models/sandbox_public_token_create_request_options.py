from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sandbox_public_token_create_request_options_transactions import (
    SandboxPublicTokenCreateRequestOptionsTransactions,
    SandboxPublicTokenCreateRequestOptionsTransactionsDict,
)


class SandboxPublicTokenCreateRequestOptions(SdkBaseModel):
    """An optional set of options to be used when configuring the Item. If specified, must not be ``null``."""

    webhook: Optional[str] = UNSET
    """Specify a webhook to associate with the new Item."""

    override_username: str | None = "user_good"
    """Test username to use for the creation of the Sandbox Item. Default value is ``user_good``."""

    override_password: str | None = "pass_good"
    """Test password to use for the creation of the Sandbox Item. Default value is ``pass_good``."""

    transactions: Optional[SandboxPublicTokenCreateRequestOptionsTransactions] = UNSET
    """SandboxPublicTokenCreateRequestOptionsTransactions is an optional set of parameters corresponding to transactions
    options."""


class SandboxPublicTokenCreateRequestOptionsDict(TypedDict):
    webhook: NotRequired[str]
    override_username: NotRequired[str | None]
    override_password: NotRequired[str | None]
    transactions: NotRequired[SandboxPublicTokenCreateRequestOptionsTransactionsDict]
