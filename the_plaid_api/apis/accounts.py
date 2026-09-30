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
from ..models.accounts_balance_get_request import AccountsBalanceGetRequest, AccountsBalanceGetRequestDict
from ..models.accounts_get_request import AccountsGetRequest, AccountsGetRequestDict
from ..models.accounts_get_response import AccountsGetResponse
from ..server.server import Server


class Accounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountsWithRawResponse(client, server, auth)

    def accounts_balance_get(
        self,
        body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountsGetResponse:
        """The ``/accounts/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/accounts/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added
        via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other
        product, ``balance`` itself is not a product that can be used to initialize Link.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.accounts_balance_get(body, request_options=request_options).unwrap()

    def accounts_get(
        self, body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountsGetResponse:
        """The ``/accounts/get`` endpoint can be used to retrieve information for any linked Item. Note that some
        information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are
        capable of carrying a balance.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a
        result, balances returned may not be up-to-date; for realtime balance information, use ``/accounts/balance/get``
        instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.accounts_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return self._with_raw_response


class AsyncAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountsWithRawResponse(client, server, auth)

    async def accounts_balance_get(
        self,
        body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountsGetResponse:
        """The ``/accounts/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/accounts/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added
        via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other
        product, ``balance`` itself is not a product that can be used to initialize Link.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.accounts_balance_get(body, request_options=request_options)).unwrap()

    async def accounts_get(
        self, body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountsGetResponse:
        """The ``/accounts/get`` endpoint can be used to retrieve information for any linked Item. Note that some
        information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are
        capable of carrying a balance.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a
        result, balances returned may not be up-to-date; for realtime balance information, use ``/accounts/balance/get``
        instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.accounts_get(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return self._with_raw_response


class AccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def accounts_balance_get(
        self,
        body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountsGetResponse, RawError]:
        """The ``/accounts/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/accounts/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added
        via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other
        product, ``balance`` itself is not a product that can be used to initialize Link.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/accounts/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountsBalanceGetRequest | AccountsBalanceGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[AccountsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def accounts_get(
        self, body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountsGetResponse, RawError]:
        """The ``/accounts/get`` endpoint can be used to retrieve information for any linked Item. Note that some
        information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are
        capable of carrying a balance.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a
        result, balances returned may not be up-to-date; for realtime balance information, use ``/accounts/balance/get``
        instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/accounts/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountsGetRequest | AccountsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[AccountsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def accounts_balance_get(
        self,
        body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountsGetResponse, RawError]:
        """The ``/accounts/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/accounts/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added
        via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other
        product, ``balance`` itself is not a product that can be used to initialize Link.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/accounts/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountsBalanceGetRequest | AccountsBalanceGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[AccountsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def accounts_get(
        self, body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountsGetResponse, RawError]:
        """The ``/accounts/get`` endpoint can be used to retrieve information for any linked Item. Note that some
        information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are
        capable of carrying a balance.

        This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a
        result, balances returned may not be up-to-date; for realtime balance information, use ``/accounts/balance/get``
        instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/accounts/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountsGetRequest | AccountsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[AccountsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
