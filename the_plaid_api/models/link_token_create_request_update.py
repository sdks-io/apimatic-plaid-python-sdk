from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestUpdate(SdkBaseModel):
    """Specifies options for initializing Link for `update mode <https://plaid.com/docs/link/update-mode>`__."""

    account_selection_enabled: bool = False
    """If ``true``, enables `update mode with Account Select
    <https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts>`__."""


class LinkTokenCreateRequestUpdateDict(TypedDict):
    account_selection_enabled: NotRequired[bool]
