from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Address2(SdkBaseModel):
    city: OptionalNullable[str] = UNSET
    """The full city name."""

    street: OptionalNullable[str] = UNSET
    """The listed street address."""

    line1: OptionalNullable[str] = UNSET
    """Street address line 1."""

    line2: OptionalNullable[str] = UNSET
    """Street address line 2."""

    postal_code: OptionalNullable[str] = UNSET
    """5 digit postal code."""

    region: OptionalNullable[str] = UNSET
    """The region or state Example: ``"NC"``"""

    state_code: OptionalNullable[str] = UNSET
    """The region or state Example: ``"NC"``"""

    country: OptionalNullable[str] = UNSET
    """The country of the address."""


class Address2Dict(TypedDict):
    city: NotRequired[str | None]
    street: NotRequired[str | None]
    line1: NotRequired[str | None]
    line2: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    region: NotRequired[str | None]
    state_code: NotRequired[str | None]
    country: NotRequired[str | None]
