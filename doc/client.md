
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](../README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| plaid_client_id_credentials | [`PlaidClientIdCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| plaid_secret_credentials | [`PlaidSecretCredentials`](auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| plaid_version_credentials | [`PlaidVersionCredentials`](auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from plaid.configuration import Environment
from plaid.http.auth.plaid_client_id import PlaidClientIdCredentials
from plaid.http.auth.plaid_secret import PlaidSecretCredentials
from plaid.http.auth.plaid_version import PlaidVersionCredentials
from plaid.logging.configuration.api_logging_configuration import LoggingConfiguration
from plaid.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from plaid.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from plaid.plaid_client import PlaidClient

client = PlaidClient(
    plaid_client_id_credentials=PlaidClientIdCredentials(
        plaid_client_id='PLAID-CLIENT-ID'
    ),
    plaid_secret_credentials=PlaidSecretCredentials(
        plaid_secret='PLAID-SECRET'
    ),
    plaid_version_credentials=PlaidVersionCredentials(
        plaid_version='Plaid-Version'
    ),
    environment=Environment.PRODUCTION,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from plaid.plaid_client import PlaidClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PlaidClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## The Plaid API Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| item | Gets ItemApi |
| asset_report | Gets AssetReportApi |
| processor | Gets ProcessorApi |
| payment_initiation | Gets PaymentInitiationApi |
| sandbox | Gets SandboxApi |
| investments | Gets InvestmentsApi |
| institutions | Gets InstitutionsApi |
| application | Gets ApplicationApi |
| accounts | Gets AccountsApi |
| identity | Gets IdentityApi |
| liabilities | Gets LiabilitiesApi |
| auth | Gets AuthApi |
| transactions | Gets TransactionsApi |
| categories | Gets CategoriesApi |
| webhook_verification_key | Gets WebhookVerificationKeyApi |
| deposit_switch | Gets DepositSwitchApi |
| link | Gets LinkApi |
| transfer | Gets TransferApi |
| bank_transfer | Gets BankTransferApi |
| employers | Gets EmployersApi |
| income | Gets IncomeApi |
| signal | Gets SignalApi |

