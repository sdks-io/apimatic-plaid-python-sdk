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
from ..models.institutions_get_by_id_request import InstitutionsGetByIdRequest, InstitutionsGetByIdRequestDict
from ..models.institutions_get_by_id_response import InstitutionsGetByIdResponse
from ..models.institutions_get_request import InstitutionsGetRequest, InstitutionsGetRequestDict
from ..models.institutions_get_response import InstitutionsGetResponse
from ..models.institutions_search_request import InstitutionsSearchRequest, InstitutionsSearchRequestDict
from ..models.institutions_search_response import InstitutionsSearchResponse
from ..server.server import Server


class Institutions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InstitutionsWithRawResponse(client, server, auth)

    def institutions_get(
        self,
        body: InstitutionsGetRequest | InstitutionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsGetResponse:
        """Returns a JSON response containing details on all financial institutions currently supported by Plaid.
        Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the
        institution will be filtered out from the response. As a result, the number of institutions returned may not
        match the count specified in the call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutions_get(body, request_options=request_options).unwrap()

    def institutions_get_by_id(
        self,
        body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsGetByIdResponse:
        """Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutions_get_by_id(body, request_options=request_options).unwrap()

    def institutions_search(
        self,
        body: InstitutionsSearchRequest | InstitutionsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsSearchResponse:
        """Returns a JSON response containing details for institutions that match the query parameters, up to a maximum
        of ten institutions per query.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.institutions_search(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InstitutionsWithRawResponse:
        return self._with_raw_response


class AsyncInstitutions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInstitutionsWithRawResponse(client, server, auth)

    async def institutions_get(
        self,
        body: InstitutionsGetRequest | InstitutionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsGetResponse:
        """Returns a JSON response containing details on all financial institutions currently supported by Plaid.
        Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the
        institution will be filtered out from the response. As a result, the number of institutions returned may not
        match the count specified in the call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.institutions_get(body, request_options=request_options)).unwrap()

    async def institutions_get_by_id(
        self,
        body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsGetByIdResponse:
        """Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.institutions_get_by_id(body, request_options=request_options)).unwrap()

    async def institutions_search(
        self,
        body: InstitutionsSearchRequest | InstitutionsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InstitutionsSearchResponse:
        """Returns a JSON response containing details for institutions that match the query parameters, up to a maximum
        of ten institutions per query.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.institutions_search(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncInstitutionsWithRawResponse:
        return self._with_raw_response


class InstitutionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def institutions_get(
        self,
        body: InstitutionsGetRequest | InstitutionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsGetResponse, RawError]:
        """Returns a JSON response containing details on all financial institutions currently supported by Plaid.
        Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the
        institution will be filtered out from the response. As a result, the number of institutions returned may not
        match the count specified in the call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsGetRequest | InstitutionsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[InstitutionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def institutions_get_by_id(
        self,
        body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsGetByIdResponse, RawError]:
        """Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/get_by_id"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[InstitutionsGetByIdResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def institutions_search(
        self,
        body: InstitutionsSearchRequest | InstitutionsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsSearchResponse, RawError]:
        """Returns a JSON response containing details for institutions that match the query parameters, up to a maximum
        of ten institutions per query.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsSearchRequest | InstitutionsSearchRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[InstitutionsSearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInstitutionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def institutions_get(
        self,
        body: InstitutionsGetRequest | InstitutionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsGetResponse, RawError]:
        """Returns a JSON response containing details on all financial institutions currently supported by Plaid.
        Because Plaid supports thousands of institutions, results are paginated.

        If there is no overlap between an institution’s enabled products and a client’s enabled products, then the
        institution will be filtered out from the response. As a result, the number of institutions returned may not
        match the count specified in the call.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsGetRequest | InstitutionsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[InstitutionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def institutions_get_by_id(
        self,
        body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsGetByIdResponse, RawError]:
        """Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/get_by_id"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[InstitutionsGetByIdResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def institutions_search(
        self,
        body: InstitutionsSearchRequest | InstitutionsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InstitutionsSearchResponse, RawError]:
        """Returns a JSON response containing details for institutions that match the query parameters, up to a maximum
        of ten institutions per query.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/institutions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InstitutionsSearchRequest | InstitutionsSearchRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[InstitutionsSearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
