
# Investments Transactions Get Request

InvestmentsTransactionsGetRequest defines the request schema for `/investments/transactions/get`

*This model accepts additional fields of type Any.*

## Structure

`InvestmentsTransactionsGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `start_date` | `date` | Required | The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. |
| `end_date` | `date` | Required | The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. |
| `options` | [`InvestmentsTransactionsGetRequestOptions`](../../doc/models/investments-transactions-get-request-options.md) | Optional | An optional object to filter `/investments/transactions/get` results. If provided, must be non-`null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id0",
  "secret": "secret6",
  "access_token": "access_token6",
  "start_date": "2016-03-13",
  "end_date": "2016-03-13",
  "options": {
    "account_ids": [
      "account_ids3",
      "account_ids4",
      "account_ids5"
    ],
    "count": 98,
    "offset": 50,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

