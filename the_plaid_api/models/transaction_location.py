from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionLocation(SdkBaseModel):
    """A representation of where a transaction took place"""

    address: str | None
    """The street address where the transaction occurred."""

    city: str | None
    """The city where the transaction occurred."""

    region: str | None
    """The region or state where the transaction occurred."""

    postal_code: str | None
    """The postal code where the transaction occurred."""

    country: str | None
    """The ISO 3166-1 alpha-2 country code where the transaction occurred."""

    lat: float | None
    """The latitude where the transaction occurred."""

    lon: float | None
    """The longitude where the transaction occurred."""

    store_number: str | None
    """The merchant defined store number where the transaction occurred."""


class TransactionLocationDict(TypedDict):
    address: str | None
    city: str | None
    region: str | None
    postal_code: str | None
    country: str | None
    lat: float | None
    lon: float | None
    store_number: str | None
