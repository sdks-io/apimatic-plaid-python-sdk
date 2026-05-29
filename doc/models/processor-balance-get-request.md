
# Processor Balance Get Request

ProcessorBalanceGetRequest defines the request schema for `/processor/balance/get`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorBalanceGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `processor_token` | `str` | Required | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>` |
| `options` | [`ProcessorBalanceGetRequestOptions`](../../doc/models/processor-balance-get-request-options.md) | Optional | An optional object to filter `/processor/balance/get` results. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "processor_token": "processor_token6",
  "options": {
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

