from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr
from .sandbox_public_token_create_request_options import (
    SandboxPublicTokenCreateRequestOptions,
    SandboxPublicTokenCreateRequestOptionsDict,
)


class SandboxPublicTokenCreateRequest(SdkBaseModel):
    """SandboxPublicTokenCreateRequest defines the request schema for ``/sandbox/public_token/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    institution_id: str
    """The ID of the institution the Item will be associated with"""

    initial_products: list[ProductsOrStr]
    """The products to initially pull for the Item. May be any products that the specified ``institution_id`` supports.
    This array may not be empty."""

    options: Optional[SandboxPublicTokenCreateRequestOptions] = UNSET
    """An optional set of options to be used when configuring the Item. If specified, must not be ``null``."""


class SandboxPublicTokenCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    institution_id: str
    initial_products: list[ProductsOrStr]
    options: NotRequired[SandboxPublicTokenCreateRequestOptionsDict]
