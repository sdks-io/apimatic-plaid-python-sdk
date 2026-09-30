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
from ..models.investments_holdings_get_request import InvestmentsHoldingsGetRequest, InvestmentsHoldingsGetRequestDict
from ..models.investments_holdings_get_response import InvestmentsHoldingsGetResponse
from ..models.investments_transactions_get_request import (
    InvestmentsTransactionsGetRequest,
    InvestmentsTransactionsGetRequestDict,
)
from ..models.investments_transactions_get_response import InvestmentsTransactionsGetResponse
from ..server.server import Server


class Investments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InvestmentsWithRawResponse(client, server, auth)

    def investments_holdings_get(
        self,
        body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvestmentsHoldingsGetResponse:
        """The ``/investments/holdings/get`` endpoint allows developers to receive user-authorized stock position data
        for ``investment``-type accounts.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.investments_holdings_get(body, request_options=request_options).unwrap()

    def investments_transactions_get(
        self,
        body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvestmentsTransactionsGetResponse:
        """The ``/investments/transactions/get`` endpoint allows developers to retrieve user-authorized transaction data
        for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated.
        Manipulate the count and offset parameters in conjunction with the ``total_investment_transactions`` response
        body field to fetch all available investment transactions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.investments_transactions_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InvestmentsWithRawResponse:
        return self._with_raw_response


class AsyncInvestments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInvestmentsWithRawResponse(client, server, auth)

    async def investments_holdings_get(
        self,
        body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvestmentsHoldingsGetResponse:
        """The ``/investments/holdings/get`` endpoint allows developers to receive user-authorized stock position data
        for ``investment``-type accounts.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.investments_holdings_get(body, request_options=request_options)).unwrap()

    async def investments_transactions_get(
        self,
        body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InvestmentsTransactionsGetResponse:
        """The ``/investments/transactions/get`` endpoint allows developers to retrieve user-authorized transaction data
        for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated.
        Manipulate the count and offset parameters in conjunction with the ``total_investment_transactions`` response
        body field to fetch all available investment transactions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.investments_transactions_get(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInvestmentsWithRawResponse:
        return self._with_raw_response


class InvestmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def investments_holdings_get(
        self,
        body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvestmentsHoldingsGetResponse, RawError]:
        """The ``/investments/holdings/get`` endpoint allows developers to receive user-authorized stock position data
        for ``investment``-type accounts.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/investments/holdings/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[InvestmentsHoldingsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def investments_transactions_get(
        self,
        body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvestmentsTransactionsGetResponse, RawError]:
        """The ``/investments/transactions/get`` endpoint allows developers to retrieve user-authorized transaction data
        for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated.
        Manipulate the count and offset parameters in conjunction with the ``total_investment_transactions`` response
        body field to fetch all available investment transactions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/investments/transactions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[InvestmentsTransactionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInvestmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def investments_holdings_get(
        self,
        body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvestmentsHoldingsGetResponse, RawError]:
        """The ``/investments/holdings/get`` endpoint allows developers to receive user-authorized stock position data
        for ``investment``-type accounts.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/investments/holdings/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[InvestmentsHoldingsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def investments_transactions_get(
        self,
        body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InvestmentsTransactionsGetResponse, RawError]:
        """The ``/investments/transactions/get`` endpoint allows developers to retrieve user-authorized transaction data
        for investment accounts.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift.

        Due to the potentially large number of investment transactions associated with an Item, results are paginated.
        Manipulate the count and offset parameters in conjunction with the ``total_investment_transactions`` response
        body field to fetch all available investment transactions.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/investments/transactions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[InvestmentsTransactionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
