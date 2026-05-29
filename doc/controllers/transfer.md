# Transfer

```python
transfer_api = client.transfer
```

## Class Name

`TransferApi`

## Methods

* [Transfer Event Sync](../../doc/controllers/transfer.md#transfer-event-sync)
* [Transfer List](../../doc/controllers/transfer.md#transfer-list)
* [Transfer Get](../../doc/controllers/transfer.md#transfer-get)
* [Transfer Cancel](../../doc/controllers/transfer.md#transfer-cancel)
* [Transfer Create](../../doc/controllers/transfer.md#transfer-create)
* [Transfer Authorization Create](../../doc/controllers/transfer.md#transfer-authorization-create)
* [Transfer Event List](../../doc/controllers/transfer.md#transfer-event-list)


# Transfer Event Sync

`/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.

Find out more here: [/transfer/reference#transfereventsync](/transfer/reference#transfereventsync)

```python
def transfer_event_sync(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferEventSyncRequest`](../../doc/models/transfer-event-sync-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferEventSyncResponse`](../../doc/models/transfer-event-sync-response.md).

## Example Usage

```python
body = TransferEventSyncRequest(
    after_id=50,
    count=25
)

result = transfer_api.transfer_event_sync(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer List

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.

Find out more here: [/transfer/reference#transferlist](/transfer/reference#transferlist)

```python
def transfer_list(self,
                 body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferListRequest`](../../doc/models/transfer-list-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferListResponse`](../../doc/models/transfer-list-response.md).

## Example Usage

```python
body = TransferListRequest(
    count=25,
    offset=0
)

result = transfer_api.transfer_list(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer Get

The `/transfer/get` fetches information about the transfer corresponding to the given `transfer_id`.

Find out more here: [/transfer/reference#transferget](/transfer/reference#transferget)

```python
def transfer_get(self,
                body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferGetRequest`](../../doc/models/transfer-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferGetResponse`](../../doc/models/transfer-get-response.md).

## Example Usage

```python
body = TransferGetRequest(
    transfer_id='transfer_id2'
)

result = transfer_api.transfer_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer Cancel

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/transfer/get` is `true`.

Find out more here: [/transfer/reference#transfercancel](/transfer/reference#transfercancel)

```python
def transfer_cancel(self,
                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferCancelRequest`](../../doc/models/transfer-cancel-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferCancelResponse`](../../doc/models/transfer-cancel-response.md).

## Example Usage

```python
body = TransferCancelRequest(
    transfer_id='transfer_id2'
)

result = transfer_api.transfer_cancel(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "saKrIBuEB9qJZno"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer Create

Use the `/transfer/create` endpoint to initiate a new transfer.

Find out more here: [/transfer/reference#transfercreate](/transfer/reference#transfercreate)

```python
def transfer_create(self,
                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferCreateRequest`](../../doc/models/transfer-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferCreateResponse`](../../doc/models/transfer-create-response.md).

## Example Usage

```python
body = TransferCreateRequest(
    idempotency_key='idempotency_key2',
    access_token='access_token4',
    account_id='account_id8',
    authorization_id='authorization_id2',
    mtype=TransferType1.DEBIT,
    network=TransferNetwork.ACH,
    amount='amount8',
    description='description4',
    ach_class=AchClass.CCD,
    user=TransferUserInRequest(
        legal_name='legal_name8'
    )
)

result = transfer_api.transfer_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer Authorization Create

Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

In Plaid's sandbox environment the decisions will be returned as follows:

- To approve a transfer, make an authorization request with an `amount` less than the available balance in the account.

- To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

- To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

- To permit a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

- To permit a transfer with the rationale code `LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

All username/password combinations other than the ones listed above will result in a decision of permitted and rationale code `ERROR`.

Find out more here: [/transfer/reference#transferauthorizationcreate](/transfer/reference#transferauthorizationcreate)

```python
def transfer_authorization_create(self,
                                 body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferAuthorizationCreateRequest`](../../doc/models/transfer-authorization-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferAuthorizationCreateResponse`](../../doc/models/transfer-authorization-create-response.md).

## Example Usage

```python
body = TransferAuthorizationCreateRequest(
    access_token='access_token4',
    account_id='account_id8',
    mtype=TransferType1.DEBIT,
    network=TransferNetwork.ACH,
    amount='amount8',
    ach_class=AchClass.CCD,
    user=TransferUserInRequest(
        legal_name='legal_name8'
    )
)

result = transfer_api.transfer_authorization_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Transfer Event List

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

Find out more here: [/transfer/reference#transfereventlist](/transfer/reference#transfereventlist)

```python
def transfer_event_list(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferEventListRequest`](../../doc/models/transfer-event-list-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferEventListResponse`](../../doc/models/transfer-event-list-response.md).

## Example Usage

```python
body = TransferEventListRequest(
    count=25,
    offset=0
)

result = transfer_api.transfer_event_list(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

