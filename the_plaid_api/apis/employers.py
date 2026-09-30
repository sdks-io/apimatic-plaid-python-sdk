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
from ..models.employers_search_request import EmployersSearchRequest, EmployersSearchRequestDict
from ..models.employers_search_response import EmployersSearchResponse
from ..server.server import Server


class Employers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmployersWithRawResponse(client, server, auth)

    def employers_search(
        self,
        body: EmployersSearchRequest | EmployersSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EmployersSearchResponse:
        """``/employers/search`` allows you the ability to search Plaid’s database of known employers, for use with
        Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are
        supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress
        through their respective beta periods, more employers are being regularly added. Because the employer database
        is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.employers_search(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EmployersWithRawResponse:
        return self._with_raw_response


class AsyncEmployers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmployersWithRawResponse(client, server, auth)

    async def employers_search(
        self,
        body: EmployersSearchRequest | EmployersSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> EmployersSearchResponse:
        """``/employers/search`` allows you the ability to search Plaid’s database of known employers, for use with
        Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are
        supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress
        through their respective beta periods, more employers are being regularly added. Because the employer database
        is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.employers_search(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncEmployersWithRawResponse:
        return self._with_raw_response


class EmployersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def employers_search(
        self,
        body: EmployersSearchRequest | EmployersSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EmployersSearchResponse, RawError]:
        """``/employers/search`` allows you the ability to search Plaid’s database of known employers, for use with
        Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are
        supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress
        through their respective beta periods, more employers are being regularly added. Because the employer database
        is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/employers/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EmployersSearchRequest | EmployersSearchRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[EmployersSearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEmployersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def employers_search(
        self,
        body: EmployersSearchRequest | EmployersSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[EmployersSearchResponse, RawError]:
        """``/employers/search`` allows you the ability to search Plaid’s database of known employers, for use with
        Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are
        supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

        The data in the employer database is currently limited. As the Deposit Switch and Income products progress
        through their respective beta periods, more employers are being regularly added. Because the employer database
        is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/employers/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EmployersSearchRequest | EmployersSearchRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[EmployersSearchResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
