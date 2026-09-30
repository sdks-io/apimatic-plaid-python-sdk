from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DocumentMetadata(SdkBaseModel):
    """An object representing metadata from the end user's uploaded document."""

    name: Optional[str] = UNSET
    """The name of the document."""

    status: Optional[str] = UNSET
    """The processing status of the document."""

    doc_id: Optional[str] = UNSET
    """An identifier of the document that is also present in the paystub response."""


class DocumentMetadataDict(TypedDict):
    name: NotRequired[str]
    status: NotRequired[str]
    doc_id: NotRequired[str]
