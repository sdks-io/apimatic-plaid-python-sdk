from __future__ import annotations

from typing import Any
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
from ..models.sandbox_bank_transfer_fire_webhook_request import (
    SandboxBankTransferFireWebhookRequest,
    SandboxBankTransferFireWebhookRequestDict,
)
from ..models.sandbox_bank_transfer_fire_webhook_response import SandboxBankTransferFireWebhookResponse
from ..models.sandbox_bank_transfer_simulate_request import (
    SandboxBankTransferSimulateRequest,
    SandboxBankTransferSimulateRequestDict,
)
from ..models.sandbox_bank_transfer_simulate_response import SandboxBankTransferSimulateResponse
from ..models.sandbox_income_fire_webhook_request import (
    SandboxIncomeFireWebhookRequest,
    SandboxIncomeFireWebhookRequestDict,
)
from ..models.sandbox_income_fire_webhook_response import SandboxIncomeFireWebhookResponse
from ..models.sandbox_item_fire_webhook_request import SandboxItemFireWebhookRequest, SandboxItemFireWebhookRequestDict
from ..models.sandbox_item_fire_webhook_response import SandboxItemFireWebhookResponse
from ..models.sandbox_item_reset_login_request import SandboxItemResetLoginRequest, SandboxItemResetLoginRequestDict
from ..models.sandbox_item_reset_login_response import SandboxItemResetLoginResponse
from ..models.sandbox_item_set_verification_status_request import (
    SandboxItemSetVerificationStatusRequest,
    SandboxItemSetVerificationStatusRequestDict,
)
from ..models.sandbox_item_set_verification_status_response import SandboxItemSetVerificationStatusResponse
from ..models.sandbox_oauth_select_accounts_request import (
    SandboxOauthSelectAccountsRequest,
    SandboxOauthSelectAccountsRequestDict,
)
from ..models.sandbox_processor_token_create_request import (
    SandboxProcessorTokenCreateRequest,
    SandboxProcessorTokenCreateRequestDict,
)
from ..models.sandbox_processor_token_create_response import SandboxProcessorTokenCreateResponse
from ..models.sandbox_public_token_create_request import (
    SandboxPublicTokenCreateRequest,
    SandboxPublicTokenCreateRequestDict,
)
from ..models.sandbox_public_token_create_response import SandboxPublicTokenCreateResponse
from ..models.sandbox_transfer_simulate_request import (
    SandboxTransferSimulateRequest,
    SandboxTransferSimulateRequestDict,
)
from ..models.sandbox_transfer_simulate_response import SandboxTransferSimulateResponse
from ..server.server import Server


