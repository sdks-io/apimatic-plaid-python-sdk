from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxItemFireWebhookRequest(SdkBaseModel):
    """SandboxItemFireWebhookRequest defines the request schema for ``/sandbox/item/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item data is being requested for."""

    webhook_code: str
    """The following values for ``webhook_code`` are supported:

    * ``DEFAULT_UPDATE``"""


class SandboxItemFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    webhook_code: str
