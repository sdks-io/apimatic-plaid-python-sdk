from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .numbers_achnullable import NumbersAchnullable, NumbersAchnullableDict
from .numbers_bacsnullable import NumbersBacsnullable, NumbersBacsnullableDict
from .numbers_eftnullable import NumbersEftnullable, NumbersEftnullableDict
from .numbers_international_nullable import NumbersInternationalNullable, NumbersInternationalNullableDict


class ProcessorNumber(SdkBaseModel):
    """An object containing identifying numbers used for making electronic transfers to and from the ``account``. The
    identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by the ``account`` for which
    auth data has been requested, a null value will be returned."""

    ach: Optional[NumbersAchnullable] = UNSET
    eft: Optional[NumbersEftnullable] = UNSET
    international: Optional[NumbersInternationalNullable] = UNSET
    bacs: Optional[NumbersBacsnullable] = UNSET


class ProcessorNumberDict(TypedDict):
    ach: NotRequired[NumbersAchnullableDict]
    eft: NotRequired[NumbersEftnullableDict]
    international: NotRequired[NumbersInternationalNullableDict]
    bacs: NotRequired[NumbersBacsnullableDict]
