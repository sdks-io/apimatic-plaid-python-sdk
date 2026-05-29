# Accounts

```python
accounts_api = client.accounts
```

## Class Name

`AccountsApi`

## Methods

* [Accounts Get](../../doc/controllers/accounts.md#accounts-get)
* [Accounts Balance Get](../../doc/controllers/accounts.md#accounts-balance-get)


# Accounts Get

The `/accounts/get`  endpoint can be used to retrieve information for any linked Item. Note that some information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are capable of carrying a balance.

This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead.

Find out more here: [/api/accounts/#accountsget](/api/accounts/#accountsget)

```python
def accounts_get(self,
                body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountsGetRequest`](../../doc/models/accounts-get-request.md) | Body, Required | - |

## Response Type

**200**: success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccountsGetResponse`](../../doc/models/accounts-get-response.md).

## Example Usage

```python
body = AccountsGetRequest(
    access_token='string',
    client_id='string',
    secret='string',
    options=AccountsGetRequestOptions(
        account_ids=[
            'string'
        ]
    )
)

result = accounts_api.accounts_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Accounts Balance Get

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link.

Find out more here: [/api/products/#accountsbalanceget](/api/products/#accountsbalanceget)

```python
def accounts_balance_get(self,
                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountsBalanceGetRequest`](../../doc/models/accounts-balance-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccountsGetResponse`](../../doc/models/accounts-get-response.md).

## Example Usage

```python
body = AccountsBalanceGetRequest(
    access_token='string',
    secret='string',
    client_id='string',
    options=AccountsBalanceGetRequestOptions(
        account_ids=[
            'string'
        ]
    )
)

result = accounts_api.accounts_balance_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

