from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.accounts import Accounts
from .apis.application_api import ApplicationApi
from .apis.asset_report_api import AssetReportApi
from .apis.auth_api import AuthApi
from .apis.bank_transfer_api import BankTransferApi
from .apis.categories import Categories
from .apis.deposit_switch import DepositSwitch
from .apis.employers import Employers
from .apis.identity import Identity
from .apis.income import Income
from .apis.institutions import Institutions
from .apis.investments import Investments
from .apis.item_api import ItemApi
from .apis.liabilities import Liabilities
from .apis.link import Link
from .apis.payment_initiation import PaymentInitiation
from .apis.processor_api import ProcessorApi
from .apis.sandbox import Sandbox
from .apis.signal import Signal
from .apis.transactions import Transactions
from .apis.transfer_api import TransferApi
from .apis.webhook_verification_key import WebhookVerificationKey
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseThePlaidApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class ThePlaidApiClient(BaseThePlaidApiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        plaid_client_id: str | None = None,
        plaid_secret: str | None = None,
        plaid_version: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
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
        self._auth = AuthSchemes(
            plaid_client_id=(
                ApiKeyHeaderScheme("PLAID-CLIENT-ID", plaid_client_id) if plaid_client_id is not None else no_auth
            ),
            plaid_secret=ApiKeyHeaderScheme("PLAID-SECRET", plaid_secret) if plaid_secret is not None else no_auth,
            plaid_version=ApiKeyHeaderScheme("Plaid-Version", plaid_version) if plaid_version is not None else no_auth,
        )

    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._raw_client, self._server, self._auth)

    @cached_property
    def application_api(self) -> ApplicationApi:
        return ApplicationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def asset_report_api(self) -> AssetReportApi:
        return AssetReportApi(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_api(self) -> AuthApi:
        return AuthApi(self._raw_client, self._server, self._auth)

    @cached_property
    def bank_transfer_api(self) -> BankTransferApi:
        return BankTransferApi(self._raw_client, self._server, self._auth)

    @cached_property
    def categories(self) -> Categories:
        return Categories(self._raw_client, self._server)

    @cached_property
    def deposit_switch(self) -> DepositSwitch:
        return DepositSwitch(self._raw_client, self._server, self._auth)

    @cached_property
    def employers(self) -> Employers:
        return Employers(self._raw_client, self._server, self._auth)

    @cached_property
    def identity(self) -> Identity:
        return Identity(self._raw_client, self._server, self._auth)

    @cached_property
    def income(self) -> Income:
        return Income(self._raw_client, self._server, self._auth)

    @cached_property
    def institutions(self) -> Institutions:
        return Institutions(self._raw_client, self._server, self._auth)

    @cached_property
    def investments(self) -> Investments:
        return Investments(self._raw_client, self._server, self._auth)

    @cached_property
    def item_api(self) -> ItemApi:
        return ItemApi(self._raw_client, self._server, self._auth)

    @cached_property
    def liabilities(self) -> Liabilities:
        return Liabilities(self._raw_client, self._server, self._auth)

    @cached_property
    def link(self) -> Link:
        return Link(self._raw_client, self._server, self._auth)

    @cached_property
    def payment_initiation(self) -> PaymentInitiation:
        return PaymentInitiation(self._raw_client, self._server, self._auth)

    @cached_property
    def processor_api(self) -> ProcessorApi:
        return ProcessorApi(self._raw_client, self._server, self._auth)

    @cached_property
    def sandbox(self) -> Sandbox:
        return Sandbox(self._raw_client, self._server, self._auth)

    @cached_property
    def signal(self) -> Signal:
        return Signal(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> Transactions:
        return Transactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_api(self) -> TransferApi:
        return TransferApi(self._raw_client, self._server, self._auth)

    @cached_property
    def webhook_verification_key(self) -> WebhookVerificationKey:
        return WebhookVerificationKey(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = ThePlaidApiClient
