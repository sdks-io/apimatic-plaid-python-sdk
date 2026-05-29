
# Getting Started with The Plaid API

## Introduction

The Plaid REST API. Please see https://plaid.com/docs/api for more details.

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install apimatic-plaid-sdk==0.0.1
```

You can also view the package at:
https://pypi.python.org/pypi/apimatic-plaid-sdk/0.0.1

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| plaid_client_id_credentials | [`PlaidClientIdCredentials`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| plaid_secret_credentials | [`PlaidSecretCredentials`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |
| plaid_version_credentials | [`PlaidVersionCredentials`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature-2.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

### Code-Based Client Initialization

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

### Environment-Based Client Initialization

```python
from plaid.plaid_client import PlaidClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PlaidClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** Production |
| ENVIRONMENT2 | Development |
| ENVIRONMENT3 | Sandbox |

## Authorization

This API uses the following authentication schemes.

* [`PLAID-CLIENT-ID (Custom Header Signature)`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature.md)
* [`PLAID-SECRET (Custom Header Signature)`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature-1.md)
* [`Plaid-Version (Custom Header Signature)`](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/auth/custom-header-signature-2.md)

## List of APIs

* [Item](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/item.md)
* [Asset Report](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/asset-report.md)
* [Processor](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/processor.md)
* [Payment Initiation](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/payment-initiation.md)
* [Sandbox](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/sandbox.md)
* [Investments](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/investments.md)
* [Institutions](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/institutions.md)
* [Application](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/application.md)
* [Accounts](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/accounts.md)
* [Identity](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/identity.md)
* [Liabilities](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/liabilities.md)
* [Auth](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/auth.md)
* [Transactions](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/transactions.md)
* [Categories](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/categories.md)
* [Webhook Verification Key](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/webhook-verification-key.md)
* [Deposit Switch](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/deposit-switch.md)
* [Link](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/link.md)
* [Transfer](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/transfer.md)
* [Bank Transfer](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/bank-transfer.md)
* [Employers](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/employers.md)
* [Income](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/income.md)
* [Signal](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/controllers/signal.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/proxy-settings.md)
* [Environment-Based Client Initialization](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/environment-based-client-initialization.md)
* [AbstractLogger](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/http-request.md)

### Utilities

* [ApiResponse](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/api-response.md)
* [ApiHelper](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/sdks-io/apimatic-plaid-python-sdk/tree/0.0.1/doc/unix-date-time.md)

