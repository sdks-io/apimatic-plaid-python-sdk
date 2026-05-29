
# Sandbox Bank Transfer Fire Webhook Request

Defines the request schema for `/sandbox/bank_transfer/fire_webhook`

*This model accepts additional fields of type Any.*

## Structure

`SandboxBankTransferFireWebhookRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `webhook` | `str` | Required | The URL to which the webhook should be sent. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id2",
  "secret": "secret6",
  "webhook": "webhook8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

