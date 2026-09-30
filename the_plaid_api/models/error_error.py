from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.error_type import ErrorTypeOrStr


class ErrorError(SdkBaseModel):
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    error_type: ErrorTypeOrStr
    """A broad categorization of the error. Safe for programatic use."""

    error_code: str
    """The particular error code. Safe for programmatic use."""

    error_message: str
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic
    use."""

    display_message: str | None
    """A user-friendly representation of the error code. ``null`` if the error is not related to user action.

    This may change over time and is not safe for programmatic use."""

    request_id: Optional[str] = UNSET
    """A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in
    errors provided by webhooks."""

    causes: Optional[list[Any]] = UNSET
    """In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request,
    ``causes`` will return an array of errors containing a breakdown of these errors on the individual Item level, if
    any can be identified.

    ``causes`` will only be provided for the ``error_type`` ``ASSET_REPORT_ERROR``."""

    status: OptionalNullable[float] = UNSET
    """The HTTP status code associated with the error. This will only be returned in the response body when the error
    information is provided via a webhook."""

    documentation_url: Optional[str] = UNSET
    """The URL of a Plaid documentation page with more information about the error"""

    suggested_action: Optional[str] = UNSET
    """Suggested steps for resolving the error"""


class ErrorErrorDict(TypedDict):
    error_type: ErrorTypeOrStr
    error_code: str
    error_message: str
    display_message: str | None
    request_id: NotRequired[str]
    causes: NotRequired[list[Any]]
    status: NotRequired[float | None]
    documentation_url: NotRequired[str]
    suggested_action: NotRequired[str]
