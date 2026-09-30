from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.country_code import CountryCodeOrStr
from .enums.products import ProductsOrStr
from .institutions_search_request_options import InstitutionsSearchRequestOptions, InstitutionsSearchRequestOptionsDict


class InstitutionsSearchRequest(SdkBaseModel):
    """InstitutionsSearchRequest defines the request schema for ``/institutions/search``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    query: str
    """The search query. Institutions with names matching the query are returned"""

    products: list[ProductsOrStr]
    """Filter the Institutions based on whether they support all products listed in ``products``. Provide ``null`` to
    get institutions regardless of supported products. Note that when ``auth`` is specified as a product, if you are
    enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned
    even if ``auth`` is not present in their product array."""

    country_codes: list[CountryCodeOrStr]
    """Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country
    code standard."""

    options: Optional[InstitutionsSearchRequestOptions] = UNSET
    """An optional object to filter ``/institutions/search`` results."""


class InstitutionsSearchRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    query: str
    products: list[ProductsOrStr]
    country_codes: list[CountryCodeOrStr]
    options: NotRequired[InstitutionsSearchRequestOptionsDict]
