from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Application(SdkBaseModel):
    """Metadata about the application"""

    application_id: str
    """This field will map to the application ID that is returned from /item/applications/list, or provided to the
    institution in an oauth redirect."""

    name: str
    """The name of the application"""

    created_at: Date
    """The date this application was linked in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format in
    UTC."""

    logo_url: str | None
    """A URL that links to the application logo image."""

    application_url: str | None
    """The URL for the application's website"""

    reason_for_access: str | None
    """A string provided by the connected app stating why they use their respective enabled products."""


class ApplicationDict(TypedDict):
    application_id: str
    name: str
    created_at: Date
    logo_url: str | None
    application_url: str | None
    reason_for_access: str | None
