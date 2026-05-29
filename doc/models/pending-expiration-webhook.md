
# Pending Expiration Webhook

Fired when an Item’s access consent is expiring in 7 days. Some Items have explicit expiration times and we try to relay this when possible to reduce service disruption. This can be resolved by having the user go through Link’s update mode.

*This model accepts additional fields of type Any.*

## Structure

`PendingExpirationWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `ITEM` |
| `webhook_code` | `str` | Required | `PENDING_EXPIRATION` |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `consent_expiration_time` | `datetime` | Required | The date and time at which the Item's access consent will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type4",
  "webhook_code": "webhook_code6",
  "item_id": "item_id0",
  "consent_expiration_time": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

