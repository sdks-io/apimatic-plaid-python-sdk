# Payment Initiation

```python
payment_initiation_api = client.payment_initiation
```

## Class Name

`PaymentInitiationApi`

## Methods

* [Payment Initiation Payment Reverse](../../doc/controllers/payment-initiation.md#payment-initiation-payment-reverse)
* [Payment Initiation Recipient Create](../../doc/controllers/payment-initiation.md#payment-initiation-recipient-create)
* [Payment Initiation Recipient List](../../doc/controllers/payment-initiation.md#payment-initiation-recipient-list)
* [Payment Initiation Recipient Get](../../doc/controllers/payment-initiation.md#payment-initiation-recipient-get)
* [Payment Initiation Payment Create](../../doc/controllers/payment-initiation.md#payment-initiation-payment-create)
* [Payment Initiation Payment Get](../../doc/controllers/payment-initiation.md#payment-initiation-payment-get)
* [Create Payment Token](../../doc/controllers/payment-initiation.md#create-payment-token)
* [Payment Initiation Payment List](../../doc/controllers/payment-initiation.md#payment-initiation-payment-list)


# Payment Initiation Payment Reverse

Reverse a previously initiated payment.

A payment can only be reversed once and will be refunded to the original sender's account.

Find out more here: [/api/products/#payment_initiationpaymentreverse](/api/products/#payment_initiationpaymentreverse)

```python
def payment_initiation_payment_reverse(self,
                                      body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationPaymentReverseRequest`](../../doc/models/payment-initiation-payment-reverse-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationPaymentReverseResponse`](../../doc/models/payment-initiation-payment-reverse-response.md).

## Example Usage

```python
body = PaymentInitiationPaymentReverseRequest(
    payment_id='payment_id6'
)

result = payment_initiation_api.payment_initiation_payment_reverse(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "refund_id": "refund-id-sandbox-c5f8cd31-6cae-4cad-9b0d-f7c10be9cc4b",
  "request_id": "HtlKzBX0fMeF7mU",
  "status": "INITIATED"
}
```


# Payment Initiation Recipient Create

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA).  For a standing order (recurring) payment, the recipient must be in the UK.

The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.

Find out more here: [/api/products/#payment_initiationrecipientcreate](/api/products/#payment_initiationrecipientcreate)

```python
def payment_initiation_recipient_create(self,
                                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationRecipientCreateRequest`](../../doc/models/payment-initiation-recipient-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationRecipientCreateResponse`](../../doc/models/payment-initiation-recipient-create-response.md).

## Example Usage

```python
body = PaymentInitiationRecipientCreateRequest(
    name='name6'
)

result = payment_initiation_api.payment_initiation_recipient_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "recipient_id": "recipient-id-sandbox-9b6b4679-914b-445b-9450-efbdb80296f6",
  "request_id": "4zlKapIkTm8p5KM"
}
```


# Payment Initiation Recipient List

The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

Find out more here: [/api/products/#payment_initiationrecipientlist](/api/products/#payment_initiationrecipientlist)

```python
def payment_initiation_recipient_list(self,
                                     body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationRecipientListRequest`](../../doc/models/payment-initiation-recipient-list-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationRecipientListResponse`](../../doc/models/payment-initiation-recipient-list-response.md).

## Example Usage

```python
body = PaymentInitiationRecipientListRequest()

result = payment_initiation_api.payment_initiation_recipient_list(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "recipients": [
    {
      "recipient_id": "recipient-id-sandbox-9b6b4679-914b-445b-9450-efbdb80296f6",
      "name": "Wonder Wallet",
      "iban": "GB29NWBK60161331926819",
      "address": {
        "street": [
          "96 Guild Street",
          "9th Floor"
        ],
        "city": "London",
        "postal_code": "SE14 8JW",
        "country": "GB"
      }
    }
  ],
  "request_id": "4zlKapIkTm8p5KM"
}
```


# Payment Initiation Recipient Get

Get details about a payment recipient you have previously created.

Find out more here: [/api/products/#payment_initiationrecipientget](/api/products/#payment_initiationrecipientget)

```python
def payment_initiation_recipient_get(self,
                                    body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationRecipientGetRequest`](../../doc/models/payment-initiation-recipient-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationRecipientGetResponse`](../../doc/models/payment-initiation-recipient-get-response.md).

## Example Usage

```python
body = PaymentInitiationRecipientGetRequest(
    recipient_id='recipient_id4'
)

result = payment_initiation_api.payment_initiation_recipient_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "recipient_id": "recipient-id-sandbox-9b6b4679-914b-445b-9450-efbdb80296f6",
  "name": "Wonder Wallet",
  "iban": "GB29NWBK60161331926819",
  "address": {
    "street": [
      "96 Guild Street",
      "9th Floor"
    ],
    "city": "London",
    "postal_code": "SE14 8JW",
    "country": "GB"
  },
  "request_id": "4zlKapIkTm8p5KM"
}
```


# Payment Initiation Payment Create

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR or GBP.  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments will be sent via the Faster Payments network, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer will typically arrive in one business day.

Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in Production, contact your Plaid Account Manager.

Find out more here: [/api/products/#payment_initiationpaymentcreate](/api/products/#payment_initiationpaymentcreate)

```python
def payment_initiation_payment_create(self,
                                     body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationPaymentCreateRequest`](../../doc/models/payment-initiation-payment-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationPaymentCreateResponse`](../../doc/models/payment-initiation-payment-create-response.md).

## Example Usage

```python
body = PaymentInitiationPaymentCreateRequest(
    recipient_id='recipient_id4',
    reference='reference8',
    amount=PaymentAmount(
        currency=Currency.GBP,
        value=52.3
    )
)

result = payment_initiation_api.payment_initiation_payment_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "payment_id": "payment-id-sandbox-feca8a7a-5591-4aef-9297-f3062bb735d3",
  "status": "PAYMENT_STATUS_INPUT_NEEDED",
  "request_id": "4ciYVmesrySiUAB"
}
```


# Payment Initiation Payment Get

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

Find out more here: [/api/products/#payment_initiationpaymentget](/api/products/#payment_initiationpaymentget)

```python
def payment_initiation_payment_get(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationPaymentGetRequest`](../../doc/models/payment-initiation-payment-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationPaymentGetResponse`](../../doc/models/payment-initiation-payment-get-response.md).

## Example Usage

```python
body = PaymentInitiationPaymentGetRequest(
    payment_id='payment_id6'
)

result = payment_initiation_api.payment_initiation_payment_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Payment Token

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

Find out more here: [/link/maintain-legacy-integration/#creating-a-payment-token](/link/maintain-legacy-integration/#creating-a-payment-token)

```python
def create_payment_token(self,
                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationPaymentTokenCreateRequest`](../../doc/models/payment-initiation-payment-token-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationPaymentTokenCreateResponse`](../../doc/models/payment-initiation-payment-token-create-response.md).

## Example Usage

```python
body = PaymentInitiationPaymentTokenCreateRequest(
    payment_id='payment_id6'
)

result = payment_initiation_api.create_payment_token(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "payment_token": "payment-token-sandbox-feca8a7a-5591-4aef-9297-f3062bb735d3",
  "payment_token_expiration_time": "2020-01-01T00:00:00Z",
  "request_id": "4ciYVmesrySiUAB"
}
```


# Payment Initiation Payment List

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

Find out more here: [/api/products/#payment_initiationpaymentlist](/api/products/#payment_initiationpaymentlist)

```python
def payment_initiation_payment_list(self,
                                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInitiationPaymentListRequest`](../../doc/models/payment-initiation-payment-list-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PaymentInitiationPaymentListResponse`](../../doc/models/payment-initiation-payment-list-response.md).

## Example Usage

```python
body = PaymentInitiationPaymentListRequest(
    count=10
)

result = payment_initiation_api.payment_initiation_payment_list(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

