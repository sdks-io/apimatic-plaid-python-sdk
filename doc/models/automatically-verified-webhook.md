
# Automatically Verified Webhook

Fired when an Item is verified via automated micro-deposits. We recommend communicating to your users when this event is received to notify them that their account is verified and ready for use.

*This model accepts additional fields of type Any.*

## Structure

`AutomaticallyVerifiedWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `AUTH` |
| `webhook_code` | `str` | Required | `AUTOMATICALLY_VERIFIED` |
| `account_id` | `str` | Required | The `account_id` of the account associated with the webhook |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type2",
  "webhook_code": "webhook_code8",
  "account_id": "account_id0",
  "item_id": "item_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

