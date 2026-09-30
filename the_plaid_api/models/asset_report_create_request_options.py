from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asset_report_user import AssetReportUser, AssetReportUserDict


class AssetReportCreateRequestOptions(SdkBaseModel):
    """An optional object to filter ``/asset_report/create`` results. If provided, must be non-``null``. The optional
    ``user`` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program."""

    client_report_id: Optional[str] = UNSET
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    webhook: Optional[str] = UNSET
    """URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready."""

    user: Optional[AssetReportUser] = UNSET
    """The user object allows you to provide additional information about the user to be appended to the Asset Report.
    All fields are optional. The ``first_name``, ``last_name``, and ``ssn`` fields are required if you would like the
    Report to be eligible for Fannie Mae’s Day 1 Certainty™ program."""


class AssetReportCreateRequestOptionsDict(TypedDict):
    client_report_id: NotRequired[str]
    webhook: NotRequired[str]
    user: NotRequired[AssetReportUserDict]
