
# Processor Token Create Request

ProcessorTokenCreateRequest defines the request schema for `/processor/token/create`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorTokenCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `account_id` | `str` | Required | The `account_id` value obtained from the `onSuccess` callback in Link |
| `processor` | [`Processor`](../../doc/models/processor.md) | Required | The processor you are integrating with. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id4",
  "secret": "secret8",
  "access_token": "access_token0",
  "account_id": "account_id4",
  "processor": "unit",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

