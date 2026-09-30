from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Jwtheader(SdkBaseModel):
    """A JWT Header, used for webhook validation"""

    id: str


class JwtheaderDict(TypedDict):
    id: str
