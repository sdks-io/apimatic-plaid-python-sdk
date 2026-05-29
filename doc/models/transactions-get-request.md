
# Transactions Get Request

TransactionsGetRequest defines the request schema for `/transactions/get`

*This model accepts additional fields of type Any.*

## Structure

`TransactionsGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `options` | [`TransactionsGetRequestOptions`](../../doc/models/transactions-get-request-options.md) | Optional | An optional object to be used with the request. If specified, `options` must not be `null`. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `start_date` | `date` | Required | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. |
| `end_date` | `date` | Required | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id2",
  "options": {
    "account_ids": [
      "account_ids3",
      "account_ids4",
      "account_ids5"
    ],
    "count": 98,
    "offset": 50,
    "include_original_description": false,
    "include_personal_finance_category_beta": false,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "access_token": "access_token8",
  "secret": "secret6",
  "start_date": "2016-03-13",
  "end_date": "2016-03-13",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

