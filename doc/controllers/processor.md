# Processor

```python
processor_api = client.processor
```

## Class Name

`ProcessorApi`

## Methods

* [Processor Bank Transfer Create](../../doc/controllers/processor.md#processor-bank-transfer-create)
* [Processor Balance Get](../../doc/controllers/processor.md#processor-balance-get)
* [Processor Auth Get](../../doc/controllers/processor.md#processor-auth-get)
* [Processor Identity Get](../../doc/controllers/processor.md#processor-identity-get)
* [Processor Apex Processor Token Create](../../doc/controllers/processor.md#processor-apex-processor-token-create)
* [Processor Token Create](../../doc/controllers/processor.md#processor-token-create)
* [Processor Stripe Bank Account Token Create](../../doc/controllers/processor.md#processor-stripe-bank-account-token-create)


# Processor Bank Transfer Create

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

Find out more here: [/api/processors/#bank_transfercreate](/api/processors/#bank_transfercreate)

```python
def processor_bank_transfer_create(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorBankTransferCreateRequest`](../../doc/models/processor-bank-transfer-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorBankTransferCreateResponse`](../../doc/models/processor-bank-transfer-create-response.md).

## Example Usage

```python
body = ProcessorBankTransferCreateRequest(
    idempotency_key='idempotency_key2',
    processor_token='processor_token4',
    mtype=BankTransferType.DEBIT,
    network=BankTransferNetwork.SAMEDAYACH,
    amount='amount8',
    iso_currency_code='iso_currency_code0',
    description='description4',
    user=BankTransferUser(
        legal_name='legal_name8'
    )
)

result = processor_api.processor_bank_transfer_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Processor Balance Get

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached.

Find out more here: [/api/processors/#processorbalanceget](/api/processors/#processorbalanceget)

```python
def processor_balance_get(self,
                         body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorBalanceGetRequest`](../../doc/models/processor-balance-get-request.md) | Body, Required | The `/processor/balance/get` endpoint returns the real-time balance for the account associated with a given `processor_token`.<br><br>The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.<br><br>Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of `null`. |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorBalanceGetResponse`](../../doc/models/processor-balance-get-response.md).

## Example Usage

```python
body = ProcessorBalanceGetRequest(
    processor_token='processor_token4'
)

result = processor_api.processor_balance_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "account": {
    "account_id": "QKKzevvp33HxPWpoqn6rI13BxW4awNSjnw4xv",
    "balances": {
      "available": 100,
      "current": 110,
      "limit": null,
      "iso_currency_code": "USD",
      "unofficial_currency_code": null
    },
    "mask": "0000",
    "name": "Plaid Checking",
    "official_name": "Plaid Gold Checking",
    "subtype": "checking",
    "type": "depository"
  },
  "request_id": "1zlMf"
}
```


# Processor Auth Get

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that's associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

Find out more here: [/api/processors/#processorauthget](/api/processors/#processorauthget)

```python
def processor_auth_get(self,
                      body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorAuthGetRequest`](../../doc/models/processor-auth-get-request.md) | Body, Required | - |

## Response Type

**200**: success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorAuthGetResponse`](../../doc/models/processor-auth-get-response.md).

## Example Usage

```python
body = ProcessorAuthGetRequest(
    processor_token='processor_token4'
)

result = processor_api.processor_auth_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "account": {
    "account_id": "vzeNDwK7KQIm4yEog683uElbp9GRLEFXGK98D",
    "balances": {
      "available": 100,
      "current": 110,
      "iso_currency_code": "USD",
      "limit": null,
      "unofficial_currency_code": null
    },
    "mask": "0000",
    "name": "Plaid Checking",
    "official_name": "Plaid Gold Checking",
    "subtype": "checking",
    "type": "depository"
  },
  "numbers": {
    "ach": {
      "account": "9900009606",
      "account_id": "vzeNDwK7KQIm4yEog683uElbp9GRLEFXGK98D",
      "routing": "011401533",
      "wire_routing": "021000021"
    },
    "eft": {
      "account": "111122223333",
      "account_id": "vzeNDwK7KQIm4yEog683uElbp9GRLEFXGK98D",
      "institution": "021",
      "branch": "01140"
    },
    "international": {
      "account_id": "vzeNDwK7KQIm4yEog683uElbp9GRLEFXGK98D",
      "bic": "NWBKGB21",
      "iban": "GB29NWBK60161331926819"
    },
    "bacs": {
      "account": "31926819",
      "account_id": "vzeNDwK7KQIm4yEog683uElbp9GRLEFXGK98D",
      "sort_code": "601613"
    }
  },
  "request_id": "1zlMf"
}
```


# Processor Identity Get

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

Find out more here: [/api/processors/#processoridentityget](/api/processors/#processoridentityget)

```python
def processor_identity_get(self,
                          body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorIdentityGetRequest`](../../doc/models/processor-identity-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorIdentityGetResponse`](../../doc/models/processor-identity-get-response.md).

## Example Usage

```python
body = ProcessorIdentityGetRequest(
    processor_token='processor_token4'
)

result = processor_api.processor_identity_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "account": {
    "account_id": "XMGPJy4q1gsQoKd5z9R3tK8kJ9EWL8SdkgKMq",
    "balances": {
      "available": 100,
      "current": 110,
      "iso_currency_code": "USD",
      "limit": null,
      "unofficial_currency_code": null
    },
    "mask": "0000",
    "name": "Plaid Checking",
    "official_name": "Plaid Gold Standard 0% Interest Checking",
    "owners": [
      {
        "addresses": [
          {
            "data": {
              "city": "Malakoff",
              "country": "US",
              "postal_code": "14236",
              "region": "NY",
              "street": "2992 Cameron Road"
            },
            "primary": true
          },
          {
            "data": {
              "city": "San Matias",
              "country": "US",
              "postal_code": "93405-2255",
              "region": "CA",
              "street": "2493 Leisure Lane"
            },
            "primary": false
          }
        ],
        "emails": [
          {
            "data": "accountholder0@example.com",
            "primary": true,
            "type": "primary"
          },
          {
            "data": "accountholder1@example.com",
            "primary": false,
            "type": "secondary"
          },
          {
            "data": "extraordinarily.long.email.username.123456@reallylonghostname.com",
            "primary": false,
            "type": "other"
          }
        ],
        "names": [
          "Alberta Bobbeth Charleson"
        ],
        "phone_numbers": [
          {
            "data": "1112223333",
            "primary": false,
            "type": "home"
          },
          {
            "data": "1112224444",
            "primary": false,
            "type": "work"
          },
          {
            "data": "1112225555",
            "primary": false,
            "type": "mobile1"
          }
        ]
      }
    ],
    "subtype": "checking",
    "type": "depository"
  },
  "request_id": "eOPkBl6t33veI2J"
}
```


# Processor Apex Processor Token Create

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

Find out more here: [/none/](/none/)

```python
def processor_apex_processor_token_create(self,
                                         body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorApexProcessorTokenCreateRequest`](../../doc/models/processor-apex-processor-token-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorTokenCreateResponse`](../../doc/models/processor-token-create-response.md).

## Example Usage

```python
body = ProcessorApexProcessorTokenCreateRequest(
    access_token='access_token4',
    account_id='account_id8'
)

result = processor_api.processor_apex_processor_token_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Processor Token Create

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations.

Find out more here: [/api/processors/#processortokencreate](/api/processors/#processortokencreate)

```python
def processor_token_create(self,
                          body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorTokenCreateRequest`](../../doc/models/processor-token-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorTokenCreateResponse`](../../doc/models/processor-token-create-response.md).

## Example Usage

```python
body = ProcessorTokenCreateRequest(
    access_token='access_token4',
    account_id='account_id8',
    processor=Processor.ASTRA
)

result = processor_api.processor_token_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "processor_token": "processor-sandbox-0asd1-a92nc",
  "request_id": "xrQNYZ7Zoh6R7gV"
}
```


# Processor Stripe Bank Account Token Create

Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

Find out more here: [/api/processors/#processorstripebank_account_tokencreate](/api/processors/#processorstripebank_account_tokencreate)

```python
def processor_stripe_bank_account_token_create(self,
                                              body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProcessorStripeBankAccountTokenCreateRequest`](../../doc/models/processor-stripe-bank-account-token-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ProcessorStripeBankAccountTokenCreateResponse`](../../doc/models/processor-stripe-bank-account-token-create-response.md).

## Example Usage

```python
body = ProcessorStripeBankAccountTokenCreateRequest(
    access_token='access_token4',
    account_id='account_id8'
)

result = processor_api.processor_stripe_bank_account_token_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "stripe_bank_account_token": "btok_5oEetfLzPklE1fwJZ7SG",
  "request_id": "xrQNYZ7Zoh6R7gV"
}
```

