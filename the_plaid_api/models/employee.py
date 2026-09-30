from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address2 import Address2, Address2Dict
from .taxpayer_id import TaxpayerId, TaxpayerIdDict


class Employee(SdkBaseModel):
    """Data about the employee."""

    name: str | None
    """The name of the employee."""

    address: Address2
    marital_status: OptionalNullable[str] = UNSET
    """Marital status of the employee."""

    taxpayer_id: Optional[TaxpayerId] = UNSET


class EmployeeDict(TypedDict):
    name: str | None
    address: Address2Dict
    marital_status: NotRequired[str | None]
    taxpayer_id: NotRequired[TaxpayerIdDict]
