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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.signal_decision_report_request import SignalDecisionReportRequest, SignalDecisionReportRequestDict
from ..models.signal_decision_report_response import SignalDecisionReportResponse
from ..models.signal_evaluate_request import SignalEvaluateRequest, SignalEvaluateRequestDict
from ..models.signal_evaluate_response import SignalEvaluateResponse
from ..models.signal_return_report_request import SignalReturnReportRequest, SignalReturnReportRequestDict
from ..models.signal_return_report_response import SignalReturnReportResponse
from ..server.server import Server


class Signal:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SignalWithRawResponse(client, server, auth)

    def signal_decision_report(
        self,
        body: SignalDecisionReportRequest | SignalDecisionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalDecisionReportResponse:
        """After calling ``/signal/evaluate``, call ``/signal/decision/report`` to report whether the transaction was
        initiated. This endpoint will return an ``INVALID_REQUEST`` error if called a second time with a different value
        for ``initiated``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.signal_decision_report(body, request_options=request_options).unwrap()

    def signal_evaluate(
        self,
        body: SignalEvaluateRequest | SignalEvaluateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalEvaluateResponse:
        """Use ``/signal/evaluate`` to evaluate a planned ACH transaction to get a return risk assessment (such as a
        risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and
        the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the
        transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying
        cause.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.signal_evaluate(body, request_options=request_options).unwrap()

    def signal_return_report(
        self,
        body: SignalReturnReportRequest | SignalReturnReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalReturnReportResponse:
        """Call the ``/signal/return/report`` endpoint to report a returned transaction that was previously sent to the
        ``/signal/evaluate`` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in
        your portfolio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.signal_return_report(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SignalWithRawResponse:
        return self._with_raw_response


class AsyncSignal:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSignalWithRawResponse(client, server, auth)

    async def signal_decision_report(
        self,
        body: SignalDecisionReportRequest | SignalDecisionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalDecisionReportResponse:
        """After calling ``/signal/evaluate``, call ``/signal/decision/report`` to report whether the transaction was
        initiated. This endpoint will return an ``INVALID_REQUEST`` error if called a second time with a different value
        for ``initiated``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.signal_decision_report(body, request_options=request_options)).unwrap()

    async def signal_evaluate(
        self,
        body: SignalEvaluateRequest | SignalEvaluateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalEvaluateResponse:
        """Use ``/signal/evaluate`` to evaluate a planned ACH transaction to get a return risk assessment (such as a
        risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and
        the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the
        transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying
        cause.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.signal_evaluate(body, request_options=request_options)).unwrap()

    async def signal_return_report(
        self,
        body: SignalReturnReportRequest | SignalReturnReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SignalReturnReportResponse:
        """Call the ``/signal/return/report`` endpoint to report a returned transaction that was previously sent to the
        ``/signal/evaluate`` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in
        your portfolio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.signal_return_report(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSignalWithRawResponse:
        return self._with_raw_response


class SignalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def signal_decision_report(
        self,
        body: SignalDecisionReportRequest | SignalDecisionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalDecisionReportResponse, RawError]:
        """After calling ``/signal/evaluate``, call ``/signal/decision/report`` to report whether the transaction was
        initiated. This endpoint will return an ``INVALID_REQUEST`` error if called a second time with a different value
        for ``initiated``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/decision/report"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalDecisionReportRequest | SignalDecisionReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SignalDecisionReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def signal_evaluate(
        self,
        body: SignalEvaluateRequest | SignalEvaluateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalEvaluateResponse, RawError]:
        """Use ``/signal/evaluate`` to evaluate a planned ACH transaction to get a return risk assessment (such as a
        risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and
        the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the
        transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying
        cause.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/evaluate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalEvaluateRequest | SignalEvaluateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SignalEvaluateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def signal_return_report(
        self,
        body: SignalReturnReportRequest | SignalReturnReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalReturnReportResponse, RawError]:
        """Call the ``/signal/return/report`` endpoint to report a returned transaction that was previously sent to the
        ``/signal/evaluate`` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in
        your portfolio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/return/report"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalReturnReportRequest | SignalReturnReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SignalReturnReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSignalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def signal_decision_report(
        self,
        body: SignalDecisionReportRequest | SignalDecisionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalDecisionReportResponse, RawError]:
        """After calling ``/signal/evaluate``, call ``/signal/decision/report`` to report whether the transaction was
        initiated. This endpoint will return an ``INVALID_REQUEST`` error if called a second time with a different value
        for ``initiated``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/decision/report"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalDecisionReportRequest | SignalDecisionReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SignalDecisionReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def signal_evaluate(
        self,
        body: SignalEvaluateRequest | SignalEvaluateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalEvaluateResponse, RawError]:
        """Use ``/signal/evaluate`` to evaluate a planned ACH transaction to get a return risk assessment (such as a
        risk score and risk tier) and additional risk signals.

        In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and
        the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the
        transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying
        cause.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/evaluate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalEvaluateRequest | SignalEvaluateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SignalEvaluateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def signal_return_report(
        self,
        body: SignalReturnReportRequest | SignalReturnReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SignalReturnReportResponse, RawError]:
        """Call the ``/signal/return/report`` endpoint to report a returned transaction that was previously sent to the
        ``/signal/evaluate`` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in
        your portfolio.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/signal/return/report"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SignalReturnReportRequest | SignalReturnReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SignalReturnReportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
