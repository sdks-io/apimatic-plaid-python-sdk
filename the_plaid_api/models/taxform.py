from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .w2 import W2, W2Dict


class Taxform(SdkBaseModel):
    document_type: str
    """The type of tax document."""

    w2: Optional[W2] = UNSET
    """W2 is an object that represents income data taken from a W2 tax document."""


class TaxformDict(TypedDict):
    document_type: str
    w2: NotRequired[W2Dict]
