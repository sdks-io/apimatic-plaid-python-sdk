from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .application import Application, ApplicationDict


class ApplicationGetResponse(SdkBaseModel):
    """The request ID associated with this call."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    application: Application
    """Metadata about the application"""


class ApplicationGetResponseDict(TypedDict):
    request_id: str
    application: ApplicationDict
