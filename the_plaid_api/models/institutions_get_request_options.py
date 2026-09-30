from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.products import ProductsOrStr


class InstitutionsGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/institutions/get`` results."""

    products: Optional[list[ProductsOrStr]] = UNSET
    """Filter the Institutions based on which products they support."""

    routing_numbers: Optional[list[str]] = UNSET
    """Specify an array of routing numbers to filter institutions. The response will only return institutions that match
    all of the routing numbers in the array."""

    oauth: Optional[bool] = UNSET
    """Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with
    European country codes."""

    include_optional_metadata: Optional[bool] = UNSET
    """When ``true``, return the institution's homepage URL, logo and primary brand color.

    Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you
    agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the
    appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied
    warranties with respect to the logos."""

    include_auth_metadata: bool = False
    """When ``true``, returns metadata related to the Auth product indicating which auth methods are supported."""

    include_payment_initiation_metadata: bool = False
    """When ``true``, returns metadata related to the Payment Initiation product indicating which payment configurations
    are supported."""


class InstitutionsGetRequestOptionsDict(TypedDict):
    products: NotRequired[list[ProductsOrStr]]
    routing_numbers: NotRequired[list[str]]
    oauth: NotRequired[bool]
    include_optional_metadata: NotRequired[bool]
    include_auth_metadata: NotRequired[bool]
    include_payment_initiation_metadata: NotRequired[bool]
