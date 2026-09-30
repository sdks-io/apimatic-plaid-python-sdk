from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .link_token_get_metadata_response import LinkTokenGetMetadataResponse, LinkTokenGetMetadataResponseDict


class LinkTokenGetResponse(SdkBaseModel):
    """LinkTokenGetResponse defines the response schema for ``/link/token/get``"""

    link_token: str
    """A ``link_token``, which can be supplied to Link in order to initialize it and receive a ``public_token``, which
    can be exchanged for an ``access_token``."""

    created_at: RFC3339DateTime | None
    """The creation timestamp for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    expiration: RFC3339DateTime | None
    """The expiration timestamp for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    metadata: LinkTokenGetMetadataResponse
    """An object specifying the arguments originally provided to the ``/link/token/create`` call."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LinkTokenGetResponseDict(TypedDict):
    link_token: str
    created_at: RFC3339DateTime | None
    expiration: RFC3339DateTime | None
    metadata: LinkTokenGetMetadataResponseDict
    request_id: str
