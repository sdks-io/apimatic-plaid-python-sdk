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
from ..models.application_get_request import ApplicationGetRequest, ApplicationGetRequestDict
from ..models.application_get_response import ApplicationGetResponse
from ..server.server import Server


class ApplicationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApplicationApiWithRawResponse(client, server, auth)

    def application_get(
        self,
        body: ApplicationGetRequest | ApplicationGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApplicationGetResponse:
        """Allows financial institutions to retrieve information about Plaid clients for the purpose of building
        control-tower experiences

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.application_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ApplicationApiWithRawResponse:
        return self._with_raw_response


class AsyncApplicationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApplicationApiWithRawResponse(client, server, auth)

    async def application_get(
        self,
        body: ApplicationGetRequest | ApplicationGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApplicationGetResponse:
        """Allows financial institutions to retrieve information about Plaid clients for the purpose of building
        control-tower experiences

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.application_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncApplicationApiWithRawResponse:
        return self._with_raw_response


class ApplicationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def application_get(
        self,
        body: ApplicationGetRequest | ApplicationGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApplicationGetResponse, RawError]:
        """Allows financial institutions to retrieve information about Plaid clients for the purpose of building
        control-tower experiences

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/application/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApplicationGetRequest | ApplicationGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ApplicationGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApplicationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def application_get(
        self,
        body: ApplicationGetRequest | ApplicationGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApplicationGetResponse, RawError]:
        """Allows financial institutions to retrieve information about Plaid clients for the purpose of building
        control-tower experiences

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/application/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApplicationGetRequest | ApplicationGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ApplicationGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
