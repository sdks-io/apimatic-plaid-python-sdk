from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.product_data_type import ProductDataTypeOrStr
from .requested_scopes import RequestedScopes, RequestedScopesDict
from .scopes_nullable import ScopesNullable, ScopesNullableDict


class ConnectedApplication(SdkBaseModel):
    """Describes the connected application for a particular end user."""

    application_id: str
    """This field will map to the application ID that is returned from /item/applications/list, or provided to the
    institution in an oauth redirect."""

    name: str
    """The name of the application"""

    logo: str | None
    """A URL that links to the application logo image (will be deprecated in the future, please use logo_url)."""

    logo_url: str | None
    """A URL that links to the application logo image."""

    application_url: str | None
    """The URL for the application's website"""

    reason_for_access: str | None
    """A string provided by the connected app stating why they use their respective enabled products."""

    created_at: Date
    """The date this application was linked in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format in
    UTC."""

    product_data_types: list[ProductDataTypeOrStr]
    """(Deprecated) A list of enums representing the data collected and products enabled for this connected
    application."""

    scopes: Optional[ScopesNullable] = UNSET
    requested_scopes: Optional[RequestedScopes] = UNSET
    """Scope of required and optional account features or content from a ConnectedApplication."""


class ConnectedApplicationDict(TypedDict):
    application_id: str
    name: str
    logo: str | None
    logo_url: str | None
    application_url: str | None
    reason_for_access: str | None
    created_at: Date
    product_data_types: list[ProductDataTypeOrStr]
    scopes: NotRequired[ScopesNullableDict]
    requested_scopes: NotRequired[RequestedScopesDict]
