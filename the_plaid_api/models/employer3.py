from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Employer3(SdkBaseModel):
    """The employer on the paystub."""

    name: Optional[str] = UNSET
    """The name of the employer."""


class Employer3Dict(TypedDict):
    name: NotRequired[str]
