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
from ..models.payment_initiation_payment_create_request import (
    PaymentInitiationPaymentCreateRequest,
    PaymentInitiationPaymentCreateRequestDict,
)
from ..models.payment_initiation_payment_create_response import PaymentInitiationPaymentCreateResponse
from ..models.payment_initiation_payment_get_request import (
    PaymentInitiationPaymentGetRequest,
    PaymentInitiationPaymentGetRequestDict,
)
from ..models.payment_initiation_payment_get_response import PaymentInitiationPaymentGetResponse
from ..models.payment_initiation_payment_list_request import (
    PaymentInitiationPaymentListRequest,
    PaymentInitiationPaymentListRequestDict,
)
from ..models.payment_initiation_payment_list_response import PaymentInitiationPaymentListResponse
from ..models.payment_initiation_payment_reverse_request import (
    PaymentInitiationPaymentReverseRequest,
    PaymentInitiationPaymentReverseRequestDict,
)
from ..models.payment_initiation_payment_reverse_response import PaymentInitiationPaymentReverseResponse
from ..models.payment_initiation_payment_token_create_request import (
    PaymentInitiationPaymentTokenCreateRequest,
    PaymentInitiationPaymentTokenCreateRequestDict,
)
from ..models.payment_initiation_payment_token_create_response import PaymentInitiationPaymentTokenCreateResponse
from ..models.payment_initiation_recipient_create_request import (
    PaymentInitiationRecipientCreateRequest,
    PaymentInitiationRecipientCreateRequestDict,
)
from ..models.payment_initiation_recipient_create_response import PaymentInitiationRecipientCreateResponse
from ..models.payment_initiation_recipient_get_request import (
    PaymentInitiationRecipientGetRequest,
    PaymentInitiationRecipientGetRequestDict,
)
from ..models.payment_initiation_recipient_get_response import PaymentInitiationRecipientGetResponse
from ..models.payment_initiation_recipient_list_request import (
    PaymentInitiationRecipientListRequest,
    PaymentInitiationRecipientListRequestDict,
)
from ..models.payment_initiation_recipient_list_response import PaymentInitiationRecipientListResponse
from ..server.server import Server


