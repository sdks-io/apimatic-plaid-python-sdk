from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AssetReportGetRequest(SdkBaseModel):
    """AssetReportGetRequest defines the request schema for ``/asset_report/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    asset_report_token: str
    """A token that can be provided to endpoints such as ``/asset_report/get`` or ``/asset_report/pdf/get`` to fetch or
    update an Asset Report."""

    include_insights: Optional[bool] = UNSET
    """``true`` if you would like to retrieve the Asset Report with Insights, ``false`` otherwise. This field defaults
    to ``false`` if omitted."""


class AssetReportGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    asset_report_token: str
    include_insights: NotRequired[bool]
