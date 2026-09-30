from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.income_verification_create_request import (
    IncomeVerificationCreateRequest,
    IncomeVerificationCreateRequestDict,
)
from ..models.income_verification_create_response import IncomeVerificationCreateResponse
from ..models.income_verification_documents_download_request import (
    IncomeVerificationDocumentsDownloadRequest,
    IncomeVerificationDocumentsDownloadRequestDict,
)
from ..models.income_verification_paystub_get_request import (
    IncomeVerificationPaystubGetRequest,
    IncomeVerificationPaystubGetRequestDict,
)
from ..models.income_verification_paystub_get_response import IncomeVerificationPaystubGetResponse
from ..models.income_verification_paystubs_get_request import (
    IncomeVerificationPaystubsGetRequest,
    IncomeVerificationPaystubsGetRequestDict,
)
from ..models.income_verification_paystubs_get_response import IncomeVerificationPaystubsGetResponse
from ..models.income_verification_precheck_request import (
    IncomeVerificationPrecheckRequest,
    IncomeVerificationPrecheckRequestDict,
)
from ..models.income_verification_precheck_response import IncomeVerificationPrecheckResponse
from ..models.income_verification_refresh_request import (
    IncomeVerificationRefreshRequest,
    IncomeVerificationRefreshRequestDict,
)
from ..models.income_verification_refresh_response import IncomeVerificationRefreshResponse
from ..models.income_verification_summary_get_request import (
    IncomeVerificationSummaryGetRequest,
    IncomeVerificationSummaryGetRequestDict,
)
from ..models.income_verification_summary_get_response import IncomeVerificationSummaryGetResponse
from ..models.income_verification_taxforms_get_request import (
    IncomeVerificationTaxformsGetRequest,
    IncomeVerificationTaxformsGetRequestDict,
)
from ..models.income_verification_taxforms_get_response import IncomeVerificationTaxformsGetResponse
from ..server.server import Server


