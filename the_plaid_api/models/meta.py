from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Meta(SdkBaseModel):
    """Allows specifying the metadata of the test account"""

    name: str
    """The account's name"""

    official_name: str
    """The account's official name"""

    limit: float
    """The account's limit"""


class MetaDict(TypedDict):
    name: str
    official_name: str
    limit: float
