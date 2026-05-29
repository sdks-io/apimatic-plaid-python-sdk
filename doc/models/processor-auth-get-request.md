
# Processor Auth Get Request

ProcessorAuthGetRequest defines the request schema for `/processor/auth/get`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorAuthGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `processor_token` | `str` | Required | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "processor_token": "processor_token6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

