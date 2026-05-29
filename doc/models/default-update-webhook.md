
# Default Update Webhook

Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.

*This model accepts additional fields of type Any.*

## Structure

`DefaultUpdateWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `TRANSACTIONS` |
| `webhook_code` | `str` | Required | `DEFAULT_UPDATE` |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `new_transactions` | `float` | Required | The number of new transactions detected since the last time this webhook was fired. |
| `item_id` | `str` | Required | The `item_id` of the Item the webhook relates to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type4",
  "webhook_code": "webhook_code6",
  "error": {
    "error_type": "RECAPTCHA_ERROR",
    "error_code": "error_code6",
    "error_message": "error_message6",
    "display_message": "display_message8",
    "request_id": "request_id4",
    "causes": [
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "status": 217.06,
    "documentation_url": "documentation_url6",
    "suggested_action": "suggested_action0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "new_transactions": 152.4,
  "item_id": "item_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

