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
from ..models.transactions_get_request import TransactionsGetRequest, TransactionsGetRequestDict
from ..models.transactions_get_response import TransactionsGetResponse
from ..models.transactions_refresh_request import TransactionsRefreshRequest, TransactionsRefreshRequestDict
from ..models.transactions_refresh_response import TransactionsRefreshResponse
from ..server.server import Server


class Transactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransactionsWithRawResponse(client, server, auth)

    def transactions_get(
        self,
        body: TransactionsGetRequest | TransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionsGetResponse:
        """The ``/transactions/get`` endpoint allows developers to receive user-authorized transaction data for credit,
        depository, and some loan-type accounts (only those with account subtype ``student``; coverage may be limited).
        For transaction history from investments accounts, use the `Investments endpoint
        <https://plaid.com/docs/api/products#investments>`__ instead. Transaction data is standardized across financial
        institutions, and in many cases transactions are linked to a clean name, entity type, location, and category.
        Similarly, account data is standardized and returned with a clean name, number, balance, and other meta
        information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed
        transaction will no longer appear in ``/transactions/get``. For more details, see `Pending and posted
        transactions <https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions>`__.

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate
        the ``count`` and ``offset`` parameters in conjunction with the ``total_transactions`` response body field to
        fetch all available transactions.

        Data returned by ``/transactions/get`` will be the data available for the Item as of the most recent successful
        check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur
        less frequently, such as once a day, depending on the institution. An Item's
        ``status.transactions.last_successful_update`` field will show the timestamp of the most recent successful
        update. To force Plaid to check for new transactions, you can use the ``/transactions/refresh`` endpoint.

        Note that data may not be immediately available to ``/transactions/get``. Plaid will begin to prepare
        transactions data upon Item link, if Link was initialized with ``transactions``, or upon the first call to
        ``/transactions/get``, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the
        https://plaid.com/docs/api/webhooks#transactions-initial_update and
        https://plaid.com/docs/api/webhooks#transactions-historical_update webhooks. If no transaction history is ready
        when ``/transactions/get`` is called, it will return a ``PRODUCT_NOT_READY`` error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transactions_get(body, request_options=request_options).unwrap()

    def transactions_refresh(
        self,
        body: TransactionsRefreshRequest | TransactionsRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionsRefreshResponse:
        """``/transactions/refresh`` is an optional endpoint for users of the Transactions product. It initiates an
        on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in
        addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled
        Item. If changes to transactions are discovered after calling ``/transactions/refresh``, Plaid will fire a
        webhook: https://plaid.com/docs/api/webhooks#deleted-transactions-detected will be fired if any removed
        transactions are detected, and https://plaid.com/docs/api/webhooks#transactions-default_update will be fired if
        any new transactions are detected. New transactions can be fetched by calling ``/transactions/get``.

        Access to ``/transactions/refresh`` in Production is specific to certain pricing plans. If you cannot access
        ``/transactions/refresh`` in Production, `contact Sales <https://www.plaid.com/contact>`__ for assistance.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transactions_refresh(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        return self._with_raw_response


class AsyncTransactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransactionsWithRawResponse(client, server, auth)

    async def transactions_get(
        self,
        body: TransactionsGetRequest | TransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionsGetResponse:
        """The ``/transactions/get`` endpoint allows developers to receive user-authorized transaction data for credit,
        depository, and some loan-type accounts (only those with account subtype ``student``; coverage may be limited).
        For transaction history from investments accounts, use the `Investments endpoint
        <https://plaid.com/docs/api/products#investments>`__ instead. Transaction data is standardized across financial
        institutions, and in many cases transactions are linked to a clean name, entity type, location, and category.
        Similarly, account data is standardized and returned with a clean name, number, balance, and other meta
        information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed
        transaction will no longer appear in ``/transactions/get``. For more details, see `Pending and posted
        transactions <https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions>`__.

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate
        the ``count`` and ``offset`` parameters in conjunction with the ``total_transactions`` response body field to
        fetch all available transactions.

        Data returned by ``/transactions/get`` will be the data available for the Item as of the most recent successful
        check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur
        less frequently, such as once a day, depending on the institution. An Item's
        ``status.transactions.last_successful_update`` field will show the timestamp of the most recent successful
        update. To force Plaid to check for new transactions, you can use the ``/transactions/refresh`` endpoint.

        Note that data may not be immediately available to ``/transactions/get``. Plaid will begin to prepare
        transactions data upon Item link, if Link was initialized with ``transactions``, or upon the first call to
        ``/transactions/get``, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the
        https://plaid.com/docs/api/webhooks#transactions-initial_update and
        https://plaid.com/docs/api/webhooks#transactions-historical_update webhooks. If no transaction history is ready
        when ``/transactions/get`` is called, it will return a ``PRODUCT_NOT_READY`` error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transactions_get(body, request_options=request_options)).unwrap()

    async def transactions_refresh(
        self,
        body: TransactionsRefreshRequest | TransactionsRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionsRefreshResponse:
        """``/transactions/refresh`` is an optional endpoint for users of the Transactions product. It initiates an
        on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in
        addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled
        Item. If changes to transactions are discovered after calling ``/transactions/refresh``, Plaid will fire a
        webhook: https://plaid.com/docs/api/webhooks#deleted-transactions-detected will be fired if any removed
        transactions are detected, and https://plaid.com/docs/api/webhooks#transactions-default_update will be fired if
        any new transactions are detected. New transactions can be fetched by calling ``/transactions/get``.

        Access to ``/transactions/refresh`` in Production is specific to certain pricing plans. If you cannot access
        ``/transactions/refresh`` in Production, `contact Sales <https://www.plaid.com/contact>`__ for assistance.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transactions_refresh(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        return self._with_raw_response


class TransactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def transactions_get(
        self,
        body: TransactionsGetRequest | TransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionsGetResponse, RawError]:
        """The ``/transactions/get`` endpoint allows developers to receive user-authorized transaction data for credit,
        depository, and some loan-type accounts (only those with account subtype ``student``; coverage may be limited).
        For transaction history from investments accounts, use the `Investments endpoint
        <https://plaid.com/docs/api/products#investments>`__ instead. Transaction data is standardized across financial
        institutions, and in many cases transactions are linked to a clean name, entity type, location, and category.
        Similarly, account data is standardized and returned with a clean name, number, balance, and other meta
        information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed
        transaction will no longer appear in ``/transactions/get``. For more details, see `Pending and posted
        transactions <https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions>`__.

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate
        the ``count`` and ``offset`` parameters in conjunction with the ``total_transactions`` response body field to
        fetch all available transactions.

        Data returned by ``/transactions/get`` will be the data available for the Item as of the most recent successful
        check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur
        less frequently, such as once a day, depending on the institution. An Item's
        ``status.transactions.last_successful_update`` field will show the timestamp of the most recent successful
        update. To force Plaid to check for new transactions, you can use the ``/transactions/refresh`` endpoint.

        Note that data may not be immediately available to ``/transactions/get``. Plaid will begin to prepare
        transactions data upon Item link, if Link was initialized with ``transactions``, or upon the first call to
        ``/transactions/get``, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the
        https://plaid.com/docs/api/webhooks#transactions-initial_update and
        https://plaid.com/docs/api/webhooks#transactions-historical_update webhooks. If no transaction history is ready
        when ``/transactions/get`` is called, it will return a ``PRODUCT_NOT_READY`` error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transactions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionsGetRequest | TransactionsGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransactionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transactions_refresh(
        self,
        body: TransactionsRefreshRequest | TransactionsRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionsRefreshResponse, RawError]:
        """``/transactions/refresh`` is an optional endpoint for users of the Transactions product. It initiates an
        on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in
        addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled
        Item. If changes to transactions are discovered after calling ``/transactions/refresh``, Plaid will fire a
        webhook: https://plaid.com/docs/api/webhooks#deleted-transactions-detected will be fired if any removed
        transactions are detected, and https://plaid.com/docs/api/webhooks#transactions-default_update will be fired if
        any new transactions are detected. New transactions can be fetched by calling ``/transactions/get``.

        Access to ``/transactions/refresh`` in Production is specific to certain pricing plans. If you cannot access
        ``/transactions/refresh`` in Production, `contact Sales <https://www.plaid.com/contact>`__ for assistance.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transactions/refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionsRefreshRequest | TransactionsRefreshRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransactionsRefreshResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTransactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def transactions_get(
        self,
        body: TransactionsGetRequest | TransactionsGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionsGetResponse, RawError]:
        """The ``/transactions/get`` endpoint allows developers to receive user-authorized transaction data for credit,
        depository, and some loan-type accounts (only those with account subtype ``student``; coverage may be limited).
        For transaction history from investments accounts, use the `Investments endpoint
        <https://plaid.com/docs/api/products#investments>`__ instead. Transaction data is standardized across financial
        institutions, and in many cases transactions are linked to a clean name, entity type, location, and category.
        Similarly, account data is standardized and returned with a clean name, number, balance, and other meta
        information where available.

        Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and
        will not shift. Transactions are not immutable and can also be removed altogether by the institution; a removed
        transaction will no longer appear in ``/transactions/get``. For more details, see `Pending and posted
        transactions <https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions>`__.

        Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate
        the ``count`` and ``offset`` parameters in conjunction with the ``total_transactions`` response body field to
        fetch all available transactions.

        Data returned by ``/transactions/get`` will be the data available for the Item as of the most recent successful
        check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur
        less frequently, such as once a day, depending on the institution. An Item's
        ``status.transactions.last_successful_update`` field will show the timestamp of the most recent successful
        update. To force Plaid to check for new transactions, you can use the ``/transactions/refresh`` endpoint.

        Note that data may not be immediately available to ``/transactions/get``. Plaid will begin to prepare
        transactions data upon Item link, if Link was initialized with ``transactions``, or upon the first call to
        ``/transactions/get``, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the
        https://plaid.com/docs/api/webhooks#transactions-initial_update and
        https://plaid.com/docs/api/webhooks#transactions-historical_update webhooks. If no transaction history is ready
        when ``/transactions/get`` is called, it will return a ``PRODUCT_NOT_READY`` error.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transactions/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionsGetRequest | TransactionsGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransactionsGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transactions_refresh(
        self,
        body: TransactionsRefreshRequest | TransactionsRefreshRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionsRefreshResponse, RawError]:
        """``/transactions/refresh`` is an optional endpoint for users of the Transactions product. It initiates an
        on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in
        addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled
        Item. If changes to transactions are discovered after calling ``/transactions/refresh``, Plaid will fire a
        webhook: https://plaid.com/docs/api/webhooks#deleted-transactions-detected will be fired if any removed
        transactions are detected, and https://plaid.com/docs/api/webhooks#transactions-default_update will be fired if
        any new transactions are detected. New transactions can be fetched by calling ``/transactions/get``.

        Access to ``/transactions/refresh`` in Production is specific to certain pricing plans. If you cannot access
        ``/transactions/refresh`` in Production, `contact Sales <https://www.plaid.com/contact>`__ for assistance.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transactions/refresh"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransactionsRefreshRequest | TransactionsRefreshRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransactionsRefreshResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
