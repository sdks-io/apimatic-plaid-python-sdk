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
from ..models.auth_get_request import AuthGetRequest, AuthGetRequestDict
from ..models.auth_get_response import AuthGetResponse
from ..server.server import Server


class AuthApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthApiWithRawResponse(client, server, auth)

    def auth_get(
        self, body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthGetResponse:
        """The ``/auth/get`` endpoint returns the bank account and bank identification numbers (such as routing numbers,
        for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and
        balances when available.

        Note: This request may take some time to complete if ``auth`` was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Also note that ``/auth/get`` will not return data for any new accounts opened after the Item was created. To
        obtain data for new accounts, create a new Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.auth_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthApiWithRawResponse:
        return self._with_raw_response


class AsyncAuthApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthApiWithRawResponse(client, server, auth)

    async def auth_get(
        self, body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AuthGetResponse:
        """The ``/auth/get`` endpoint returns the bank account and bank identification numbers (such as routing numbers,
        for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and
        balances when available.

        Note: This request may take some time to complete if ``auth`` was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Also note that ``/auth/get`` will not return data for any new accounts opened after the Item was created. To
        obtain data for new accounts, create a new Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.auth_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthApiWithRawResponse:
        return self._with_raw_response


class AuthApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def auth_get(
        self, body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthGetResponse, RawError]:
        """The ``/auth/get`` endpoint returns the bank account and bank identification numbers (such as routing numbers,
        for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and
        balances when available.

        Note: This request may take some time to complete if ``auth`` was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Also note that ``/auth/get`` will not return data for any new accounts opened after the Item was created. To
        obtain data for new accounts, create a new Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthGetRequest | AuthGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[AuthGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAuthApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def auth_get(
        self, body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AuthGetResponse, RawError]:
        """The ``/auth/get`` endpoint returns the bank account and bank identification numbers (such as routing numbers,
        for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and
        balances when available.

        Note: This request may take some time to complete if ``auth`` was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Also note that ``/auth/get`` will not return data for any new accounts opened after the Item was created. To
        obtain data for new accounts, create a new Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthGetRequest | AuthGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[AuthGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
