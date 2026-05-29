
# Investments Holdings Get Request

InvestmentsHoldingsGetRequest defines the request schema for `/investments/holdings/get`

*This model accepts additional fields of type Any.*

## Structure

`InvestmentsHoldingsGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `options` | [`InvestmentHoldingsGetRequestOptions`](../../doc/models/investment-holdings-get-request-options.md) | Optional | An optional object to filter `/investments/holdings/get` results. If provided, must not be `null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id0",
  "secret": "secret4",
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

