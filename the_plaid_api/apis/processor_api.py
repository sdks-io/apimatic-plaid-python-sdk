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
from ..models.processor_apex_processor_token_create_request import (
    ProcessorApexProcessorTokenCreateRequest,
    ProcessorApexProcessorTokenCreateRequestDict,
)
from ..models.processor_auth_get_request import ProcessorAuthGetRequest, ProcessorAuthGetRequestDict
from ..models.processor_auth_get_response import ProcessorAuthGetResponse
from ..models.processor_balance_get_request import ProcessorBalanceGetRequest, ProcessorBalanceGetRequestDict
from ..models.processor_balance_get_response import ProcessorBalanceGetResponse
from ..models.processor_bank_transfer_create_request import (
    ProcessorBankTransferCreateRequest,
    ProcessorBankTransferCreateRequestDict,
)
from ..models.processor_bank_transfer_create_response import ProcessorBankTransferCreateResponse
from ..models.processor_identity_get_request import ProcessorIdentityGetRequest, ProcessorIdentityGetRequestDict
from ..models.processor_identity_get_response import ProcessorIdentityGetResponse
from ..models.processor_stripe_bank_account_token_create_request import (
    ProcessorStripeBankAccountTokenCreateRequest,
    ProcessorStripeBankAccountTokenCreateRequestDict,
)
from ..models.processor_stripe_bank_account_token_create_response import ProcessorStripeBankAccountTokenCreateResponse
from ..models.processor_token_create_request import ProcessorTokenCreateRequest, ProcessorTokenCreateRequestDict
from ..models.processor_token_create_response import ProcessorTokenCreateResponse
from ..server.server import Server


class ProcessorApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProcessorApiWithRawResponse(client, server, auth)

    def processor_apex_processor_token_create(
        self,
        body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorTokenCreateResponse:
        """Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_apex_processor_token_create(
            body, request_options=request_options
        ).unwrap()

    def processor_auth_get(
        self,
        body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorAuthGetResponse:
        """The ``/processor/auth/get`` endpoint returns the bank account and bank identification number (such as the
        routing number, for US accounts), for a checking or savings account that's associated with a given
        ``processor_token``. The endpoint also returns high-level account data and balances when available.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_auth_get(body, request_options=request_options).unwrap()

    def processor_balance_get(
        self,
        body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorBalanceGetResponse:
        """The ``/processor/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/processor/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached.

        Args:
            body: The ``/processor/balance/get`` endpoint returns the real-time balance for the account associated with
                a given ``processor_token``. The current balance is the total amount of funds in the account. The
                available balance is the current balance less any outstanding holds or debits that have not yet posted
                to the account. Note that not all institutions calculate the available balance. In the event that
                available balance is unavailable from the institution, Plaid will return an available balance value of
                ``null``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_balance_get(body, request_options=request_options).unwrap()

    def processor_bank_transfer_create(
        self,
        body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorBankTransferCreateResponse:
        """Use the ``/processor/bank_transfer/create`` endpoint to initiate a new bank transfer as a processor

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_bank_transfer_create(body, request_options=request_options).unwrap()

    def processor_identity_get(
        self,
        body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorIdentityGetResponse:
        """The ``/processor/identity/get`` endpoint allows you to retrieve various account holder information on file
        with the financial institution, including names, emails, phone numbers, and addresses.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_identity_get(body, request_options=request_options).unwrap()

    def processor_stripe_bank_account_token_create(
        self,
        body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorStripeBankAccountTokenCreateResponse:
        """Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed
        guide on integrating Stripe, see `Add Stripe to your app <https://plaid.com/docs/auth/partnerships/stripe/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_stripe_bank_account_token_create(
            body, request_options=request_options
        ).unwrap()

    def processor_token_create(
        self,
        body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorTokenCreateResponse:
        """Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that
        Stripe partnerships use bank account tokens instead; see ``/processor/stripe/bank_account_token/create`` for
        creating tokens for use with Stripe integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.processor_token_create(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ProcessorApiWithRawResponse:
        return self._with_raw_response


class AsyncProcessorApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProcessorApiWithRawResponse(client, server, auth)

    async def processor_apex_processor_token_create(
        self,
        body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorTokenCreateResponse:
        """Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.processor_apex_processor_token_create(body, request_options=request_options)
        ).unwrap()

    async def processor_auth_get(
        self,
        body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorAuthGetResponse:
        """The ``/processor/auth/get`` endpoint returns the bank account and bank identification number (such as the
        routing number, for US accounts), for a checking or savings account that's associated with a given
        ``processor_token``. The endpoint also returns high-level account data and balances when available.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.processor_auth_get(body, request_options=request_options)).unwrap()

    async def processor_balance_get(
        self,
        body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorBalanceGetResponse:
        """The ``/processor/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/processor/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached.

        Args:
            body: The ``/processor/balance/get`` endpoint returns the real-time balance for the account associated with
                a given ``processor_token``. The current balance is the total amount of funds in the account. The
                available balance is the current balance less any outstanding holds or debits that have not yet posted
                to the account. Note that not all institutions calculate the available balance. In the event that
                available balance is unavailable from the institution, Plaid will return an available balance value of
                ``null``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.processor_balance_get(body, request_options=request_options)).unwrap()

    async def processor_bank_transfer_create(
        self,
        body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorBankTransferCreateResponse:
        """Use the ``/processor/bank_transfer/create`` endpoint to initiate a new bank transfer as a processor

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.processor_bank_transfer_create(body, request_options=request_options)
        ).unwrap()

    async def processor_identity_get(
        self,
        body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorIdentityGetResponse:
        """The ``/processor/identity/get`` endpoint allows you to retrieve various account holder information on file
        with the financial institution, including names, emails, phone numbers, and addresses.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.processor_identity_get(body, request_options=request_options)).unwrap()

    async def processor_stripe_bank_account_token_create(
        self,
        body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorStripeBankAccountTokenCreateResponse:
        """Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed
        guide on integrating Stripe, see `Add Stripe to your app <https://plaid.com/docs/auth/partnerships/stripe/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.processor_stripe_bank_account_token_create(
                body, request_options=request_options
            )
        ).unwrap()

    async def processor_token_create(
        self,
        body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProcessorTokenCreateResponse:
        """Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that
        Stripe partnerships use bank account tokens instead; see ``/processor/stripe/bank_account_token/create`` for
        creating tokens for use with Stripe integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.processor_token_create(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncProcessorApiWithRawResponse:
        return self._with_raw_response


class ProcessorApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def processor_apex_processor_token_create(
        self,
        body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/apex/processor_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict](
                body
            ),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_auth_get(
        self,
        body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorAuthGetResponse, RawError]:
        """The ``/processor/auth/get`` endpoint returns the bank account and bank identification number (such as the
        routing number, for US accounts), for a checking or savings account that's associated with a given
        ``processor_token``. The endpoint also returns high-level account data and balances when available.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/auth/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorAuthGetRequest | ProcessorAuthGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorAuthGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_balance_get(
        self,
        body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorBalanceGetResponse, RawError]:
        """The ``/processor/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/processor/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached.

        Args:
            body: The ``/processor/balance/get`` endpoint returns the real-time balance for the account associated with
                a given ``processor_token``. The current balance is the total amount of funds in the account. The
                available balance is the current balance less any outstanding holds or debits that have not yet posted
                to the account. Note that not all institutions calculate the available balance. In the event that
                available balance is unavailable from the institution, Plaid will return an available balance value of
                ``null``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorBalanceGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_bank_transfer_create(
        self,
        body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorBankTransferCreateResponse, RawError]:
        """Use the ``/processor/bank_transfer/create`` endpoint to initiate a new bank transfer as a processor

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/bank_transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorBankTransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_identity_get(
        self,
        body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorIdentityGetResponse, RawError]:
        """The ``/processor/identity/get`` endpoint allows you to retrieve various account holder information on file
        with the financial institution, including names, emails, phone numbers, and addresses.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/identity/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorIdentityGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_stripe_bank_account_token_create(
        self,
        body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorStripeBankAccountTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed
        guide on integrating Stripe, see `Add Stripe to your app <https://plaid.com/docs/auth/partnerships/stripe/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/stripe/bank_account_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict
            ](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorStripeBankAccountTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def processor_token_create(
        self,
        body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that
        Stripe partnerships use bank account tokens instead; see ``/processor/stripe/bank_account_token/create`` for
        creating tokens for use with Stripe integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProcessorApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def processor_apex_processor_token_create(
        self,
        body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/apex/processor_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict](
                body
            ),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_auth_get(
        self,
        body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorAuthGetResponse, RawError]:
        """The ``/processor/auth/get`` endpoint returns the bank account and bank identification number (such as the
        routing number, for US accounts), for a checking or savings account that's associated with a given
        ``processor_token``. The endpoint also returns high-level account data and balances when available.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/auth/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorAuthGetRequest | ProcessorAuthGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorAuthGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_balance_get(
        self,
        body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorBalanceGetResponse, RawError]:
        """The ``/processor/balance/get`` endpoint returns the real-time balance for each of an Item's accounts. While
        other endpoints may return a balance object, only ``/processor/balance/get`` forces the available and current
        balance fields to be refreshed rather than cached.

        Args:
            body: The ``/processor/balance/get`` endpoint returns the real-time balance for the account associated with
                a given ``processor_token``. The current balance is the total amount of funds in the account. The
                available balance is the current balance less any outstanding holds or debits that have not yet posted
                to the account. Note that not all institutions calculate the available balance. In the event that
                available balance is unavailable from the institution, Plaid will return an available balance value of
                ``null``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/balance/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorBalanceGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_bank_transfer_create(
        self,
        body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorBankTransferCreateResponse, RawError]:
        """Use the ``/processor/bank_transfer/create`` endpoint to initiate a new bank transfer as a processor

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/bank_transfer/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorBankTransferCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_identity_get(
        self,
        body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorIdentityGetResponse, RawError]:
        """The ``/processor/identity/get`` endpoint allows you to retrieve various account holder information on file
        with the financial institution, including names, emails, phone numbers, and addresses.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/identity/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorIdentityGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_stripe_bank_account_token_create(
        self,
        body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorStripeBankAccountTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed
        guide on integrating Stripe, see `Add Stripe to your app <https://plaid.com/docs/auth/partnerships/stripe/>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/stripe/bank_account_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict
            ](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorStripeBankAccountTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def processor_token_create(
        self,
        body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProcessorTokenCreateResponse, RawError]:
        """Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that
        Stripe partnerships use bank account tokens instead; see ``/processor/stripe/bank_account_token/create`` for
        creating tokens for use with Stripe integrations.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/processor/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
