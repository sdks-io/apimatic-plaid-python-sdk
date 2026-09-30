from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Numbers(SdkBaseModel):
    """Account and bank identifier number data used to configure the test account. All values are optional."""

    account: Optional[str] = UNSET
    """Will be used for the account number."""

    ach_routing: Optional[str] = UNSET
    """Must be a valid ACH routing number."""

    ach_wire_routing: Optional[str] = UNSET
    """Must be a valid wire transfer routing number."""

    eft_institution: Optional[str] = UNSET
    """EFT institution number. Must be specified alongside ``eft_branch``."""

    eft_branch: Optional[str] = UNSET
    """EFT branch number. Must be specified alongside ``eft_institution``."""

    international_bic: Optional[str] = UNSET
    """Bank identifier code (BIC). Must be specified alongside ``international_iban``."""

    international_iban: Optional[str] = UNSET
    """International bank account number (IBAN). If no account number is specified via ``account``, will also be used as
    the account number by default. Must be specified alongside ``international_bic``."""

    bacs_sort_code: Optional[str] = UNSET
    """BACS sort code"""


class NumbersDict(TypedDict):
    account: NotRequired[str]
    ach_routing: NotRequired[str]
    ach_wire_routing: NotRequired[str]
    eft_institution: NotRequired[str]
    eft_branch: NotRequired[str]
    international_bic: NotRequired[str]
    international_iban: NotRequired[str]
    bacs_sort_code: NotRequired[str]
