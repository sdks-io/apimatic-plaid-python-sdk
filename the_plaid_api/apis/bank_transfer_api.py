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
from ..models.bank_transfer_balance_get_request import BankTransferBalanceGetRequest, BankTransferBalanceGetRequestDict
from ..models.bank_transfer_balance_get_response import BankTransferBalanceGetResponse
from ..models.bank_transfer_cancel_request import BankTransferCancelRequest, BankTransferCancelRequestDict
from ..models.bank_transfer_cancel_response import BankTransferCancelResponse
from ..models.bank_transfer_create_request import BankTransferCreateRequest, BankTransferCreateRequestDict
from ..models.bank_transfer_create_response import BankTransferCreateResponse
from ..models.bank_transfer_event_list_request import BankTransferEventListRequest, BankTransferEventListRequestDict
from ..models.bank_transfer_event_list_response import BankTransferEventListResponse
from ..models.bank_transfer_event_sync_request import BankTransferEventSyncRequest, BankTransferEventSyncRequestDict
from ..models.bank_transfer_event_sync_response import BankTransferEventSyncResponse
from ..models.bank_transfer_get_request import BankTransferGetRequest, BankTransferGetRequestDict
from ..models.bank_transfer_get_response import BankTransferGetResponse
from ..models.bank_transfer_list_request import BankTransferListRequest, BankTransferListRequestDict
from ..models.bank_transfer_list_response import BankTransferListResponse
from ..models.bank_transfer_migrate_account_request import (
    BankTransferMigrateAccountRequest,
    BankTransferMigrateAccountRequestDict,
)
from ..models.bank_transfer_migrate_account_response import BankTransferMigrateAccountResponse
from ..models.bank_transfer_sweep_get_request import BankTransferSweepGetRequest, BankTransferSweepGetRequestDict
from ..models.bank_transfer_sweep_get_response import BankTransferSweepGetResponse
from ..models.bank_transfer_sweep_list_request import BankTransferSweepListRequest, BankTransferSweepListRequestDict
from ..models.bank_transfer_sweep_list_response import BankTransferSweepListResponse
from ..server.server import Server


class BankTransferApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BankTransferApiWithRawResponse(client, server, auth)

    def bank_transfer_balance_get(
        self,
        body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferBalanceGetResponse:
        """Use the ``/bank_transfer/balance/get`` endpoint to see the available balance in your bank transfer account.
        Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when
        they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is
        essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service
        configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform
        configuration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_balance_get(body, request_options=request_options).unwrap()

    def bank_transfer_cancel(
        self,
        body: BankTransferCancelRequest | BankTransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferCancelResponse:
        """Use the ``/bank_transfer/cancel`` endpoint to cancel a bank transfer. A transfer is eligible for cancelation
        if the ``cancellable`` property returned by ``/bank_transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_cancel(body, request_options=request_options).unwrap()

    def bank_transfer_create(
        self,
        body: BankTransferCreateRequest | BankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferCreateResponse:
        """Use the ``/bank_transfer/create`` endpoint to initiate a new bank transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_create(body, request_options=request_options).unwrap()

    def bank_transfer_event_list(
        self,
        body: BankTransferEventListRequest | BankTransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferEventListResponse:
        """Use the ``/bank_transfer/event/list`` endpoint to get a list of bank transfer events based on specified
        filter criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_event_list(body, request_options=request_options).unwrap()

    def bank_transfer_event_sync(
        self,
        body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferEventSyncResponse:
        """``/bank_transfer/event/sync`` allows you to request up to the next 25 bank transfer events that happened
        after a specific ``event_id``. Use the ``/bank_transfer/event/sync`` endpoint to guarantee you have seen all
        bank transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_event_sync(body, request_options=request_options).unwrap()

    def bank_transfer_get(
        self,
        body: BankTransferGetRequest | BankTransferGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferGetResponse:
        """The ``/bank_transfer/get`` fetches information about the bank transfer corresponding to the given
        ``bank_transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_get(body, request_options=request_options).unwrap()

    def bank_transfer_list(
        self,
        body: BankTransferListRequest | BankTransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferListResponse:
        """Use the ``/bank_transfer/list`` endpoint to see a list of all your bank transfers and their statuses. Results
        are paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired bank transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_list(body, request_options=request_options).unwrap()

    def bank_transfer_migrate_account(
        self,
        body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferMigrateAccountResponse:
        """As an alternative to adding Items via Link, you can also use the ``/bank_transfer/migrate_account`` endpoint
        to migrate known account and routing numbers to Plaid Items. Note that Items created in this way are not
        compatible with endpoints for other products, such as ``/accounts/balance/get``, and can only be used with Bank
        Transfer endpoints. If you require access to other endpoints, create the Item through Link instead. Access to
        ``/bank_transfer/migrate_account`` is not enabled by default; to obtain access, contact your Plaid Account
        Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_migrate_account(body, request_options=request_options).unwrap()

    def bank_transfer_sweep_get(
        self,
        body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferSweepGetResponse:
        """The ``/bank_transfer/sweep/get`` endpoint fetches information about the sweep corresponding to the given
        ``sweep_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_sweep_get(body, request_options=request_options).unwrap()

    def bank_transfer_sweep_list(
        self,
        body: BankTransferSweepListRequest | BankTransferSweepListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferSweepListResponse:
        """The ``/bank_transfer/sweep/list`` endpoint fetches information about the sweeps matching the given filters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bank_transfer_sweep_list(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BankTransferApiWithRawResponse:
        return self._with_raw_response


class AsyncBankTransferApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBankTransferApiWithRawResponse(client, server, auth)

    async def bank_transfer_balance_get(
        self,
        body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferBalanceGetResponse:
        """Use the ``/bank_transfer/balance/get`` endpoint to see the available balance in your bank transfer account.
        Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when
        they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is
        essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service
        configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform
        configuration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_balance_get(body, request_options=request_options)).unwrap()

    async def bank_transfer_cancel(
        self,
        body: BankTransferCancelRequest | BankTransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferCancelResponse:
        """Use the ``/bank_transfer/cancel`` endpoint to cancel a bank transfer. A transfer is eligible for cancelation
        if the ``cancellable`` property returned by ``/bank_transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_cancel(body, request_options=request_options)).unwrap()

    async def bank_transfer_create(
        self,
        body: BankTransferCreateRequest | BankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferCreateResponse:
        """Use the ``/bank_transfer/create`` endpoint to initiate a new bank transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_create(body, request_options=request_options)).unwrap()

    async def bank_transfer_event_list(
        self,
        body: BankTransferEventListRequest | BankTransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferEventListResponse:
        """Use the ``/bank_transfer/event/list`` endpoint to get a list of bank transfer events based on specified
        filter criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_event_list(body, request_options=request_options)).unwrap()

    async def bank_transfer_event_sync(
        self,
        body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferEventSyncResponse:
        """``/bank_transfer/event/sync`` allows you to request up to the next 25 bank transfer events that happened
        after a specific ``event_id``. Use the ``/bank_transfer/event/sync`` endpoint to guarantee you have seen all
        bank transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_event_sync(body, request_options=request_options)).unwrap()

    async def bank_transfer_get(
        self,
        body: BankTransferGetRequest | BankTransferGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferGetResponse:
        """The ``/bank_transfer/get`` fetches information about the bank transfer corresponding to the given
        ``bank_transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_get(body, request_options=request_options)).unwrap()

    async def bank_transfer_list(
        self,
        body: BankTransferListRequest | BankTransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferListResponse:
        """Use the ``/bank_transfer/list`` endpoint to see a list of all your bank transfers and their statuses. Results
        are paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired bank transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_list(body, request_options=request_options)).unwrap()

    async def bank_transfer_migrate_account(
        self,
        body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferMigrateAccountResponse:
        """As an alternative to adding Items via Link, you can also use the ``/bank_transfer/migrate_account`` endpoint
        to migrate known account and routing numbers to Plaid Items. Note that Items created in this way are not
        compatible with endpoints for other products, such as ``/accounts/balance/get``, and can only be used with Bank
        Transfer endpoints. If you require access to other endpoints, create the Item through Link instead. Access to
        ``/bank_transfer/migrate_account`` is not enabled by default; to obtain access, contact your Plaid Account
        Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bank_transfer_migrate_account(body, request_options=request_options)
        ).unwrap()

    async def bank_transfer_sweep_get(
        self,
        body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferSweepGetResponse:
        """The ``/bank_transfer/sweep/get`` endpoint fetches information about the sweep corresponding to the given
        ``sweep_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_sweep_get(body, request_options=request_options)).unwrap()

    async def bank_transfer_sweep_list(
        self,
        body: BankTransferSweepListRequest | BankTransferSweepListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BankTransferSweepListResponse:
        """The ``/bank_transfer/sweep/list`` endpoint fetches information about the sweeps matching the given filters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bank_transfer_sweep_list(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBankTransferApiWithRawResponse:
        return self._with_raw_response


class BankTransferApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bank_transfer_balance_get(
        self,
        body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferBalanceGetResponse, RawError]:
        """Use the ``/bank_transfer/balance/get`` endpoint to see the available balance in your bank transfer account.
        Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when
        they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is
        essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service
        configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform
        configuration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferBalanceGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_cancel(
        self,
        body: BankTransferCancelRequest | BankTransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferCancelResponse, RawError]:
        """Use the ``/bank_transfer/cancel`` endpoint to cancel a bank transfer. A transfer is eligible for cancelation
        if the ``cancellable`` property returned by ``/bank_transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferCancelRequest | BankTransferCancelRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferCancelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_create(
        self,
        body: BankTransferCreateRequest | BankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferCreateResponse, RawError]:
        """Use the ``/bank_transfer/create`` endpoint to initiate a new bank transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferCreateRequest | BankTransferCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_event_list(
        self,
        body: BankTransferEventListRequest | BankTransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferEventListResponse, RawError]:
        """Use the ``/bank_transfer/event/list`` endpoint to get a list of bank transfer events based on specified
        filter criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/event/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferEventListRequest | BankTransferEventListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferEventListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_event_sync(
        self,
        body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferEventSyncResponse, RawError]:
        """``/bank_transfer/event/sync`` allows you to request up to the next 25 bank transfer events that happened
        after a specific ``event_id``. Use the ``/bank_transfer/event/sync`` endpoint to guarantee you have seen all
        bank transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/event/sync"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferEventSyncRequest | BankTransferEventSyncRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferEventSyncResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_get(
        self,
        body: BankTransferGetRequest | BankTransferGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferGetResponse, RawError]:
        """The ``/bank_transfer/get`` fetches information about the bank transfer corresponding to the given
        ``bank_transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferGetRequest | BankTransferGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_list(
        self,
        body: BankTransferListRequest | BankTransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferListResponse, RawError]:
        """Use the ``/bank_transfer/list`` endpoint to see a list of all your bank transfers and their statuses. Results
        are paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired bank transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferListRequest | BankTransferListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_migrate_account(
        self,
        body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferMigrateAccountResponse, RawError]:
        """As an alternative to adding Items via Link, you can also use the ``/bank_transfer/migrate_account`` endpoint
        to migrate known account and routing numbers to Plaid Items. Note that Items created in this way are not
        compatible with endpoints for other products, such as ``/accounts/balance/get``, and can only be used with Bank
        Transfer endpoints. If you require access to other endpoints, create the Item through Link instead. Access to
        ``/bank_transfer/migrate_account`` is not enabled by default; to obtain access, contact your Plaid Account
        Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/migrate_account"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferMigrateAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_sweep_get(
        self,
        body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferSweepGetResponse, RawError]:
        """The ``/bank_transfer/sweep/get`` endpoint fetches information about the sweep corresponding to the given
        ``sweep_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/sweep/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferSweepGetRequest | BankTransferSweepGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferSweepGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bank_transfer_sweep_list(
        self,
        body: BankTransferSweepListRequest | BankTransferSweepListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferSweepListResponse, RawError]:
        """The ``/bank_transfer/sweep/list`` endpoint fetches information about the sweeps matching the given filters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/sweep/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferSweepListRequest | BankTransferSweepListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[BankTransferSweepListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBankTransferApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bank_transfer_balance_get(
        self,
        body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferBalanceGetResponse, RawError]:
        """Use the ``/bank_transfer/balance/get`` endpoint to see the available balance in your bank transfer account.
        Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when
        they are created.

        The transactable balance shows the amount in your account that you are able to use for transfers, and is
        essentially your available balance minus your minimum balance.

        Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service
        configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform
        configuration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferBalanceGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_cancel(
        self,
        body: BankTransferCancelRequest | BankTransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferCancelResponse, RawError]:
        """Use the ``/bank_transfer/cancel`` endpoint to cancel a bank transfer. A transfer is eligible for cancelation
        if the ``cancellable`` property returned by ``/bank_transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferCancelRequest | BankTransferCancelRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferCancelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_create(
        self,
        body: BankTransferCreateRequest | BankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferCreateResponse, RawError]:
        """Use the ``/bank_transfer/create`` endpoint to initiate a new bank transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferCreateRequest | BankTransferCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_event_list(
        self,
        body: BankTransferEventListRequest | BankTransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferEventListResponse, RawError]:
        """Use the ``/bank_transfer/event/list`` endpoint to get a list of bank transfer events based on specified
        filter criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/event/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferEventListRequest | BankTransferEventListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferEventListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_event_sync(
        self,
        body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferEventSyncResponse, RawError]:
        """``/bank_transfer/event/sync`` allows you to request up to the next 25 bank transfer events that happened
        after a specific ``event_id``. Use the ``/bank_transfer/event/sync`` endpoint to guarantee you have seen all
        bank transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/event/sync"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferEventSyncRequest | BankTransferEventSyncRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferEventSyncResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_get(
        self,
        body: BankTransferGetRequest | BankTransferGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferGetResponse, RawError]:
        """The ``/bank_transfer/get`` fetches information about the bank transfer corresponding to the given
        ``bank_transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferGetRequest | BankTransferGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_list(
        self,
        body: BankTransferListRequest | BankTransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferListResponse, RawError]:
        """Use the ``/bank_transfer/list`` endpoint to see a list of all your bank transfers and their statuses. Results
        are paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired bank transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferListRequest | BankTransferListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_migrate_account(
        self,
        body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferMigrateAccountResponse, RawError]:
        """As an alternative to adding Items via Link, you can also use the ``/bank_transfer/migrate_account`` endpoint
        to migrate known account and routing numbers to Plaid Items. Note that Items created in this way are not
        compatible with endpoints for other products, such as ``/accounts/balance/get``, and can only be used with Bank
        Transfer endpoints. If you require access to other endpoints, create the Item through Link instead. Access to
        ``/bank_transfer/migrate_account`` is not enabled by default; to obtain access, contact your Plaid Account
        Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/migrate_account"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferMigrateAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_sweep_get(
        self,
        body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferSweepGetResponse, RawError]:
        """The ``/bank_transfer/sweep/get`` endpoint fetches information about the sweep corresponding to the given
        ``sweep_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/sweep/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferSweepGetRequest | BankTransferSweepGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferSweepGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bank_transfer_sweep_list(
        self,
        body: BankTransferSweepListRequest | BankTransferSweepListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BankTransferSweepListResponse, RawError]:
        """The ``/bank_transfer/sweep/list`` endpoint fetches information about the sweeps matching the given filters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/bank_transfer/sweep/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BankTransferSweepListRequest | BankTransferSweepListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[BankTransferSweepListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