class Sandbox:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SandboxWithRawResponse(client, server, auth)

    def sandbox_bank_transfer_fire_webhook(
        self,
        body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxBankTransferFireWebhookResponse:
        """Use the ``/sandbox/bank_transfer/fire_webhook`` endpoint to manually trigger a Bank Transfers webhook in the
        Sandbox environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_bank_transfer_fire_webhook(
            body, request_options=request_options
        ).unwrap()

    def sandbox_bank_transfer_simulate(
        self,
        body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxBankTransferSimulateResponse:
        """Use the ``/sandbox/bank_transfer/simulate`` endpoint to simulate a bank transfer event in the Sandbox
        environment. Note that while an event will be simulated and will appear when using endpoints such as
        ``/bank_transfer/event/sync`` or ``/bank_transfer/event/list``, no transactions will actually take place and
        funds will not move between accounts, even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_bank_transfer_simulate(body, request_options=request_options).unwrap()

    def sandbox_income_fire_webhook(
        self,
        body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxIncomeFireWebhookResponse:
        """Use the ``/sandbox/income/fire_webhook`` endpoint to manually trigger an Income webhook in the Sandbox
        environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_income_fire_webhook(body, request_options=request_options).unwrap()

    def sandbox_item_fire_webhook(
        self,
        body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemFireWebhookResponse:
        """The ``/sandbox/item/fire_webhook`` endpoint is used to test that code correctly handles webhooks. Calling
        this endpoint triggers a Transactions ``DEFAULT_UPDATE`` webhook to be fired for a given Sandbox Item. If the
        Item does not support Transactions, a ``SANDBOX_PRODUCT_NOT_ENABLED`` error will result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_item_fire_webhook(body, request_options=request_options).unwrap()

    def sandbox_item_reset_login(
        self,
        body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemResetLoginResponse:
        """``/sandbox/item/reset_login/`` forces an Item into an ``ITEM_LOGIN_REQUIRED`` state in order to simulate an
        Item whose login is no longer valid. This makes it easy to test Link's `update mode
        <https://plaid.com/docs/link/update-mode>`__ flow in the Sandbox environment. After calling
        ``/sandbox/item/reset_login``, You can then use Plaid Link update mode to restore the Item to a good state. An
        ``ITEM_LOGIN_REQUIRED`` webhook will also be fired after a call to this endpoint, if one is associated with the
        Item.

        In the Sandbox, Items will transition to an ``ITEM_LOGIN_REQUIRED`` error state automatically after 30 days,
        even if this endpoint is not called.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_item_reset_login(body, request_options=request_options).unwrap()

    def sandbox_item_set_verification_status(
        self,
        body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemSetVerificationStatusResponse:
        """The ``/sandbox/item/set_verification_status`` endpoint can be used to change the verification status of an
        Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your
        account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your
        status, contact your account manager or `submit a product access Support ticket
        <https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access>`__.

        For more information on testing Automated Micro-deposits in Sandbox, see `Auth full coverage testing
        <https://plaid.com/docs/auth/coverage/testing#>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_item_set_verification_status(
            body, request_options=request_options
        ).unwrap()

    def sandbox_oauth_select_accounts(
        self,
        body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Save the selected accounts when connecting to the Platypus Oauth institution

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_oauth_select_accounts(body, request_options=request_options).unwrap()

    def sandbox_processor_token_create(
        self,
        body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxProcessorTokenCreateResponse:
        """Use the ``/sandbox/processor_token/create`` endpoint to create a valid ``processor_token`` for an arbitrary
        institution ID and test credentials. The created ``processor_token`` corresponds to a new Sandbox Item. You can
        then use this ``processor_token`` with the ``/processor/`` API endpoints in Sandbox. You can also use
        ``/sandbox/processor_token/create`` with the https://plaid.com/docs/sandbox/user-custom to generate a test
        account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_processor_token_create(body, request_options=request_options).unwrap()

    def sandbox_public_token_create(
        self,
        body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxPublicTokenCreateResponse:
        """Use the ``/sandbox/public_token/create`` endpoint to create a valid ``public_token`` for an arbitrary
        institution ID, initial products, and test credentials. The created ``public_token`` maps to a new Sandbox Item.
        You can then call ``/item/public_token/exchange`` to exchange the ``public_token`` for an ``access_token`` and
        perform all API actions. ``/sandbox/public_token/create`` can also be used with the
        https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_public_token_create(body, request_options=request_options).unwrap()

    def sandbox_transfer_simulate(
        self,
        body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxTransferSimulateResponse:
        """Use the ``/sandbox/transfer/simulate`` endpoint to simulate a transfer event in the Sandbox environment. Note
        that while an event will be simulated and will appear when using endpoints such as ``/transfer/event/sync`` or
        ``/transfer/event/list``, no transactions will actually take place and funds will not move between accounts,
        even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.sandbox_transfer_simulate(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SandboxWithRawResponse:
        return self._with_raw_response


class AsyncSandbox:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSandboxWithRawResponse(client, server, auth)

    async def sandbox_bank_transfer_fire_webhook(
        self,
        body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxBankTransferFireWebhookResponse:
        """Use the ``/sandbox/bank_transfer/fire_webhook`` endpoint to manually trigger a Bank Transfers webhook in the
        Sandbox environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_bank_transfer_fire_webhook(body, request_options=request_options)
        ).unwrap()

    async def sandbox_bank_transfer_simulate(
        self,
        body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxBankTransferSimulateResponse:
        """Use the ``/sandbox/bank_transfer/simulate`` endpoint to simulate a bank transfer event in the Sandbox
        environment. Note that while an event will be simulated and will appear when using endpoints such as
        ``/bank_transfer/event/sync`` or ``/bank_transfer/event/list``, no transactions will actually take place and
        funds will not move between accounts, even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_bank_transfer_simulate(body, request_options=request_options)
        ).unwrap()

    async def sandbox_income_fire_webhook(
        self,
        body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxIncomeFireWebhookResponse:
        """Use the ``/sandbox/income/fire_webhook`` endpoint to manually trigger an Income webhook in the Sandbox
        environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_income_fire_webhook(body, request_options=request_options)
        ).unwrap()

    async def sandbox_item_fire_webhook(
        self,
        body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemFireWebhookResponse:
        """The ``/sandbox/item/fire_webhook`` endpoint is used to test that code correctly handles webhooks. Calling
        this endpoint triggers a Transactions ``DEFAULT_UPDATE`` webhook to be fired for a given Sandbox Item. If the
        Item does not support Transactions, a ``SANDBOX_PRODUCT_NOT_ENABLED`` error will result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.sandbox_item_fire_webhook(body, request_options=request_options)).unwrap()

    async def sandbox_item_reset_login(
        self,
        body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemResetLoginResponse:
        """``/sandbox/item/reset_login/`` forces an Item into an ``ITEM_LOGIN_REQUIRED`` state in order to simulate an
        Item whose login is no longer valid. This makes it easy to test Link's `update mode
        <https://plaid.com/docs/link/update-mode>`__ flow in the Sandbox environment. After calling
        ``/sandbox/item/reset_login``, You can then use Plaid Link update mode to restore the Item to a good state. An
        ``ITEM_LOGIN_REQUIRED`` webhook will also be fired after a call to this endpoint, if one is associated with the
        Item.

        In the Sandbox, Items will transition to an ``ITEM_LOGIN_REQUIRED`` error state automatically after 30 days,
        even if this endpoint is not called.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.sandbox_item_reset_login(body, request_options=request_options)).unwrap()

    async def sandbox_item_set_verification_status(
        self,
        body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxItemSetVerificationStatusResponse:
        """The ``/sandbox/item/set_verification_status`` endpoint can be used to change the verification status of an
        Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your
        account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your
        status, contact your account manager or `submit a product access Support ticket
        <https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access>`__.

        For more information on testing Automated Micro-deposits in Sandbox, see `Auth full coverage testing
        <https://plaid.com/docs/auth/coverage/testing#>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_item_set_verification_status(body, request_options=request_options)
        ).unwrap()

    async def sandbox_oauth_select_accounts(
        self,
        body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Save the selected accounts when connecting to the Platypus Oauth institution

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_oauth_select_accounts(body, request_options=request_options)
        ).unwrap()

    async def sandbox_processor_token_create(
        self,
        body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxProcessorTokenCreateResponse:
        """Use the ``/sandbox/processor_token/create`` endpoint to create a valid ``processor_token`` for an arbitrary
        institution ID and test credentials. The created ``processor_token`` corresponds to a new Sandbox Item. You can
        then use this ``processor_token`` with the ``/processor/`` API endpoints in Sandbox. You can also use
        ``/sandbox/processor_token/create`` with the https://plaid.com/docs/sandbox/user-custom to generate a test
        account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_processor_token_create(body, request_options=request_options)
        ).unwrap()

    async def sandbox_public_token_create(
        self,
        body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxPublicTokenCreateResponse:
        """Use the ``/sandbox/public_token/create`` endpoint to create a valid ``public_token`` for an arbitrary
        institution ID, initial products, and test credentials. The created ``public_token`` maps to a new Sandbox Item.
        You can then call ``/item/public_token/exchange`` to exchange the ``public_token`` for an ``access_token`` and
        perform all API actions. ``/sandbox/public_token/create`` can also be used with the
        https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.sandbox_public_token_create(body, request_options=request_options)
        ).unwrap()

    async def sandbox_transfer_simulate(
        self,
        body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SandboxTransferSimulateResponse:
        """Use the ``/sandbox/transfer/simulate`` endpoint to simulate a transfer event in the Sandbox environment. Note
        that while an event will be simulated and will appear when using endpoints such as ``/transfer/event/sync`` or
        ``/transfer/event/list``, no transactions will actually take place and funds will not move between accounts,
        even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.sandbox_transfer_simulate(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSandboxWithRawResponse:
        return self._with_raw_response


class SandboxWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sandbox_bank_transfer_fire_webhook(
        self,
        body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxBankTransferFireWebhookResponse, RawError]:
        """Use the ``/sandbox/bank_transfer/fire_webhook`` endpoint to manually trigger a Bank Transfers webhook in the
        Sandbox environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/bank_transfer/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxBankTransferFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_bank_transfer_simulate(
        self,
        body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxBankTransferSimulateResponse, RawError]:
        """Use the ``/sandbox/bank_transfer/simulate`` endpoint to simulate a bank transfer event in the Sandbox
        environment. Note that while an event will be simulated and will appear when using endpoints such as
        ``/bank_transfer/event/sync`` or ``/bank_transfer/event/list``, no transactions will actually take place and
        funds will not move between accounts, even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/bank_transfer/simulate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxBankTransferSimulateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_income_fire_webhook(
        self,
        body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxIncomeFireWebhookResponse, RawError]:
        """Use the ``/sandbox/income/fire_webhook`` endpoint to manually trigger an Income webhook in the Sandbox
        environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/income/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxIncomeFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_item_fire_webhook(
        self,
        body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemFireWebhookResponse, RawError]:
        """The ``/sandbox/item/fire_webhook`` endpoint is used to test that code correctly handles webhooks. Calling
        this endpoint triggers a Transactions ``DEFAULT_UPDATE`` webhook to be fired for a given Sandbox Item. If the
        Item does not support Transactions, a ``SANDBOX_PRODUCT_NOT_ENABLED`` error will result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxItemFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_item_reset_login(
        self,
        body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemResetLoginResponse, RawError]:
        """``/sandbox/item/reset_login/`` forces an Item into an ``ITEM_LOGIN_REQUIRED`` state in order to simulate an
        Item whose login is no longer valid. This makes it easy to test Link's `update mode
        <https://plaid.com/docs/link/update-mode>`__ flow in the Sandbox environment. After calling
        ``/sandbox/item/reset_login``, You can then use Plaid Link update mode to restore the Item to a good state. An
        ``ITEM_LOGIN_REQUIRED`` webhook will also be fired after a call to this endpoint, if one is associated with the
        Item.

        In the Sandbox, Items will transition to an ``ITEM_LOGIN_REQUIRED`` error state automatically after 30 days,
        even if this endpoint is not called.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/reset_login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxItemResetLoginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_item_set_verification_status(
        self,
        body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemSetVerificationStatusResponse, RawError]:
        """The ``/sandbox/item/set_verification_status`` endpoint can be used to change the verification status of an
        Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your
        account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your
        status, contact your account manager or `submit a product access Support ticket
        <https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access>`__.

        For more information on testing Automated Micro-deposits in Sandbox, see `Auth full coverage testing
        <https://plaid.com/docs/auth/coverage/testing#>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/set_verification_status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxItemSetVerificationStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_oauth_select_accounts(
        self,
        body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Save the selected accounts when connecting to the Platypus Oauth institution

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/oauth/select_accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_processor_token_create(
        self,
        body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxProcessorTokenCreateResponse, RawError]:
        """Use the ``/sandbox/processor_token/create`` endpoint to create a valid ``processor_token`` for an arbitrary
        institution ID and test credentials. The created ``processor_token`` corresponds to a new Sandbox Item. You can
        then use this ``processor_token`` with the ``/processor/`` API endpoints in Sandbox. You can also use
        ``/sandbox/processor_token/create`` with the https://plaid.com/docs/sandbox/user-custom to generate a test
        account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/processor_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_public_token_create(
        self,
        body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxPublicTokenCreateResponse, RawError]:
        """Use the ``/sandbox/public_token/create`` endpoint to create a valid ``public_token`` for an arbitrary
        institution ID, initial products, and test credentials. The created ``public_token`` maps to a new Sandbox Item.
        You can then call ``/item/public_token/exchange`` to exchange the ``public_token`` for an ``access_token`` and
        perform all API actions. ``/sandbox/public_token/create`` can also be used with the
        https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/public_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxPublicTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def sandbox_transfer_simulate(
        self,
        body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxTransferSimulateResponse, RawError]:
        """Use the ``/sandbox/transfer/simulate`` endpoint to simulate a transfer event in the Sandbox environment. Note
        that while an event will be simulated and will appear when using endpoints such as ``/transfer/event/sync`` or
        ``/transfer/event/list``, no transactions will actually take place and funds will not move between accounts,
        even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/transfer/simulate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[SandboxTransferSimulateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSandboxWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sandbox_bank_transfer_fire_webhook(
        self,
        body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxBankTransferFireWebhookResponse, RawError]:
        """Use the ``/sandbox/bank_transfer/fire_webhook`` endpoint to manually trigger a Bank Transfers webhook in the
        Sandbox environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/bank_transfer/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxBankTransferFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_bank_transfer_simulate(
        self,
        body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxBankTransferSimulateResponse, RawError]:
        """Use the ``/sandbox/bank_transfer/simulate`` endpoint to simulate a bank transfer event in the Sandbox
        environment. Note that while an event will be simulated and will appear when using endpoints such as
        ``/bank_transfer/event/sync`` or ``/bank_transfer/event/list``, no transactions will actually take place and
        funds will not move between accounts, even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/bank_transfer/simulate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxBankTransferSimulateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_income_fire_webhook(
        self,
        body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxIncomeFireWebhookResponse, RawError]:
        """Use the ``/sandbox/income/fire_webhook`` endpoint to manually trigger an Income webhook in the Sandbox
        environment.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/income/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxIncomeFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_item_fire_webhook(
        self,
        body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemFireWebhookResponse, RawError]:
        """The ``/sandbox/item/fire_webhook`` endpoint is used to test that code correctly handles webhooks. Calling
        this endpoint triggers a Transactions ``DEFAULT_UPDATE`` webhook to be fired for a given Sandbox Item. If the
        Item does not support Transactions, a ``SANDBOX_PRODUCT_NOT_ENABLED`` error will result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/fire_webhook"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxItemFireWebhookResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_item_reset_login(
        self,
        body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemResetLoginResponse, RawError]:
        """``/sandbox/item/reset_login/`` forces an Item into an ``ITEM_LOGIN_REQUIRED`` state in order to simulate an
        Item whose login is no longer valid. This makes it easy to test Link's `update mode
        <https://plaid.com/docs/link/update-mode>`__ flow in the Sandbox environment. After calling
        ``/sandbox/item/reset_login``, You can then use Plaid Link update mode to restore the Item to a good state. An
        ``ITEM_LOGIN_REQUIRED`` webhook will also be fired after a call to this endpoint, if one is associated with the
        Item.

        In the Sandbox, Items will transition to an ``ITEM_LOGIN_REQUIRED`` error state automatically after 30 days,
        even if this endpoint is not called.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/reset_login"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxItemResetLoginResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_item_set_verification_status(
        self,
        body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxItemSetVerificationStatusResponse, RawError]:
        """The ``/sandbox/item/set_verification_status`` endpoint can be used to change the verification status of an
        Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

        Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your
        account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your
        status, contact your account manager or `submit a product access Support ticket
        <https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access>`__.

        For more information on testing Automated Micro-deposits in Sandbox, see `Auth full coverage testing
        <https://plaid.com/docs/auth/coverage/testing#>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/item/set_verification_status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxItemSetVerificationStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_oauth_select_accounts(
        self,
        body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Save the selected accounts when connecting to the Platypus Oauth institution

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/oauth/select_accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_processor_token_create(
        self,
        body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxProcessorTokenCreateResponse, RawError]:
        """Use the ``/sandbox/processor_token/create`` endpoint to create a valid ``processor_token`` for an arbitrary
        institution ID and test credentials. The created ``processor_token`` corresponds to a new Sandbox Item. You can
        then use this ``processor_token`` with the ``/processor/`` API endpoints in Sandbox. You can also use
        ``/sandbox/processor_token/create`` with the https://plaid.com/docs/sandbox/user-custom to generate a test
        account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/processor_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxProcessorTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_public_token_create(
        self,
        body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxPublicTokenCreateResponse, RawError]:
        """Use the ``/sandbox/public_token/create`` endpoint to create a valid ``public_token`` for an arbitrary
        institution ID, initial products, and test credentials. The created ``public_token`` maps to a new Sandbox Item.
        You can then call ``/item/public_token/exchange`` to exchange the ``public_token`` for an ``access_token`` and
        perform all API actions. ``/sandbox/public_token/create`` can also be used with the
        https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/public_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxPublicTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def sandbox_transfer_simulate(
        self,
        body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SandboxTransferSimulateResponse, RawError]:
        """Use the ``/sandbox/transfer/simulate`` endpoint to simulate a transfer event in the Sandbox environment. Note
        that while an event will be simulated and will appear when using endpoints such as ``/transfer/event/sync`` or
        ``/transfer/event/list``, no transactions will actually take place and funds will not move between accounts,
        even within the Sandbox.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sandbox/transfer/simulate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[SandboxTransferSimulateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