class Income:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = IncomeWithRawResponse(client, server, auth)

    def income_verification_create(
        self,
        body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationCreateResponse:
        """``/income/verification/create`` begins the income verification process by returning an
        ``income_verification_id``. You can then provide the ``income_verification_id`` to ``/link/token/create`` under
        the ``income_verification`` parameter in order to create a Link instance that will prompt the user to go through
        the income verification flow. Plaid will fire an ``INCOME`` webhook once the user completes the Payroll Income
        flow, or when the uploaded documents in the Document Income flow have finished processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_create(body, request_options=request_options).unwrap()

    def income_verification_documents_download(
        self,
        body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """``/income/verification/documents/download`` provides the ability to download the source paystub PDF that the
        end user uploaded via Paystub Import.

        The response to ``/income/verification/documents/download`` is a ZIP file in binary data. The ``request_id`` is
        returned in the ``Plaid-Request-ID`` header.

        For Payroll Income, the most recent file available for download with the payroll provider will also be available
        from this endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A ZIP file containing the source paystub(s) used as the basis for income verification.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_documents_download(
            body, request_options=request_options
        ).unwrap()

    def income_verification_paystub_get(
        self,
        body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPaystubGetResponse:
        """(Deprecated) Retrieve information from a single paystub used for income verification

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_paystub_get(body, request_options=request_options).unwrap()

    def income_verification_paystubs_get(
        self,
        body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPaystubsGetResponse:
        """``/income/verification/paystubs/get`` returns the information collected from the paystubs that were used to
        verify an end user's income. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_paystubs_get(body, request_options=request_options).unwrap()

    def income_verification_precheck(
        self,
        body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPrecheckResponse:
        """``/income/verification/precheck`` returns whether a given user is supportable by the income product

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_precheck(body, request_options=request_options).unwrap()

    def income_verification_refresh(
        self,
        body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationRefreshResponse:
        """``/income/verification/refresh`` refreshes a given income verification.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_refresh(body, request_options=request_options).unwrap()

    def income_verification_summary_get(
        self,
        body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationSummaryGetResponse:
        """``/income/verification/summary/get`` returns a verification summary for the income that was verified for an
        end user. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_summary_get(body, request_options=request_options).unwrap()

    def income_verification_taxforms_get(
        self,
        body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationTaxformsGetResponse:
        """``/income/verification/taxforms/get`` returns the information collected from taxforms that were used to
        verify an end user's. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.income_verification_taxforms_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> IncomeWithRawResponse:
        return self._with_raw_response


class AsyncIncome:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncIncomeWithRawResponse(client, server, auth)

    async def income_verification_create(
        self,
        body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationCreateResponse:
        """``/income/verification/create`` begins the income verification process by returning an
        ``income_verification_id``. You can then provide the ``income_verification_id`` to ``/link/token/create`` under
        the ``income_verification`` parameter in order to create a Link instance that will prompt the user to go through
        the income verification flow. Plaid will fire an ``INCOME`` webhook once the user completes the Payroll Income
        flow, or when the uploaded documents in the Document Income flow have finished processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_create(body, request_options=request_options)
        ).unwrap()

    async def income_verification_documents_download(
        self,
        body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """``/income/verification/documents/download`` provides the ability to download the source paystub PDF that the
        end user uploaded via Paystub Import.

        The response to ``/income/verification/documents/download`` is a ZIP file in binary data. The ``request_id`` is
        returned in the ``Plaid-Request-ID`` header.

        For Payroll Income, the most recent file available for download with the payroll provider will also be available
        from this endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A ZIP file containing the source paystub(s) used as the basis for income verification.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_documents_download(body, request_options=request_options)
        ).unwrap()

    async def income_verification_paystub_get(
        self,
        body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPaystubGetResponse:
        """(Deprecated) Retrieve information from a single paystub used for income verification

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_paystub_get(body, request_options=request_options)
        ).unwrap()

    async def income_verification_paystubs_get(
        self,
        body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPaystubsGetResponse:
        """``/income/verification/paystubs/get`` returns the information collected from the paystubs that were used to
        verify an end user's income. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_paystubs_get(body, request_options=request_options)
        ).unwrap()

    async def income_verification_precheck(
        self,
        body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationPrecheckResponse:
        """``/income/verification/precheck`` returns whether a given user is supportable by the income product

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_precheck(body, request_options=request_options)
        ).unwrap()

    async def income_verification_refresh(
        self,
        body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationRefreshResponse:
        """``/income/verification/refresh`` refreshes a given income verification.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_refresh(body, request_options=request_options)
        ).unwrap()

    async def income_verification_summary_get(
        self,
        body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationSummaryGetResponse:
        """``/income/verification/summary/get`` returns a verification summary for the income that was verified for an
        end user. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_summary_get(body, request_options=request_options)
        ).unwrap()

    async def income_verification_taxforms_get(
        self,
        body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IncomeVerificationTaxformsGetResponse:
        """``/income/verification/taxforms/get`` returns the information collected from taxforms that were used to
        verify an end user's. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.income_verification_taxforms_get(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncIncomeWithRawResponse:
        return self._with_raw_response


class IncomeWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def income_verification_create(
        self,
        body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationCreateResponse, RawError]:
        """``/income/verification/create`` begins the income verification process by returning an
        ``income_verification_id``. You can then provide the ``income_verification_id`` to ``/link/token/create`` under
        the ``income_verification`` parameter in order to create a Link instance that will prompt the user to go through
        the income verification flow. Plaid will fire an ``INCOME`` webhook once the user completes the Payroll Income
        flow, or when the uploaded documents in the Document Income flow have finished processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_documents_download(
        self,
        body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """``/income/verification/documents/download`` provides the ability to download the source paystub PDF that the
        end user uploaded via Paystub Import.

        The response to ``/income/verification/documents/download`` is a ZIP file in binary data. The ``request_id`` is
        returned in the ``Plaid-Request-ID`` header.

        For Payroll Income, the most recent file available for download with the payroll provider will also be available
        from this endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/documents/download"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict](
                body
            ),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_paystub_get(
        self,
        body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPaystubGetResponse, RawError]:
        """(Deprecated) Retrieve information from a single paystub used for income verification

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/paystub/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationPaystubGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_paystubs_get(
        self,
        body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPaystubsGetResponse, RawError]:
        """``/income/verification/paystubs/get`` returns the information collected from the paystubs that were used to
        verify an end user's income. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/paystubs/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationPaystubsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_precheck(
        self,
        body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPrecheckResponse, RawError]:
        """``/income/verification/precheck`` returns whether a given user is supportable by the income product

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/precheck"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationPrecheckResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_refresh(
        self,
        body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationRefreshResponse, RawError]:
        """``/income/verification/refresh`` refreshes a given income verification.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationRefreshResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_summary_get(
        self,
        body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationSummaryGetResponse, RawError]:
        """``/income/verification/summary/get`` returns a verification summary for the income that was verified for an
        end user. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/summary/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationSummaryGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def income_verification_taxforms_get(
        self,
        body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationTaxformsGetResponse, RawError]:
        """``/income/verification/taxforms/get`` returns the information collected from taxforms that were used to
        verify an end user's. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/taxforms/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IncomeVerificationTaxformsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncIncomeWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def income_verification_create(
        self,
        body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationCreateResponse, RawError]:
        """``/income/verification/create`` begins the income verification process by returning an
        ``income_verification_id``. You can then provide the ``income_verification_id`` to ``/link/token/create`` under
        the ``income_verification`` parameter in order to create a Link instance that will prompt the user to go through
        the income verification flow. Plaid will fire an ``INCOME`` webhook once the user completes the Payroll Income
        flow, or when the uploaded documents in the Document Income flow have finished processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_documents_download(
        self,
        body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """``/income/verification/documents/download`` provides the ability to download the source paystub PDF that the
        end user uploaded via Paystub Import.

        The response to ``/income/verification/documents/download`` is a ZIP file in binary data. The ``request_id`` is
        returned in the ``Plaid-Request-ID`` header.

        For Payroll Income, the most recent file available for download with the payroll provider will also be available
        from this endpoint.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/documents/download"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict](
                body
            ),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_paystub_get(
        self,
        body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPaystubGetResponse, RawError]:
        """(Deprecated) Retrieve information from a single paystub used for income verification

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/paystub/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationPaystubGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_paystubs_get(
        self,
        body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPaystubsGetResponse, RawError]:
        """``/income/verification/paystubs/get`` returns the information collected from the paystubs that were used to
        verify an end user's income. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/paystubs/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationPaystubsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_precheck(
        self,
        body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationPrecheckResponse, RawError]:
        """``/income/verification/precheck`` returns whether a given user is supportable by the income product

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/precheck"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationPrecheckResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_refresh(
        self,
        body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationRefreshResponse, RawError]:
        """``/income/verification/refresh`` refreshes a given income verification.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationRefreshResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_summary_get(
        self,
        body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationSummaryGetResponse, RawError]:
        """``/income/verification/summary/get`` returns a verification summary for the income that was verified for an
        end user. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/summary/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationSummaryGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def income_verification_taxforms_get(
        self,
        body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IncomeVerificationTaxformsGetResponse, RawError]:
        """``/income/verification/taxforms/get`` returns the information collected from taxforms that were used to
        verify an end user's. It can be called once the status of the verification has been set to
        ``VERIFICATION_STATUS_PROCESSING_COMPLETE``, as reported by the ``INCOME: verification_status`` webhook.
        Attempting to call the endpoint before verification has been completed will result in an error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/income/verification/taxforms/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IncomeVerificationTaxformsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
