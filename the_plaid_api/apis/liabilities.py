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
from ..models.liabilities_get_request import LiabilitiesGetRequest, LiabilitiesGetRequestDict
from ..models.liabilities_get_response import LiabilitiesGetResponse
from ..server.server import Server


class Liabilities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LiabilitiesWithRawResponse(client, server, auth)

    def liabilities_get(
        self,
        body: LiabilitiesGetRequest | LiabilitiesGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LiabilitiesGetResponse:
        """The ``/liabilities/get`` endpoint returns various details about an Item with loan or credit accounts.
        Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian
        institutions. Currently supported account types are account type ``credit`` with account subtype ``credit card``
        or ``paypal``, and account type ``loan`` with account subtype ``student`` or ``mortgage``. To limit accounts
        listed in Link to types and subtypes supported by Liabilities, you can use the ``account_filters`` parameter
        when `creating a Link token <https://plaid.com/docs/api/tokens/#linktokencreate>`__.

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account
        details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest
        data can be retrieved by calling ``/liabilities/get``.

        Note: This request may take some time to complete if ``liabilities`` was not specified as an initial product
        when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the
        additional data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.liabilities_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> LiabilitiesWithRawResponse:
        return self._with_raw_response


class AsyncLiabilities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLiabilitiesWithRawResponse(client, server, auth)

    async def liabilities_get(
        self,
        body: LiabilitiesGetRequest | LiabilitiesGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LiabilitiesGetResponse:
        """The ``/liabilities/get`` endpoint returns various details about an Item with loan or credit accounts.
        Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian
        institutions. Currently supported account types are account type ``credit`` with account subtype ``credit card``
        or ``paypal``, and account type ``loan`` with account subtype ``student`` or ``mortgage``. To limit accounts
        listed in Link to types and subtypes supported by Liabilities, you can use the ``account_filters`` parameter
        when `creating a Link token <https://plaid.com/docs/api/tokens/#linktokencreate>`__.

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account
        details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest
        data can be retrieved by calling ``/liabilities/get``.

        Note: This request may take some time to complete if ``liabilities`` was not specified as an initial product
        when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the
        additional data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.liabilities_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncLiabilitiesWithRawResponse:
        return self._with_raw_response


class LiabilitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def liabilities_get(
        self,
        body: LiabilitiesGetRequest | LiabilitiesGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LiabilitiesGetResponse, RawError]:
        """The ``/liabilities/get`` endpoint returns various details about an Item with loan or credit accounts.
        Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian
        institutions. Currently supported account types are account type ``credit`` with account subtype ``credit card``
        or ``paypal``, and account type ``loan`` with account subtype ``student`` or ``mortgage``. To limit accounts
        listed in Link to types and subtypes supported by Liabilities, you can use the ``account_filters`` parameter
        when `creating a Link token <https://plaid.com/docs/api/tokens/#linktokencreate>`__.

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account
        details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest
        data can be retrieved by calling ``/liabilities/get``.

        Note: This request may take some time to complete if ``liabilities`` was not specified as an initial product
        when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the
        additional data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/liabilities/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiabilitiesGetRequest | LiabilitiesGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[LiabilitiesGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLiabilitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def liabilities_get(
        self,
        body: LiabilitiesGetRequest | LiabilitiesGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LiabilitiesGetResponse, RawError]:
        """The ``/liabilities/get`` endpoint returns various details about an Item with loan or credit accounts.
        Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian
        institutions. Currently supported account types are account type ``credit`` with account subtype ``credit card``
        or ``paypal``, and account type ``loan`` with account subtype ``student`` or ``mortgage``. To limit accounts
        listed in Link to types and subtypes supported by Liabilities, you can use the ``account_filters`` parameter
        when `creating a Link token <https://plaid.com/docs/api/tokens/#linktokencreate>`__.

        The types of information returned by Liabilities can include balances and due dates, loan terms, and account
        details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest
        data can be retrieved by calling ``/liabilities/get``.

        Note: This request may take some time to complete if ``liabilities`` was not specified as an initial product
        when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the
        additional data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/liabilities/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LiabilitiesGetRequest | LiabilitiesGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[LiabilitiesGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
