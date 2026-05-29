
# Accounts Balance Get Request

AccountsBalanceGetRequest defines the request schema for `/accounts/balance/get`

*This model accepts additional fields of type Any.*

## Structure

`AccountsBalanceGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `options` | [`AccountsBalanceGetRequestOptions`](../../doc/models/accounts-balance-get-request-options.md) | Optional | An optional object to filter `/accounts/balance/get` results. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "access_token": "access_token2",
  "secret": "secret0",
  "client_id": "client_id6",
  "options": {
    "account_ids": [
      "account_ids3",
      "account_ids4",
      "account_ids5"
    ],
    "min_last_updated_datetime": "2016-03-13T12:52:32.123Z",
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

