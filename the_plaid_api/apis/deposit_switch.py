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
from ..models.deposit_switch_alt_create_request import DepositSwitchAltCreateRequest, DepositSwitchAltCreateRequestDict
from ..models.deposit_switch_alt_create_response import DepositSwitchAltCreateResponse
from ..models.deposit_switch_create_request import DepositSwitchCreateRequest, DepositSwitchCreateRequestDict
from ..models.deposit_switch_create_response import DepositSwitchCreateResponse
from ..models.deposit_switch_get_request import DepositSwitchGetRequest, DepositSwitchGetRequestDict
from ..models.deposit_switch_get_response import DepositSwitchGetResponse
from ..models.deposit_switch_token_create_request import (
    DepositSwitchTokenCreateRequest,
    DepositSwitchTokenCreateRequestDict,
)
from ..models.deposit_switch_token_create_response import DepositSwitchTokenCreateResponse
from ..server.server import Server


class DepositSwitch:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DepositSwitchWithRawResponse(client, server, auth)

    def deposit_switch_alt_create(
        self,
        body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchAltCreateResponse:
        """This endpoint provides an alternative to ``/deposit_switch/create`` for customers who have not yet fully
        integrated with Plaid Exchange. Like ``/deposit_switch/create``, it creates a deposit switch entity that will be
        persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deposit_switch_alt_create(body, request_options=request_options).unwrap()

    def deposit_switch_create(
        self,
        body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchCreateResponse:
        """This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deposit_switch_create(body, request_options=request_options).unwrap()

    def deposit_switch_get(
        self,
        body: DepositSwitchGetRequest | DepositSwitchGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchGetResponse:
        """This endpoint returns information related to how the user has configured their payroll allocation and the
        state of the switch. You can use this information to build logic related to the user's direct deposit allocation
        preferences.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deposit_switch_get(body, request_options=request_options).unwrap()

    def deposit_switch_token_create(
        self,
        body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchTokenCreateResponse:
        """In order for the end user to take action, you will need to create a public token representing the deposit
        switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deposit_switch_token_create(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DepositSwitchWithRawResponse:
        return self._with_raw_response


class AsyncDepositSwitch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDepositSwitchWithRawResponse(client, server, auth)

    async def deposit_switch_alt_create(
        self,
        body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchAltCreateResponse:
        """This endpoint provides an alternative to ``/deposit_switch/create`` for customers who have not yet fully
        integrated with Plaid Exchange. Like ``/deposit_switch/create``, it creates a deposit switch entity that will be
        persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.deposit_switch_alt_create(body, request_options=request_options)).unwrap()

    async def deposit_switch_create(
        self,
        body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchCreateResponse:
        """This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.deposit_switch_create(body, request_options=request_options)).unwrap()

    async def deposit_switch_get(
        self,
        body: DepositSwitchGetRequest | DepositSwitchGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchGetResponse:
        """This endpoint returns information related to how the user has configured their payroll allocation and the
        state of the switch. You can use this information to build logic related to the user's direct deposit allocation
        preferences.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.deposit_switch_get(body, request_options=request_options)).unwrap()

    async def deposit_switch_token_create(
        self,
        body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DepositSwitchTokenCreateResponse:
        """In order for the end user to take action, you will need to create a public token representing the deposit
        switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deposit_switch_token_create(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDepositSwitchWithRawResponse:
        return self._with_raw_response


class DepositSwitchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def deposit_switch_alt_create(
        self,
        body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchAltCreateResponse, RawError]:
        """This endpoint provides an alternative to ``/deposit_switch/create`` for customers who have not yet fully
        integrated with Plaid Exchange. Like ``/deposit_switch/create``, it creates a deposit switch entity that will be
        persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/alt/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[DepositSwitchAltCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deposit_switch_create(
        self,
        body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchCreateResponse, RawError]:
        """This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchCreateRequest | DepositSwitchCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[DepositSwitchCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deposit_switch_get(
        self,
        body: DepositSwitchGetRequest | DepositSwitchGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchGetResponse, RawError]:
        """This endpoint returns information related to how the user has configured their payroll allocation and the
        state of the switch. You can use this information to build logic related to the user's direct deposit allocation
        preferences.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchGetRequest | DepositSwitchGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[DepositSwitchGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deposit_switch_token_create(
        self,
        body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchTokenCreateResponse, RawError]:
        """In order for the end user to take action, you will need to create a public token representing the deposit
        switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[DepositSwitchTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDepositSwitchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def deposit_switch_alt_create(
        self,
        body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchAltCreateResponse, RawError]:
        """This endpoint provides an alternative to ``/deposit_switch/create`` for customers who have not yet fully
        integrated with Plaid Exchange. Like ``/deposit_switch/create``, it creates a deposit switch entity that will be
        persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/alt/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[DepositSwitchAltCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deposit_switch_create(
        self,
        body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchCreateResponse, RawError]:
        """This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchCreateRequest | DepositSwitchCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[DepositSwitchCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deposit_switch_get(
        self,
        body: DepositSwitchGetRequest | DepositSwitchGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchGetResponse, RawError]:
        """This endpoint returns information related to how the user has configured their payroll allocation and the
        state of the switch. You can use this information to build logic related to the user's direct deposit allocation
        preferences.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchGetRequest | DepositSwitchGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[DepositSwitchGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deposit_switch_token_create(
        self,
        body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DepositSwitchTokenCreateResponse, RawError]:
        """In order for the end user to take action, you will need to create a public token representing the deposit
        switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/deposit_switch/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[DepositSwitchTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
