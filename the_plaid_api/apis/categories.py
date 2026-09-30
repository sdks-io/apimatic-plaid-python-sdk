from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    text_body,
)
from ..models.categories_get_response import CategoriesGetResponse
from ..server.server import Server


class Categories:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = CategoriesWithRawResponse(client, server)

    def categories_get(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> CategoriesGetResponse:
        """Send a request to the ``/categories/get`` endpoint to get detailed information on categories returned by
        Plaid. This endpoint does not require authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.categories_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CategoriesWithRawResponse:
        return self._with_raw_response


class AsyncCategories:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncCategoriesWithRawResponse(client, server)

    async def categories_get(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> CategoriesGetResponse:
        """Send a request to the ``/categories/get`` endpoint to get detailed information on categories returned by
        Plaid. This endpoint does not require authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.categories_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCategoriesWithRawResponse:
        return self._with_raw_response


class CategoriesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def categories_get(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoriesGetResponse, RawError]:
        """Send a request to the ``/categories/get`` endpoint to get detailed information on categories returned by
        Plaid. This endpoint does not require authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/categories/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=text_body[Any](body),
            decoder=json_decoder[CategoriesGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCategoriesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def categories_get(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CategoriesGetResponse, RawError]:
        """Send a request to the ``/categories/get`` endpoint to get detailed information on categories returned by
        Plaid. This endpoint does not require authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/categories/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=text_body[Any](body),
            decoder=async_json_decoder[CategoriesGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
