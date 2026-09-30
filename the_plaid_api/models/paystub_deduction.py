from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PaystubDeduction(SdkBaseModel):
    type_: str | None = Field(alias="type")
    """The description of the deduction, as provided on the paystub. For example: ``"401(k)"``, ``"FICA MED TAX"``."""

    is_pretax: bool | None
    """``true`` if the deduction is pre-tax; ``false`` otherwise."""

    total: float | None
    """The amount of the deduction."""


class PaystubDeductionDict(TypedDict):
    type_: str | None
    is_pretax: bool | None
    total: float | None
