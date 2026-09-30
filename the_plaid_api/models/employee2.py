from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address1 import Address1, Address1Dict


class Employee2(SdkBaseModel):
    """The employee on the paystub."""

    name: Optional[str] = UNSET
    """The name of the employee."""

    address: Optional[Address1] = UNSET
    """The address of the employee."""


class Employee2Dict(TypedDict):
    name: NotRequired[str]
    address: NotRequired[Address1Dict]
