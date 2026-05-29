# Investments

```python
investments_api = client.investments
```

## Class Name

`InvestmentsApi`

## Methods

* [Investments Transactions Get](../../doc/controllers/investments.md#investments-transactions-get)
* [Investments Holdings Get](../../doc/controllers/investments.md#investments-holdings-get)


# Investments Transactions Get

The `/investments/transactions/get` endpoint allows developers to retrieve user-authorized transaction data for investment accounts.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

Find out more here: [/api/products/#investmentstransactionsget](/api/products/#investmentstransactionsget)

```python
def investments_transactions_get(self,
                                body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvestmentsTransactionsGetRequest`](../../doc/models/investments-transactions-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvestmentsTransactionsGetResponse`](../../doc/models/investments-transactions-get-response.md).

## Example Usage

```python
body = InvestmentsTransactionsGetRequest(
    access_token='access_token4',
    start_date=dateutil.parser.parse('2016-03-13').date(),
    end_date=dateutil.parser.parse('2016-03-13').date()
)

result = investments_api.investments_transactions_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Investments Holdings Get

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

Find out more here: [/api/products/#investmentsholdingsget](/api/products/#investmentsholdingsget)

```python
def investments_holdings_get(self,
                            body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InvestmentsHoldingsGetRequest`](../../doc/models/investments-holdings-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvestmentsHoldingsGetResponse`](../../doc/models/investments-holdings-get-response.md).

## Example Usage

```python
body = InvestmentsHoldingsGetRequest(
    access_token='access_token4'
)

result = investments_api.investments_holdings_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