class PaymentInitiation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentInitiationWithRawResponse(client, server, auth)

    def create_payment_token(
        self,
        body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentTokenCreateResponse:
        """The ``/payment_initiation/payment/token/create`` endpoint has been deprecated. New Plaid customers will be
        unable to use this endpoint, and existing customers are encouraged to migrate to the newer, ``link_token``-based
        flow. The recommended flow is to provide the ``payment_id`` to ``/link/token/create``, which returns a
        ``link_token`` used to initialize Link.

        The ``/payment_initiation/payment/token/create`` is used to create a ``payment_token``, which can then be used
        in Link initialization to enter a payment initiation flow. You can only use a ``payment_token`` once. If this
        attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token.
        Creating a new payment token does not require end user input.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_payment_token(body, request_options=request_options).unwrap()

    def payment_initiation_payment_create(
        self,
        body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentCreateResponse:
        """After creating a payment recipient, you can use the ``/payment_initiation/payment/create`` endpoint to create
        a payment to that recipient. Payments can be one-time or standing order (recurring) and can be denominated in
        either EUR or GBP. If making domestic GBP-denominated payments, your recipient must have been created with BACS
        numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments
        will be sent via the Faster Payments network, but the payment network used will be determined by the
        institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA
        Credit Transfer will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK.
        Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or
        modify a standing order directly on their banking application or website, or by contacting the bank. Standing
        orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent
        Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the
        payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach
        the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in
        Production, contact your Plaid Account Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_payment_create(body, request_options=request_options).unwrap()

    def payment_initiation_payment_get(
        self,
        body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentGetResponse:
        """The ``/payment_initiation/payment/get`` endpoint can be used to check the status of a payment, as well as to
        receive basic information such as recipient and payment amount. In the case of standing orders, the
        ``/payment_initiation/payment/get`` endpoint will provide information about the status of the overall standing
        order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_payment_get(body, request_options=request_options).unwrap()

    def payment_initiation_payment_list(
        self,
        body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentListResponse:
        """The ``/payment_initiation/payment/list`` endpoint can be used to retrieve all created payments. By default,
        the 10 most recent payments are returned. You can request more payments and paginate through the results using
        the optional ``count`` and ``cursor`` parameters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_payment_list(body, request_options=request_options).unwrap()

    def payment_initiation_payment_reverse(
        self,
        body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentReverseResponse:
        """Reverse a previously initiated payment.

        A payment can only be reversed once and will be refunded to the original sender's account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_payment_reverse(
            body, request_options=request_options
        ).unwrap()

    def payment_initiation_recipient_create(
        self,
        body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientCreateResponse:
        """Create a payment recipient for payment initiation. The recipient must be in Europe, within a country that is
        a member of the Single Euro Payment Area (SEPA). For a standing order (recurring) payment, the recipient must be
        in the UK.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will
        return the same ``recipient_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_recipient_create(
            body, request_options=request_options
        ).unwrap()

    def payment_initiation_recipient_get(
        self,
        body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientGetResponse:
        """Get details about a payment recipient you have previously created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_recipient_get(body, request_options=request_options).unwrap()

    def payment_initiation_recipient_list(
        self,
        body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientListResponse:
        """The ``/payment_initiation/recipient/list`` endpoint list the payment recipients that you have previously
        created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.payment_initiation_recipient_list(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PaymentInitiationWithRawResponse:
        return self._with_raw_response


class AsyncPaymentInitiation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentInitiationWithRawResponse(client, server, auth)

    async def create_payment_token(
        self,
        body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentTokenCreateResponse:
        """The ``/payment_initiation/payment/token/create`` endpoint has been deprecated. New Plaid customers will be
        unable to use this endpoint, and existing customers are encouraged to migrate to the newer, ``link_token``-based
        flow. The recommended flow is to provide the ``payment_id`` to ``/link/token/create``, which returns a
        ``link_token`` used to initialize Link.

        The ``/payment_initiation/payment/token/create`` is used to create a ``payment_token``, which can then be used
        in Link initialization to enter a payment initiation flow. You can only use a ``payment_token`` once. If this
        attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token.
        Creating a new payment token does not require end user input.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_payment_token(body, request_options=request_options)).unwrap()

    async def payment_initiation_payment_create(
        self,
        body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentCreateResponse:
        """After creating a payment recipient, you can use the ``/payment_initiation/payment/create`` endpoint to create
        a payment to that recipient. Payments can be one-time or standing order (recurring) and can be denominated in
        either EUR or GBP. If making domestic GBP-denominated payments, your recipient must have been created with BACS
        numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments
        will be sent via the Faster Payments network, but the payment network used will be determined by the
        institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA
        Credit Transfer will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK.
        Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or
        modify a standing order directly on their banking application or website, or by contacting the bank. Standing
        orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent
        Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the
        payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach
        the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in
        Production, contact your Plaid Account Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_payment_create(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_payment_get(
        self,
        body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentGetResponse:
        """The ``/payment_initiation/payment/get`` endpoint can be used to check the status of a payment, as well as to
        receive basic information such as recipient and payment amount. In the case of standing orders, the
        ``/payment_initiation/payment/get`` endpoint will provide information about the status of the overall standing
        order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_payment_get(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_payment_list(
        self,
        body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentListResponse:
        """The ``/payment_initiation/payment/list`` endpoint can be used to retrieve all created payments. By default,
        the 10 most recent payments are returned. You can request more payments and paginate through the results using
        the optional ``count`` and ``cursor`` parameters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_payment_list(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_payment_reverse(
        self,
        body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationPaymentReverseResponse:
        """Reverse a previously initiated payment.

        A payment can only be reversed once and will be refunded to the original sender's account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_payment_reverse(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_recipient_create(
        self,
        body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientCreateResponse:
        """Create a payment recipient for payment initiation. The recipient must be in Europe, within a country that is
        a member of the Single Euro Payment Area (SEPA). For a standing order (recurring) payment, the recipient must be
        in the UK.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will
        return the same ``recipient_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_recipient_create(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_recipient_get(
        self,
        body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientGetResponse:
        """Get details about a payment recipient you have previously created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_recipient_get(body, request_options=request_options)
        ).unwrap()

    async def payment_initiation_recipient_list(
        self,
        body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInitiationRecipientListResponse:
        """The ``/payment_initiation/recipient/list`` endpoint list the payment recipients that you have previously
        created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.payment_initiation_recipient_list(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentInitiationWithRawResponse:
        return self._with_raw_response


class PaymentInitiationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_payment_token(
        self,
        body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentTokenCreateResponse, RawError]:
        """The ``/payment_initiation/payment/token/create`` endpoint has been deprecated. New Plaid customers will be
        unable to use this endpoint, and existing customers are encouraged to migrate to the newer, ``link_token``-based
        flow. The recommended flow is to provide the ``payment_id`` to ``/link/token/create``, which returns a
        ``link_token`` used to initialize Link.

        The ``/payment_initiation/payment/token/create`` is used to create a ``payment_token``, which can then be used
        in Link initialization to enter a payment initiation flow. You can only use a ``payment_token`` once. If this
        attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token.
        Creating a new payment token does not require end user input.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict](
                body
            ),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationPaymentTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_payment_create(
        self,
        body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentCreateResponse, RawError]:
        """After creating a payment recipient, you can use the ``/payment_initiation/payment/create`` endpoint to create
        a payment to that recipient. Payments can be one-time or standing order (recurring) and can be denominated in
        either EUR or GBP. If making domestic GBP-denominated payments, your recipient must have been created with BACS
        numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments
        will be sent via the Faster Payments network, but the payment network used will be determined by the
        institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA
        Credit Transfer will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK.
        Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or
        modify a standing order directly on their banking application or website, or by contacting the bank. Standing
        orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent
        Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the
        payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach
        the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in
        Production, contact your Plaid Account Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationPaymentCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_payment_get(
        self,
        body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentGetResponse, RawError]:
        """The ``/payment_initiation/payment/get`` endpoint can be used to check the status of a payment, as well as to
        receive basic information such as recipient and payment amount. In the case of standing orders, the
        ``/payment_initiation/payment/get`` endpoint will provide information about the status of the overall standing
        order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationPaymentGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_payment_list(
        self,
        body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentListResponse, RawError]:
        """The ``/payment_initiation/payment/list`` endpoint can be used to retrieve all created payments. By default,
        the 10 most recent payments are returned. You can request more payments and paginate through the results using
        the optional ``count`` and ``cursor`` parameters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationPaymentListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_payment_reverse(
        self,
        body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentReverseResponse, RawError]:
        """Reverse a previously initiated payment.

        A payment can only be reversed once and will be refunded to the original sender's account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/reverse"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationPaymentReverseResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_recipient_create(
        self,
        body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientCreateResponse, RawError]:
        """Create a payment recipient for payment initiation. The recipient must be in Europe, within a country that is
        a member of the Single Euro Payment Area (SEPA). For a standing order (recurring) payment, the recipient must be
        in the UK.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will
        return the same ``recipient_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationRecipientCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_recipient_get(
        self,
        body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientGetResponse, RawError]:
        """Get details about a payment recipient you have previously created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationRecipientGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def payment_initiation_recipient_list(
        self,
        body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientListResponse, RawError]:
        """The ``/payment_initiation/recipient/list`` endpoint list the payment recipients that you have previously
        created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict](body),
            auth_scheme=AllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=json_decoder[PaymentInitiationRecipientListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPaymentInitiationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_payment_token(
        self,
        body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentTokenCreateResponse, RawError]:
        """The ``/payment_initiation/payment/token/create`` endpoint has been deprecated. New Plaid customers will be
        unable to use this endpoint, and existing customers are encouraged to migrate to the newer, ``link_token``-based
        flow. The recommended flow is to provide the ``payment_id`` to ``/link/token/create``, which returns a
        ``link_token`` used to initialize Link.

        The ``/payment_initiation/payment/token/create`` is used to create a ``payment_token``, which can then be used
        in Link initialization to enter a payment initiation flow. You can only use a ``payment_token`` once. If this
        attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token.
        Creating a new payment token does not require end user input.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/token/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict](
                body
            ),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationPaymentTokenCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_payment_create(
        self,
        body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentCreateResponse, RawError]:
        """After creating a payment recipient, you can use the ``/payment_initiation/payment/create`` endpoint to create
        a payment to that recipient. Payments can be one-time or standing order (recurring) and can be denominated in
        either EUR or GBP. If making domestic GBP-denominated payments, your recipient must have been created with BACS
        numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments
        will be sent via the Faster Payments network, but the payment network used will be determined by the
        institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA
        Credit Transfer will typically arrive in one business day.

        Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK.
        Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or
        modify a standing order directly on their banking application or website, or by contacting the bank. Standing
        orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent
        Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the
        payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach
        the recipient’s account, although at least 90% of standing order payments are sent by 6am.

        In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in
        Production, contact your Plaid Account Manager.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationPaymentCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_payment_get(
        self,
        body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentGetResponse, RawError]:
        """The ``/payment_initiation/payment/get`` endpoint can be used to check the status of a payment, as well as to
        receive basic information such as recipient and payment amount. In the case of standing orders, the
        ``/payment_initiation/payment/get`` endpoint will provide information about the status of the overall standing
        order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationPaymentGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_payment_list(
        self,
        body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentListResponse, RawError]:
        """The ``/payment_initiation/payment/list`` endpoint can be used to retrieve all created payments. By default,
        the 10 most recent payments are returned. You can request more payments and paginate through the results using
        the optional ``count`` and ``cursor`` parameters.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationPaymentListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_payment_reverse(
        self,
        body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationPaymentReverseResponse, RawError]:
        """Reverse a previously initiated payment.

        A payment can only be reversed once and will be refunded to the original sender's account.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/payment/reverse"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationPaymentReverseResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_recipient_create(
        self,
        body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientCreateResponse, RawError]:
        """Create a payment recipient for payment initiation. The recipient must be in Europe, within a country that is
        a member of the Single Euro Payment Area (SEPA). For a standing order (recurring) payment, the recipient must be
        in the UK.

        The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will
        return the same ``recipient_id``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationRecipientCreateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_recipient_get(
        self,
        body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientGetResponse, RawError]:
        """Get details about a payment recipient you have previously created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/get"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationRecipientGetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def payment_initiation_recipient_list(
        self,
        body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInitiationRecipientListResponse, RawError]:
        """The ``/payment_initiation/recipient/list`` endpoint list the payment recipients that you have previously
        created.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/payment_initiation/recipient/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.plaid_client_id, self._auth.plaid_secret, self._auth.plaid_version),
            decoder=async_json_decoder[PaymentInitiationRecipientListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
