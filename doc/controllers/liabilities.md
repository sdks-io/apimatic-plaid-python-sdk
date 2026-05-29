# Liabilities

```python
liabilities_api = client.liabilities
```

## Class Name

`LiabilitiesApi`


# Liabilities Get

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

Find out more here: [/api/products/#liabilitiesget](/api/products/#liabilitiesget)

```python
def liabilities_get(self,
                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LiabilitiesGetRequest`](../../doc/models/liabilities-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LiabilitiesGetResponse`](../../doc/models/liabilities-get-response.md).

## Example Usage

```python
body = LiabilitiesGetRequest(
    access_token='access_token4'
)

result = liabilities_api.liabilities_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

