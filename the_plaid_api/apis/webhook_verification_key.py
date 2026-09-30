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
from ..models.webhook_verification_key_get_request import (
    WebhookVerificationKeyGetRequest,
    WebhookVerificationKeyGetRequestDict,
)
from ..models.webhook_verification_key_get_response import WebhookVerificationKeyGetResponse
from ..server.server import Server


class WebhookVerificationKey:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhookVerificationKeyWithRawResponse(client, server, auth)

    def webhook_verification_key_get(
        self,
        body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookVerificationKeyGetResponse:
        """Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity
        of any incoming webhooks to your application. A message signature is included in the ``Plaid-Verification``
        header.

        The ``/webhook_verification_key/get`` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.webhook_verification_key_get(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> WebhookVerificationKeyWithRawResponse:
        return self._with_raw_response


class AsyncWebhookVerificationKey:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhookVerificationKeyWithRawResponse(client, server, auth)

    async def webhook_verification_key_get(
        self,
        body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookVerificationKeyGetResponse:
        """Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity
        of any incoming webhooks to your application. A message signature is included in the ``Plaid-Verification``
        header.

        The ``/webhook_verification_key/get`` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.webhook_verification_key_get(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWebhookVerificationKeyWithRawResponse:
        return self._with_raw_response


class WebhookVerificationKeyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def webhook_verification_key_get(
        self,
        body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookVerificationKeyGetResponse, RawError]:
        """Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity
        of any incoming webhooks to your application. A message signature is included in the ``Plaid-Verification``
        header.

        The ``/webhook_verification_key/get`` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/webhook_verification_key/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[WebhookVerificationKeyGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWebhookVerificationKeyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def webhook_verification_key_get(
        self,
        body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookVerificationKeyGetResponse, RawError]:
        """Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity
        of any incoming webhooks to your application. A message signature is included in the ``Plaid-Verification``
        header.

        The ``/webhook_verification_key/get`` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/webhook_verification_key/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[WebhookVerificationKeyGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
