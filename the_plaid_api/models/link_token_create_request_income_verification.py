from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkTokenCreateRequestIncomeVerification(SdkBaseModel):
    """Specifies options for initializing Link for use with the Income (beta) product. This field is required if
    ``income_verification`` is included in the ``products`` array."""

    income_verification_id: str
    """The ``income_verification_id`` of the verification instance, as provided by ``/income/verification/create``."""

    asset_report_id: Optional[str] = UNSET
    """The ``asset_report_id`` of an asset report associated with the user, as provided by ``/asset_report/create``.
    Providing an ``asset_report_id`` is optional and can be used to verify the user through a streamlined flow. If
    provided, the bank linking flow will be skipped."""


class LinkTokenCreateRequestIncomeVerificationDict(TypedDict):
    income_verification_id: str
    asset_report_id: NotRequired[str]
