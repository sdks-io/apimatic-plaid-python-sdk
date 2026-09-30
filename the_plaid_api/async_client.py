from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.accounts import AsyncAccounts
from .apis.application_api import AsyncApplicationApi
from .apis.asset_report_api import AsyncAssetReportApi
from .apis.auth_api import AsyncAuthApi
from .apis.bank_transfer_api import AsyncBankTransferApi
from .apis.categories import AsyncCategories
from .apis.deposit_switch import AsyncDepositSwitch
from .apis.employers import AsyncEmployers
from .apis.identity import AsyncIdentity
from .apis.income import AsyncIncome
from .apis.institutions import AsyncInstitutions
from .apis.investments import AsyncInvestments
from .apis.item_api import AsyncItemApi
from .apis.liabilities import AsyncLiabilities
from .apis.link import AsyncLink
from .apis.payment_initiation import AsyncPaymentInitiation
from .apis.processor_api import AsyncProcessorApi
from .apis.sandbox import AsyncSandbox
from .apis.signal import AsyncSignal
from .apis.transactions import AsyncTransactions
from .apis.transfer_api import AsyncTransferApi
from .apis.webhook_verification_key import AsyncWebhookVerificationKey
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseThePlaidApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncThePlaidApiClient(BaseThePlaidApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        plaid_client_id: str | None = None,
        plaid_secret: str | None = None,
        plaid_version: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "ThePlaidApiClient/0.1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "0.1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            plaid_client_id=(
                ApiKeyHeaderScheme("PLAID-CLIENT-ID", plaid_client_id) if plaid_client_id is not None else no_auth
            ),
            plaid_secret=ApiKeyHeaderScheme("PLAID-SECRET", plaid_secret) if plaid_secret is not None else no_auth,
            plaid_version=ApiKeyHeaderScheme("Plaid-Version", plaid_version) if plaid_version is not None else no_auth,
        )

    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def application_api(self) -> AsyncApplicationApi:
        return AsyncApplicationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def asset_report_api(self) -> AsyncAssetReportApi:
        return AsyncAssetReportApi(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_api(self) -> AsyncAuthApi:
        return AsyncAuthApi(self._raw_client, self._server, self._auth)

    @cached_property
    def bank_transfer_api(self) -> AsyncBankTransferApi:
        return AsyncBankTransferApi(self._raw_client, self._server, self._auth)

    @cached_property
    def categories(self) -> AsyncCategories:
        return AsyncCategories(self._raw_client, self._server)

    @cached_property
    def deposit_switch(self) -> AsyncDepositSwitch:
        return AsyncDepositSwitch(self._raw_client, self._server, self._auth)

    @cached_property
    def employers(self) -> AsyncEmployers:
        return AsyncEmployers(self._raw_client, self._server, self._auth)

    @cached_property
    def identity(self) -> AsyncIdentity:
        return AsyncIdentity(self._raw_client, self._server, self._auth)

    @cached_property
    def income(self) -> AsyncIncome:
        return AsyncIncome(self._raw_client, self._server, self._auth)

    @cached_property
    def institutions(self) -> AsyncInstitutions:
        return AsyncInstitutions(self._raw_client, self._server, self._auth)

    @cached_property
    def investments(self) -> AsyncInvestments:
        return AsyncInvestments(self._raw_client, self._server, self._auth)

    @cached_property
    def item_api(self) -> AsyncItemApi:
        return AsyncItemApi(self._raw_client, self._server, self._auth)

    @cached_property
    def liabilities(self) -> AsyncLiabilities:
        return AsyncLiabilities(self._raw_client, self._server, self._auth)

    @cached_property
    def link(self) -> AsyncLink:
        return AsyncLink(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_initiation(self) -> AsyncPaymentInitiation:
        return AsyncPaymentInitiation(self._raw_client, self._server, self._auth)

    @cached_property
    def processor_api(self) -> AsyncProcessorApi:
        return AsyncProcessorApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sandbox(self) -> AsyncSandbox:
        return AsyncSandbox(self._raw_client, self._server, self._auth)

    @cached_property
    def signal(self) -> AsyncSignal:
        return AsyncSignal(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> AsyncTransactions:
        return AsyncTransactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_api(self) -> AsyncTransferApi:
        return AsyncTransferApi(self._raw_client, self._server, self._auth)

    @cached_property
    def webhook_verification_key(self) -> AsyncWebhookVerificationKey:
        return AsyncWebhookVerificationKey(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncThePlaidApiClient
