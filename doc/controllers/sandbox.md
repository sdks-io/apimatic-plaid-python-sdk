# Sandbox

```python
sandbox_api = client.sandbox
```

## Class Name

`SandboxApi`

## Methods

* [Sandbox Item Set Verification Status](../../doc/controllers/sandbox.md#sandbox-item-set-verification-status)
* [Sandbox Public Token Create](../../doc/controllers/sandbox.md#sandbox-public-token-create)
* [Sandbox Processor Token Create](../../doc/controllers/sandbox.md#sandbox-processor-token-create)
* [Sandbox Item Fire Webhook](../../doc/controllers/sandbox.md#sandbox-item-fire-webhook)
* [Sandbox Item Reset Login](../../doc/controllers/sandbox.md#sandbox-item-reset-login)
* [Sandbox Income Fire Webhook](../../doc/controllers/sandbox.md#sandbox-income-fire-webhook)
* [Sandbox Oauth Select Accounts](../../doc/controllers/sandbox.md#sandbox-oauth-select-accounts)
* [Sandbox Transfer Simulate](../../doc/controllers/sandbox.md#sandbox-transfer-simulate)
* [Sandbox Bank Transfer Fire Webhook](../../doc/controllers/sandbox.md#sandbox-bank-transfer-fire-webhook)
* [Sandbox Bank Transfer Simulate](../../doc/controllers/sandbox.md#sandbox-bank-transfer-simulate)


# Sandbox Item Set Verification Status

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

Find out more here: [/api/sandbox/#sandboxitemset_verification_status](/api/sandbox/#sandboxitemset_verification_status)

```python
def sandbox_item_set_verification_status(self,
                                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxItemSetVerificationStatusRequest`](../../doc/models/sandbox-item-set-verification-status-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxItemSetVerificationStatusResponse`](../../doc/models/sandbox-item-set-verification-status-response.md).

## Example Usage

```python
body = SandboxItemSetVerificationStatusRequest(
    access_token='access_token4',
    account_id='account_id8',
    verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED
)

result = sandbox_api.sandbox_item_set_verification_status(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "1vwmF5TBQwiqfwP"
}
```


# Sandbox Public Token Create

Use the `/sandbox/public_token/create`  endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

Find out more here: [/api/sandbox/#sandboxpublic_tokencreate](/api/sandbox/#sandboxpublic_tokencreate)

```python
def sandbox_public_token_create(self,
                               body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxPublicTokenCreateRequest`](../../doc/models/sandbox-public-token-create-request.md) | Body, Required | - |

## Response Type

**200**: success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxPublicTokenCreateResponse`](../../doc/models/sandbox-public-token-create-response.md).

## Example Usage

```python
body = SandboxPublicTokenCreateRequest(
    institution_id='institution_id4',
    initial_products=[
        Products.DEPOSIT_SWITCH
    ]
)

result = sandbox_api.sandbox_public_token_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "public_token": "public-sandbox-b0e2c4ee-a763-4df5-bfe9-46a46bce993d",
  "request_id": "Aim3b"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Processor Token Create

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

Find out more here: [/api/sandbox/#sandboxprocessor_tokencreate](/api/sandbox/#sandboxprocessor_tokencreate)

```python
def sandbox_processor_token_create(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxProcessorTokenCreateRequest`](../../doc/models/sandbox-processor-token-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxProcessorTokenCreateResponse`](../../doc/models/sandbox-processor-token-create-response.md).

## Example Usage

```python
body = SandboxProcessorTokenCreateRequest(
    institution_id='institution_id4'
)

result = sandbox_api.sandbox_processor_token_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "processor_token": "processor-sandbox-b0e2c4ee-a763-4df5-bfe9-46a46bce993d",
  "request_id": "Aim3b"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Item Fire Webhook

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. Calling this endpoint triggers a Transactions `DEFAULT_UPDATE` webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

Find out more here: [/api/sandbox/#sandboxitemfire_webhook](/api/sandbox/#sandboxitemfire_webhook)

```python
def sandbox_item_fire_webhook(self,
                             body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxItemFireWebhookRequest`](../../doc/models/sandbox-item-fire-webhook-request.md) | Body, Required | - |

## Response Type

**200**: success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxItemFireWebhookResponse`](../../doc/models/sandbox-item-fire-webhook-response.md).

## Example Usage

```python
body = SandboxItemFireWebhookRequest(
    access_token='access_token4',
    webhook_code='DEFAULT_UPDATE'
)

result = sandbox_api.sandbox_item_fire_webhook(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "webhook_fired": true,
  "request_id": "1vwmF5TBQwiqfwP"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Item Reset Login

`/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.

In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

Find out more here: [/api/sandbox/#sandboxitemreset_login](/api/sandbox/#sandboxitemreset_login)

```python
def sandbox_item_reset_login(self,
                            body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxItemResetLoginRequest`](../../doc/models/sandbox-item-reset-login-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxItemResetLoginResponse`](../../doc/models/sandbox-item-reset-login-response.md).

## Example Usage

```python
body = SandboxItemResetLoginRequest(
    access_token='access_token4'
)

result = sandbox_api.sandbox_item_reset_login(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "reset_login": true,
  "request_id": "m8MDnv9okwxFNBV"
}
```


# Sandbox Income Fire Webhook

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.

Find out more here: [/api/sandbox/#sandboxincomefire_webhook](/api/sandbox/#sandboxincomefire_webhook)

```python
def sandbox_income_fire_webhook(self,
                               body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxIncomeFireWebhookRequest`](../../doc/models/sandbox-income-fire-webhook-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxIncomeFireWebhookResponse`](../../doc/models/sandbox-income-fire-webhook-response.md).

## Example Usage

```python
body = SandboxIncomeFireWebhookRequest(
    income_verification_id='income_verification_id6',
    webhook='webhook4',
    verification_status=VerificationStatus3.VERIFICATION_STATUS_PROCESSING_COMPLETE
)

result = sandbox_api.sandbox_income_fire_webhook(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Oauth Select Accounts

Save the selected accounts when connecting to the Platypus Oauth institution

```python
def sandbox_oauth_select_accounts(self,
                                 body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxOauthSelectAccountsRequest`](../../doc/models/sandbox-oauth-select-accounts-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = SandboxOauthSelectAccountsRequest(
    oauth_state_id='oauth_state_id6',
    accounts=[
        'accounts4'
    ]
)

result = sandbox_api.sandbox_oauth_select_accounts(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Transfer Simulate

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

Find out more here: [/transfer/reference#sandboxtransfersimulate](/transfer/reference#sandboxtransfersimulate)

```python
def sandbox_transfer_simulate(self,
                             body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxTransferSimulateRequest`](../../doc/models/sandbox-transfer-simulate-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxTransferSimulateResponse`](../../doc/models/sandbox-transfer-simulate-response.md).

## Example Usage

```python
body = SandboxTransferSimulateRequest(
    transfer_id='transfer_id2',
    event_type='event_type4'
)

result = sandbox_api.sandbox_transfer_simulate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Bank Transfer Fire Webhook

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

Find out more here: [/api/sandbox/#sandboxbank_transferfire_webhook](/api/sandbox/#sandboxbank_transferfire_webhook)

```python
def sandbox_bank_transfer_fire_webhook(self,
                                      body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxBankTransferFireWebhookRequest`](../../doc/models/sandbox-bank-transfer-fire-webhook-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxBankTransferFireWebhookResponse`](../../doc/models/sandbox-bank-transfer-fire-webhook-response.md).

## Example Usage

```python
body = SandboxBankTransferFireWebhookRequest(
    webhook='webhook4'
)

result = sandbox_api.sandbox_bank_transfer_fire_webhook(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Sandbox Bank Transfer Simulate

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

Find out more here: [/api/sandbox/#sandboxbank_transfersimulate](/api/sandbox/#sandboxbank_transfersimulate)

```python
def sandbox_bank_transfer_simulate(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SandboxBankTransferSimulateRequest`](../../doc/models/sandbox-bank-transfer-simulate-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SandboxBankTransferSimulateResponse`](../../doc/models/sandbox-bank-transfer-simulate-response.md).

## Example Usage

```python
body = SandboxBankTransferSimulateRequest(
    bank_transfer_id='bank_transfer_id8',
    event_type='event_type4'
)

result = sandbox_api.sandbox_bank_transfer_simulate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

