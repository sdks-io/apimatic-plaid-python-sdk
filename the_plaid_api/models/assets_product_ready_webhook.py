from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AssetsProductReadyWebhook(SdkBaseModel):
    """Fired when the Asset Report has been generated and ``/asset_report/get`` is ready to be called. If you attempt to
    retrieve an Asset Report before this webhook has fired, you’ll receive a response with the HTTP status code 400 and
    a Plaid error code of ``PRODUCT_NOT_READY``."""

    webhook_type: str
    """``ASSETS``"""

    webhook_code: str
    """``PRODUCT_READY``"""

    asset_report_id: str
    """The ``asset_report_id`` that can be provided to ``/asset_report/get`` to retrieve the Asset Report."""


class AssetsProductReadyWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    asset_report_id: str
