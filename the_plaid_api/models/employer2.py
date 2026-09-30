from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address2 import Address2, Address2Dict


class Employer2(SdkBaseModel):
    name: str | None
    """The name of the employer on the paystub."""

    address: Optional[Address2] = UNSET


class Employer2Dict(TypedDict):
    name: str | None
    address: NotRequired[Address2Dict]
