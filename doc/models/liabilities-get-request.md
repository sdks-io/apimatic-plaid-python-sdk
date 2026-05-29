
# Liabilities Get Request

LiabilitiesGetRequest defines the request schema for `/liabilities/get`

*This model accepts additional fields of type Any.*

## Structure

`LiabilitiesGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `options` | [`LiabilitiesGetRequestOptions`](../../doc/models/liabilities-get-request-options.md) | Optional | An optional object to filter `/liabilities/get` results. If provided, `options` cannot be null. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id0",
  "secret": "secret6",
  "access_token": "access_token6",
  "options": {
    "account_ids": [
      "account_ids3",
      "account_ids4",
      "account_ids5"
    ],
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

