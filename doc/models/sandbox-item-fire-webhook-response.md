
# Sandbox Item Fire Webhook Response

SandboxItemFireWebhookResponse defines the response schema for `/sandbox/item/fire_webhook`

*This model accepts additional fields of type Any.*

## Structure

`SandboxItemFireWebhookResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_fired` | `bool` | Required | Value is `true`  if the test` webhook_code`  was successfully fired. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_fired": false,
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

