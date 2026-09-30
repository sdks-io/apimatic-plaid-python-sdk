from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class LinkTokenCreateResponse(SdkBaseModel):
    """LinkTokenCreateResponse defines the response schema for ``/link/token/create``"""

    link_token: str
    """A ``link_token``, which can be supplied to Link in order to initialize it and receive a ``public_token``, which
    can be exchanged for an ``access_token``."""

    expiration: RFC3339DateTime
    """The expiration date for the ``link_token``, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format. A
    ``link_token`` created to generate a ``public_token`` that will be exchanged for a new ``access_token`` expires
    after 4 hours. A ``link_token`` created for an existing Item (such as when updating an existing ``access_token`` by
    launching Link in update mode) expires after 30 minutes."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LinkTokenCreateResponseDict(TypedDict):
    link_token: str
    expiration: RFC3339DateTime
    request_id: str
