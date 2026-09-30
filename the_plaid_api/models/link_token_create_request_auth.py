from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkTokenCreateRequestAuth(SdkBaseModel):
    """Specifies options for initializing Link for use with the Auth product. This field is currently only required if
    using the Flexible Auth product (currently in closed beta)."""

    flow_type: str
    """The optional Auth flow to use. Currently only used to enable Flexible Auth."""


class LinkTokenCreateRequestAuthDict(TypedDict):
    flow_type: str
