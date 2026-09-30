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
from ..models.transfer_authorization_create_request import (
    TransferAuthorizationCreateRequest,
    TransferAuthorizationCreateRequestDict,
)
from ..models.transfer_authorization_create_response import TransferAuthorizationCreateResponse
from ..models.transfer_cancel_request import TransferCancelRequest, TransferCancelRequestDict
from ..models.transfer_cancel_response import TransferCancelResponse
from ..models.transfer_create_request import TransferCreateRequest, TransferCreateRequestDict
from ..models.transfer_create_response import TransferCreateResponse
from ..models.transfer_event_list_request import TransferEventListRequest, TransferEventListRequestDict
from ..models.transfer_event_list_response import TransferEventListResponse
from ..models.transfer_event_sync_request import TransferEventSyncRequest, TransferEventSyncRequestDict
from ..models.transfer_event_sync_response import TransferEventSyncResponse
from ..models.transfer_get_request import TransferGetRequest, TransferGetRequestDict
from ..models.transfer_get_response import TransferGetResponse
from ..models.transfer_list_request import TransferListRequest, TransferListRequestDict
from ..models.transfer_list_response import TransferListResponse
from ..server.server import Server


class TransferApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransferApiWithRawResponse(client, server, auth)

    def transfer_authorization_create(
        self,
        body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferAuthorizationCreateResponse:
        """Use the ``/transfer/authorization/create`` endpoint to determine transfer failure risk.

        In Plaid's sandbox environment the decisions will be returned as follows:

          - To approve a transfer, make an authorization request with an ``amount`` less than the available balance in
                the account.

          - To decline a transfer with the rationale code ``NSF``, the available balance on the account must be less
                than the authorization ``amount``. See `Create Sandbox test data
                <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code ``RISK``, the available balance on the account must be exactly
                $0. See `Create Sandbox test data <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to
                customize data in Sandbox.

          - To permit a transfer with the rationale code ``MANUALLY_VERIFIED_ITEM``, create an Item in Link through the
                `Same Day Micro-deposits flow
                <https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits>`__.

          - To permit a transfer with the rationale code ``LOGIN_REQUIRED``, `reset the login for an Item
                <https://plaid.com/docs/sandbox/#item_login_required>`__.

        All username/password combinations other than the ones listed above will result in a decision of permitted and
        rationale code ``ERROR``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_authorization_create(body, request_options=request_options).unwrap()

    def transfer_cancel(
        self,
        body: TransferCancelRequest | TransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferCancelResponse:
        """Use the ``/transfer/cancel`` endpoint to cancel a transfer. A transfer is eligible for cancelation if the
        ``cancellable`` property returned by ``/transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_cancel(body, request_options=request_options).unwrap()

    def transfer_create(
        self,
        body: TransferCreateRequest | TransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferCreateResponse:
        """Use the ``/transfer/create`` endpoint to initiate a new transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_create(body, request_options=request_options).unwrap()

    def transfer_event_list(
        self,
        body: TransferEventListRequest | TransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferEventListResponse:
        """Use the ``/transfer/event/list`` endpoint to get a list of transfer events based on specified filter
        criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_event_list(body, request_options=request_options).unwrap()

    def transfer_event_sync(
        self,
        body: TransferEventSyncRequest | TransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferEventSyncResponse:
        """``/transfer/event/sync`` allows you to request up to the next 25 transfer events that happened after a
        specific ``event_id``. Use the ``/transfer/event/sync`` endpoint to guarantee you have seen all transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_event_sync(body, request_options=request_options).unwrap()

    def transfer_get(
        self, body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferGetResponse:
        """The ``/transfer/get`` fetches information about the transfer corresponding to the given ``transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_get(body, request_options=request_options).unwrap()

    def transfer_list(
        self,
        body: TransferListRequest | TransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferListResponse:
        """Use the ``/transfer/list`` endpoint to see a list of all your transfers and their statuses. Results are
        paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.transfer_list(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TransferApiWithRawResponse:
        return self._with_raw_response


class AsyncTransferApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransferApiWithRawResponse(client, server, auth)

    async def transfer_authorization_create(
        self,
        body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferAuthorizationCreateResponse:
        """Use the ``/transfer/authorization/create`` endpoint to determine transfer failure risk.

        In Plaid's sandbox environment the decisions will be returned as follows:

          - To approve a transfer, make an authorization request with an ``amount`` less than the available balance in
                the account.

          - To decline a transfer with the rationale code ``NSF``, the available balance on the account must be less
                than the authorization ``amount``. See `Create Sandbox test data
                <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code ``RISK``, the available balance on the account must be exactly
                $0. See `Create Sandbox test data <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to
                customize data in Sandbox.

          - To permit a transfer with the rationale code ``MANUALLY_VERIFIED_ITEM``, create an Item in Link through the
                `Same Day Micro-deposits flow
                <https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits>`__.

          - To permit a transfer with the rationale code ``LOGIN_REQUIRED``, `reset the login for an Item
                <https://plaid.com/docs/sandbox/#item_login_required>`__.

        All username/password combinations other than the ones listed above will result in a decision of permitted and
        rationale code ``ERROR``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.transfer_authorization_create(body, request_options=request_options)
        ).unwrap()

    async def transfer_cancel(
        self,
        body: TransferCancelRequest | TransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferCancelResponse:
        """Use the ``/transfer/cancel`` endpoint to cancel a transfer. A transfer is eligible for cancelation if the
        ``cancellable`` property returned by ``/transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_cancel(body, request_options=request_options)).unwrap()

    async def transfer_create(
        self,
        body: TransferCreateRequest | TransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferCreateResponse:
        """Use the ``/transfer/create`` endpoint to initiate a new transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_create(body, request_options=request_options)).unwrap()

    async def transfer_event_list(
        self,
        body: TransferEventListRequest | TransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferEventListResponse:
        """Use the ``/transfer/event/list`` endpoint to get a list of transfer events based on specified filter
        criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_event_list(body, request_options=request_options)).unwrap()

    async def transfer_event_sync(
        self,
        body: TransferEventSyncRequest | TransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferEventSyncResponse:
        """``/transfer/event/sync`` allows you to request up to the next 25 transfer events that happened after a
        specific ``event_id``. Use the ``/transfer/event/sync`` endpoint to guarantee you have seen all transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_event_sync(body, request_options=request_options)).unwrap()

    async def transfer_get(
        self, body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransferGetResponse:
        """The ``/transfer/get`` fetches information about the transfer corresponding to the given ``transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_get(body, request_options=request_options)).unwrap()

    async def transfer_list(
        self,
        body: TransferListRequest | TransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransferListResponse:
        """Use the ``/transfer/list`` endpoint to see a list of all your transfers and their statuses. Results are
        paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.transfer_list(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransferApiWithRawResponse:
        return self._with_raw_response


class TransferApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def transfer_authorization_create(
        self,
        body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferAuthorizationCreateResponse, RawError]:
        """Use the ``/transfer/authorization/create`` endpoint to determine transfer failure risk.

        In Plaid's sandbox environment the decisions will be returned as follows:

          - To approve a transfer, make an authorization request with an ``amount`` less than the available balance in
                the account.

          - To decline a transfer with the rationale code ``NSF``, the available balance on the account must be less
                than the authorization ``amount``. See `Create Sandbox test data
                <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code ``RISK``, the available balance on the account must be exactly
                $0. See `Create Sandbox test data <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to
                customize data in Sandbox.

          - To permit a transfer with the rationale code ``MANUALLY_VERIFIED_ITEM``, create an Item in Link through the
                `Same Day Micro-deposits flow
                <https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits>`__.

          - To permit a transfer with the rationale code ``LOGIN_REQUIRED``, `reset the login for an Item
                <https://plaid.com/docs/sandbox/#item_login_required>`__.

        All username/password combinations other than the ones listed above will result in a decision of permitted and
        rationale code ``ERROR``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/authorization/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferAuthorizationCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_cancel(
        self,
        body: TransferCancelRequest | TransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferCancelResponse, RawError]:
        """Use the ``/transfer/cancel`` endpoint to cancel a transfer. A transfer is eligible for cancelation if the
        ``cancellable`` property returned by ``/transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferCancelRequest | TransferCancelRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferCancelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_create(
        self,
        body: TransferCreateRequest | TransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferCreateResponse, RawError]:
        """Use the ``/transfer/create`` endpoint to initiate a new transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferCreateRequest | TransferCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_event_list(
        self,
        body: TransferEventListRequest | TransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferEventListResponse, RawError]:
        """Use the ``/transfer/event/list`` endpoint to get a list of transfer events based on specified filter
        criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/event/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferEventListRequest | TransferEventListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferEventListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_event_sync(
        self,
        body: TransferEventSyncRequest | TransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferEventSyncResponse, RawError]:
        """``/transfer/event/sync`` allows you to request up to the next 25 transfer events that happened after a
        specific ``event_id``. Use the ``/transfer/event/sync`` endpoint to guarantee you have seen all transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/event/sync"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferEventSyncRequest | TransferEventSyncRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferEventSyncResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_get(
        self, body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferGetResponse, RawError]:
        """The ``/transfer/get`` fetches information about the transfer corresponding to the given ``transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferGetRequest | TransferGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def transfer_list(
        self,
        body: TransferListRequest | TransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferListResponse, RawError]:
        """Use the ``/transfer/list`` endpoint to see a list of all your transfers and their statuses. Results are
        paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferListRequest | TransferListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[TransferListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTransferApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def transfer_authorization_create(
        self,
        body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferAuthorizationCreateResponse, RawError]:
        """Use the ``/transfer/authorization/create`` endpoint to determine transfer failure risk.

        In Plaid's sandbox environment the decisions will be returned as follows:

          - To approve a transfer, make an authorization request with an ``amount`` less than the available balance in
                the account.

          - To decline a transfer with the rationale code ``NSF``, the available balance on the account must be less
                than the authorization ``amount``. See `Create Sandbox test data
                <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to customize data in Sandbox.

          - To decline a transfer with the rationale code ``RISK``, the available balance on the account must be exactly
                $0. See `Create Sandbox test data <https://plaid.com/docs/sandbox/user-custom/>`__ for details on how to
                customize data in Sandbox.

          - To permit a transfer with the rationale code ``MANUALLY_VERIFIED_ITEM``, create an Item in Link through the
                `Same Day Micro-deposits flow
                <https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits>`__.

          - To permit a transfer with the rationale code ``LOGIN_REQUIRED``, `reset the login for an Item
                <https://plaid.com/docs/sandbox/#item_login_required>`__.

        All username/password combinations other than the ones listed above will result in a decision of permitted and
        rationale code ``ERROR``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/authorization/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferAuthorizationCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_cancel(
        self,
        body: TransferCancelRequest | TransferCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferCancelResponse, RawError]:
        """Use the ``/transfer/cancel`` endpoint to cancel a transfer. A transfer is eligible for cancelation if the
        ``cancellable`` property returned by ``/transfer/get`` is ``true``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferCancelRequest | TransferCancelRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferCancelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_create(
        self,
        body: TransferCreateRequest | TransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferCreateResponse, RawError]:
        """Use the ``/transfer/create`` endpoint to initiate a new transfer.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferCreateRequest | TransferCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_event_list(
        self,
        body: TransferEventListRequest | TransferEventListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferEventListResponse, RawError]:
        """Use the ``/transfer/event/list`` endpoint to get a list of transfer events based on specified filter
        criteria.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/event/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferEventListRequest | TransferEventListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferEventListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_event_sync(
        self,
        body: TransferEventSyncRequest | TransferEventSyncRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferEventSyncResponse, RawError]:
        """``/transfer/event/sync`` allows you to request up to the next 25 transfer events that happened after a
        specific ``event_id``. Use the ``/transfer/event/sync`` endpoint to guarantee you have seen all transfer events.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/event/sync"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferEventSyncRequest | TransferEventSyncRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferEventSyncResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_get(
        self, body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransferGetResponse, RawError]:
        """The ``/transfer/get`` fetches information about the transfer corresponding to the given ``transfer_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferGetRequest | TransferGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def transfer_list(
        self,
        body: TransferListRequest | TransferListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransferListResponse, RawError]:
        """Use the ``/transfer/list`` endpoint to see a list of all your transfers and their statuses. Results are
        paginated; use the ``count`` and ``offset`` query parameters to retrieve the desired transfers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/transfer/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TransferListRequest | TransferListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[TransferListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
