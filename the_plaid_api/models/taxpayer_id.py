from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TaxpayerId(SdkBaseModel):
    id_type: OptionalNullable[str] = UNSET
    """Type of ID, e.g. 'SSN'"""

    last_4_digits: OptionalNullable[str] = UNSET
    """Last 4 digits of unique number of ID."""


class TaxpayerIdDict(TypedDict):
    id_type: NotRequired[str | None]
    last_4_digits: NotRequired[str | None]
