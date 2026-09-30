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
from ..models.item_access_token_invalidate_request import (
    ItemAccessTokenInvalidateRequest,
    ItemAccessTokenInvalidateRequestDict,
)
from ..models.item_access_token_invalidate_response import ItemAccessTokenInvalidateResponse
from ..models.item_application_list_request import ItemApplicationListRequest, ItemApplicationListRequestDict
from ..models.item_application_list_response import ItemApplicationListResponse
from ..models.item_application_scopes_update_request import (
    ItemApplicationScopesUpdateRequest,
    ItemApplicationScopesUpdateRequestDict,
)
from ..models.item_application_scopes_update_response import ItemApplicationScopesUpdateResponse
from ..models.item_get_request import ItemGetRequest, ItemGetRequestDict
from ..models.item_get_response import ItemGetResponse
from ..models.item_import_request import ItemImportRequest, ItemImportRequestDict
from ..models.item_import_response import ItemImportResponse
from ..models.item_public_token_create_request import ItemPublicTokenCreateRequest, ItemPublicTokenCreateRequestDict
from ..models.item_public_token_create_response import ItemPublicTokenCreateResponse
from ..models.item_public_token_exchange_request import (
    ItemPublicTokenExchangeRequest,
    ItemPublicTokenExchangeRequestDict,
)
from ..models.item_public_token_exchange_response import ItemPublicTokenExchangeResponse
from ..models.item_remove_request import ItemRemoveRequest, ItemRemoveRequestDict
from ..models.item_remove_response import ItemRemoveResponse
from ..models.item_webhook_update_request import ItemWebhookUpdateRequest, ItemWebhookUpdateRequestDict
from ..models.item_webhook_update_response import ItemWebhookUpdateResponse
from ..server.server import Server


class ItemApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ItemApiWithRawResponse(client, server, auth)

    def item_access_token_invalidate(
        self,
        body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemAccessTokenInvalidateResponse:
        """By default, the ``access_token`` associated with an Item does not expire and should be stored in a
        persistent, secure manner.

        You can use the ``/item/access_token/invalidate`` endpoint to rotate the ``access_token`` associated with an
        Item. The endpoint returns a new ``access_token`` and immediately invalidates the previous ``access_token``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_access_token_invalidate(body, request_options=request_options).unwrap()

    def item_application_list(
        self,
        body: ItemApplicationListRequest | ItemApplicationListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemApplicationListResponse:
        """List a user’s connected applications

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_application_list(body, request_options=request_options).unwrap()

    def item_application_scopes_update(
        self,
        body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemApplicationScopesUpdateResponse:
        """Enable consumers to update product access on selected accounts for an application.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_application_scopes_update(body, request_options=request_options).unwrap()

    def item_create_public_token(
        self,
        body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemPublicTokenCreateResponse:
        """Note: As of July 2020, the ``/item/public_token/create`` endpoint is deprecated. Instead, use
        ``/link/token/create`` with an ``access_token`` to create a Link token for use with `update mode
        <https://plaid.com/docs/link/update-mode>`__.

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public
        token with the ``/item/public_token/create`` endpoint and then initialize Link with that ``public_token``.

        A ``public_token`` is one-time use and expires after 30 minutes. You use a ``public_token`` to initialize Link
        in `update mode <https://plaid.com/docs/link/update-mode>`__ for a particular Item. You can generate a
        ``public_token`` for an Item even if you did not use Link to create the Item originally.

        The ``/item/public_token/create`` endpoint is **not** used to create your initial ``public_token``. If you have
        not already received an ``access_token`` for a specific Item, use Link to obtain your ``public_token`` instead.
        See the `Quickstart <https://plaid.com/docs/quickstart>`__ for more information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_create_public_token(body, request_options=request_options).unwrap()

    def item_get(
        self, body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemGetResponse:
        """Returns information about the status of an Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_get(body, request_options=request_options).unwrap()

    def item_import(
        self, body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemImportResponse:
        """``/item/import`` creates an Item via your Plaid Exchange Integration and returns an ``access_token``. As part
        of an ``/item/import`` request, you will include a User ID (``user_auth.user_id``) and Authentication Token
        (``user_auth.auth_token``) that enable data aggregation through your Plaid Exchange API endpoints. These
        authentication principals are to be chosen by you.

        Upon creating an Item via ``/item/import``, Plaid will automatically begin an extraction of that Item through
        the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native
        account ID for the account the user will switch their direct deposit to (``target_account_id``).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_import(body, request_options=request_options).unwrap()

    def item_public_token_exchange(
        self,
        body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemPublicTokenExchangeResponse:
        """Exchange a Link ``public_token`` for an API ``access_token``. Link hands off the ``public_token`` client-side
        via the ``onSuccess`` callback once a user has successfully created an Item. The ``public_token`` is ephemeral
        and expires after 30 minutes.

        The response also includes an ``item_id`` that should be stored with the ``access_token``. The ``item_id`` is
        used to identify an Item in a webhook. The ``item_id`` can also be retrieved by making an ``/item/get`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_public_token_exchange(body, request_options=request_options).unwrap()

    def item_remove(
        self, body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemRemoveResponse:
        """The ``/item/remove`` endpoint allows you to remove an Item. Once removed, the ``access_token`` associated
        with the Item is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an ``/item/remove`` request will not decrement your live
        credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via ``/item/remove`` may still show as an
        active connection in the institution's OAuth permission manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_remove(body, request_options=request_options).unwrap()

    def item_webhook_update(
        self,
        body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemWebhookUpdateResponse:
        """The POST ``/item/webhook/update`` allows you to update the webhook URL associated with an Item. This request
        triggers a https://plaid.com/docs/api/webhooks/#item-webhook-url-updated webhook to the newly specified webhook
        URL.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.item_webhook_update(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ItemApiWithRawResponse:
        return self._with_raw_response


class AsyncItemApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncItemApiWithRawResponse(client, server, auth)

    async def item_access_token_invalidate(
        self,
        body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemAccessTokenInvalidateResponse:
        """By default, the ``access_token`` associated with an Item does not expire and should be stored in a
        persistent, secure manner.

        You can use the ``/item/access_token/invalidate`` endpoint to rotate the ``access_token`` associated with an
        Item. The endpoint returns a new ``access_token`` and immediately invalidates the previous ``access_token``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.item_access_token_invalidate(body, request_options=request_options)
        ).unwrap()

    async def item_application_list(
        self,
        body: ItemApplicationListRequest | ItemApplicationListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemApplicationListResponse:
        """List a user’s connected applications

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_application_list(body, request_options=request_options)).unwrap()

    async def item_application_scopes_update(
        self,
        body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemApplicationScopesUpdateResponse:
        """Enable consumers to update product access on selected accounts for an application.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.item_application_scopes_update(body, request_options=request_options)
        ).unwrap()

    async def item_create_public_token(
        self,
        body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemPublicTokenCreateResponse:
        """Note: As of July 2020, the ``/item/public_token/create`` endpoint is deprecated. Instead, use
        ``/link/token/create`` with an ``access_token`` to create a Link token for use with `update mode
        <https://plaid.com/docs/link/update-mode>`__.

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public
        token with the ``/item/public_token/create`` endpoint and then initialize Link with that ``public_token``.

        A ``public_token`` is one-time use and expires after 30 minutes. You use a ``public_token`` to initialize Link
        in `update mode <https://plaid.com/docs/link/update-mode>`__ for a particular Item. You can generate a
        ``public_token`` for an Item even if you did not use Link to create the Item originally.

        The ``/item/public_token/create`` endpoint is **not** used to create your initial ``public_token``. If you have
        not already received an ``access_token`` for a specific Item, use Link to obtain your ``public_token`` instead.
        See the `Quickstart <https://plaid.com/docs/quickstart>`__ for more information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_create_public_token(body, request_options=request_options)).unwrap()

    async def item_get(
        self, body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemGetResponse:
        """Returns information about the status of an Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_get(body, request_options=request_options)).unwrap()

    async def item_import(
        self, body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemImportResponse:
        """``/item/import`` creates an Item via your Plaid Exchange Integration and returns an ``access_token``. As part
        of an ``/item/import`` request, you will include a User ID (``user_auth.user_id``) and Authentication Token
        (``user_auth.auth_token``) that enable data aggregation through your Plaid Exchange API endpoints. These
        authentication principals are to be chosen by you.

        Upon creating an Item via ``/item/import``, Plaid will automatically begin an extraction of that Item through
        the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native
        account ID for the account the user will switch their direct deposit to (``target_account_id``).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_import(body, request_options=request_options)).unwrap()

    async def item_public_token_exchange(
        self,
        body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemPublicTokenExchangeResponse:
        """Exchange a Link ``public_token`` for an API ``access_token``. Link hands off the ``public_token`` client-side
        via the ``onSuccess`` callback once a user has successfully created an Item. The ``public_token`` is ephemeral
        and expires after 30 minutes.

        The response also includes an ``item_id`` that should be stored with the ``access_token``. The ``item_id`` is
        used to identify an Item in a webhook. The ``item_id`` can also be retrieved by making an ``/item/get`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.item_public_token_exchange(body, request_options=request_options)
        ).unwrap()

    async def item_remove(
        self, body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ItemRemoveResponse:
        """The ``/item/remove`` endpoint allows you to remove an Item. Once removed, the ``access_token`` associated
        with the Item is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an ``/item/remove`` request will not decrement your live
        credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via ``/item/remove`` may still show as an
        active connection in the institution's OAuth permission manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_remove(body, request_options=request_options)).unwrap()

    async def item_webhook_update(
        self,
        body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemWebhookUpdateResponse:
        """The POST ``/item/webhook/update`` allows you to update the webhook URL associated with an Item. This request
        triggers a https://plaid.com/docs/api/webhooks/#item-webhook-url-updated webhook to the newly specified webhook
        URL.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.item_webhook_update(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncItemApiWithRawResponse:
        return self._with_raw_response


class ItemApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def item_access_token_invalidate(
        self,
        body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemAccessTokenInvalidateResponse, RawError]:
        """By default, the ``access_token`` associated with an Item does not expire and should be stored in a
        persistent, secure manner.

        You can use the ``/item/access_token/invalidate`` endpoint to rotate the ``access_token`` associated with an
        Item. The endpoint returns a new ``access_token`` and immediately invalidates the previous ``access_token``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/access_token/invalidate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemAccessTokenInvalidateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_application_list(
        self,
        body: ItemApplicationListRequest | ItemApplicationListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemApplicationListResponse, RawError]:
        """List a user’s connected applications

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/application/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemApplicationListRequest | ItemApplicationListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemApplicationListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_application_scopes_update(
        self,
        body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemApplicationScopesUpdateResponse, RawError]:
        """Enable consumers to update product access on selected accounts for an application.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/application/scopes/update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemApplicationScopesUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_create_public_token(
        self,
        body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemPublicTokenCreateResponse, RawError]:
        """Note: As of July 2020, the ``/item/public_token/create`` endpoint is deprecated. Instead, use
        ``/link/token/create`` with an ``access_token`` to create a Link token for use with `update mode
        <https://plaid.com/docs/link/update-mode>`__.

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public
        token with the ``/item/public_token/create`` endpoint and then initialize Link with that ``public_token``.

        A ``public_token`` is one-time use and expires after 30 minutes. You use a ``public_token`` to initialize Link
        in `update mode <https://plaid.com/docs/link/update-mode>`__ for a particular Item. You can generate a
        ``public_token`` for an Item even if you did not use Link to create the Item originally.

        The ``/item/public_token/create`` endpoint is **not** used to create your initial ``public_token``. If you have
        not already received an ``access_token`` for a specific Item, use Link to obtain your ``public_token`` instead.
        See the `Quickstart <https://plaid.com/docs/quickstart>`__ for more information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/public_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemPublicTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_get(
        self, body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemGetResponse, RawError]:
        """Returns information about the status of an Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemGetRequest | ItemGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_import(
        self, body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemImportResponse, RawError]:
        """``/item/import`` creates an Item via your Plaid Exchange Integration and returns an ``access_token``. As part
        of an ``/item/import`` request, you will include a User ID (``user_auth.user_id``) and Authentication Token
        (``user_auth.auth_token``) that enable data aggregation through your Plaid Exchange API endpoints. These
        authentication principals are to be chosen by you.

        Upon creating an Item via ``/item/import``, Plaid will automatically begin an extraction of that Item through
        the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native
        account ID for the account the user will switch their direct deposit to (``target_account_id``).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/import"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemImportRequest | ItemImportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemImportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_public_token_exchange(
        self,
        body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemPublicTokenExchangeResponse, RawError]:
        """Exchange a Link ``public_token`` for an API ``access_token``. Link hands off the ``public_token`` client-side
        via the ``onSuccess`` callback once a user has successfully created an Item. The ``public_token`` is ephemeral
        and expires after 30 minutes.

        The response also includes an ``item_id`` that should be stored with the ``access_token``. The ``item_id`` is
        used to identify an Item in a webhook. The ``item_id`` can also be retrieved by making an ``/item/get`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/public_token/exchange"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemPublicTokenExchangeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_remove(
        self, body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemRemoveResponse, RawError]:
        """The ``/item/remove`` endpoint allows you to remove an Item. Once removed, the ``access_token`` associated
        with the Item is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an ``/item/remove`` request will not decrement your live
        credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via ``/item/remove`` may still show as an
        active connection in the institution's OAuth permission manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/remove"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemRemoveRequest | ItemRemoveRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemRemoveResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def item_webhook_update(
        self,
        body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemWebhookUpdateResponse, RawError]:
        """The POST ``/item/webhook/update`` allows you to update the webhook URL associated with an Item. This request
        triggers a https://plaid.com/docs/api/webhooks/#item-webhook-url-updated webhook to the newly specified webhook
        URL.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/webhook/update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[ItemWebhookUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncItemApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def item_access_token_invalidate(
        self,
        body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemAccessTokenInvalidateResponse, RawError]:
        """By default, the ``access_token`` associated with an Item does not expire and should be stored in a
        persistent, secure manner.

        You can use the ``/item/access_token/invalidate`` endpoint to rotate the ``access_token`` associated with an
        Item. The endpoint returns a new ``access_token`` and immediately invalidates the previous ``access_token``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/access_token/invalidate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemAccessTokenInvalidateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_application_list(
        self,
        body: ItemApplicationListRequest | ItemApplicationListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemApplicationListResponse, RawError]:
        """List a user’s connected applications

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/application/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemApplicationListRequest | ItemApplicationListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemApplicationListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_application_scopes_update(
        self,
        body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemApplicationScopesUpdateResponse, RawError]:
        """Enable consumers to update product access on selected accounts for an application.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/application/scopes/update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemApplicationScopesUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_create_public_token(
        self,
        body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemPublicTokenCreateResponse, RawError]:
        """Note: As of July 2020, the ``/item/public_token/create`` endpoint is deprecated. Instead, use
        ``/link/token/create`` with an ``access_token`` to create a Link token for use with `update mode
        <https://plaid.com/docs/link/update-mode>`__.

        If you need your user to take action to restore or resolve an error associated with an Item, generate a public
        token with the ``/item/public_token/create`` endpoint and then initialize Link with that ``public_token``.

        A ``public_token`` is one-time use and expires after 30 minutes. You use a ``public_token`` to initialize Link
        in `update mode <https://plaid.com/docs/link/update-mode>`__ for a particular Item. You can generate a
        ``public_token`` for an Item even if you did not use Link to create the Item originally.

        The ``/item/public_token/create`` endpoint is **not** used to create your initial ``public_token``. If you have
        not already received an ``access_token`` for a specific Item, use Link to obtain your ``public_token`` instead.
        See the `Quickstart <https://plaid.com/docs/quickstart>`__ for more information.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/public_token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemPublicTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_get(
        self, body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemGetResponse, RawError]:
        """Returns information about the status of an Item.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemGetRequest | ItemGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_import(
        self, body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemImportResponse, RawError]:
        """``/item/import`` creates an Item via your Plaid Exchange Integration and returns an ``access_token``. As part
        of an ``/item/import`` request, you will include a User ID (``user_auth.user_id``) and Authentication Token
        (``user_auth.auth_token``) that enable data aggregation through your Plaid Exchange API endpoints. These
        authentication principals are to be chosen by you.

        Upon creating an Item via ``/item/import``, Plaid will automatically begin an extraction of that Item through
        the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native
        account ID for the account the user will switch their direct deposit to (``target_account_id``).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/import"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemImportRequest | ItemImportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemImportResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_public_token_exchange(
        self,
        body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemPublicTokenExchangeResponse, RawError]:
        """Exchange a Link ``public_token`` for an API ``access_token``. Link hands off the ``public_token`` client-side
        via the ``onSuccess`` callback once a user has successfully created an Item. The ``public_token`` is ephemeral
        and expires after 30 minutes.

        The response also includes an ``item_id`` that should be stored with the ``access_token``. The ``item_id`` is
        used to identify an Item in a webhook. The ``item_id`` can also be retrieved by making an ``/item/get`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/public_token/exchange"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemPublicTokenExchangeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_remove(
        self, body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ItemRemoveResponse, RawError]:
        """The ``/item/remove`` endpoint allows you to remove an Item. Once removed, the ``access_token`` associated
        with the Item is no longer valid and cannot be used to access any data that was associated with the Item.

        Note that in the Development environment, issuing an ``/item/remove`` request will not decrement your live
        credential count. To increase your credential account in Development, contact Support.

        Also note that for certain OAuth-based institutions, an Item removed via ``/item/remove`` may still show as an
        active connection in the institution's OAuth permission manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/remove"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemRemoveRequest | ItemRemoveRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemRemoveResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def item_webhook_update(
        self,
        body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemWebhookUpdateResponse, RawError]:
        """The POST ``/item/webhook/update`` allows you to update the webhook URL associated with an Item. This request
        triggers a https://plaid.com/docs/api/webhooks/#item-webhook-url-updated webhook to the newly specified webhook
        URL.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/item/webhook/update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[ItemWebhookUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
