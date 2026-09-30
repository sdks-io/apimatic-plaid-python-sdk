from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .institutions_search_payment_initiation_options import (
    InstitutionsSearchPaymentInitiationOptions,
    InstitutionsSearchPaymentInitiationOptionsDict,
)


class InstitutionsSearchRequestOptions(SdkBaseModel):
    """An optional object to filter ``/institutions/search`` results."""

    oauth: Optional[bool] = UNSET
    """Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with
    European country codes"""

    include_optional_metadata: Optional[bool] = UNSET
    """When true, return the institution's homepage URL, logo and primary brand color."""

    include_auth_metadata: bool = False
    """When ``true``, returns metadata related to the Auth product indicating which auth methods are supported."""

    include_payment_initiation_metadata: bool = False
    """When ``true``, returns metadata related to the Payment Initiation product indicating which payment configurations
    are supported."""

    payment_initiation: Optional[InstitutionsSearchPaymentInitiationOptions] = UNSET
    """Additional options that will be used to filter institutions by various Payment Initiation configurations."""


class InstitutionsSearchRequestOptionsDict(TypedDict):
    oauth: NotRequired[bool]
    include_optional_metadata: NotRequired[bool]
    include_auth_metadata: NotRequired[bool]
    include_payment_initiation_metadata: NotRequired[bool]
    payment_initiation: NotRequired[InstitutionsSearchPaymentInitiationOptionsDict]
