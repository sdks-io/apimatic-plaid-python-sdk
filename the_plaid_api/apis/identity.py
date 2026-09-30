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
from ..models.identity_get_request import IdentityGetRequest, IdentityGetRequestDict
from ..models.identity_get_response import IdentityGetResponse
from ..server.server import Server


class Identity:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = IdentityWithRawResponse(client, server, auth)

    def identity_get(
        self, body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> IdentityGetResponse:
        """The ``/identity/get`` endpoint allows you to retrieve various account holder information on file with the
        financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be
        returned; other fields will be empty arrays if not provided by the institution.

        Note: This request may take some time to complete if identity was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.identity_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> IdentityWithRawResponse:
        return self._with_raw_response


class AsyncIdentity:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncIdentityWithRawResponse(client, server, auth)

    async def identity_get(
        self, body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> IdentityGetResponse:
        """The ``/identity/get`` endpoint allows you to retrieve various account holder information on file with the
        financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be
        returned; other fields will be empty arrays if not provided by the institution.

        Note: This request may take some time to complete if identity was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.identity_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncIdentityWithRawResponse:
        return self._with_raw_response


class IdentityWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def identity_get(
        self, body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IdentityGetResponse, RawError]:
        """The ``/identity/get`` endpoint allows you to retrieve various account holder information on file with the
        financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be
        returned; other fields will be empty arrays if not provided by the institution.

        Note: This request may take some time to complete if identity was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/identity/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdentityGetRequest | IdentityGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[IdentityGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncIdentityWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def identity_get(
        self, body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[IdentityGetResponse, RawError]:
        """The ``/identity/get`` endpoint allows you to retrieve various account holder information on file with the
        financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be
        returned; other fields will be empty arrays if not provided by the institution.

        Note: This request may take some time to complete if identity was not specified as an initial product when
        creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/identity/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdentityGetRequest | IdentityGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[IdentityGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
