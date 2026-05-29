
# Holdings Default Update Webhook

Fired when new or updated holdings have been detected on an investment account. The webhook typically fires once per day, after market close, in response to any newly added holdings or price changes to existing holdings.

*This model accepts additional fields of type Any.*

## Structure

`HoldingsDefaultUpdateWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `HOLDINGS` |
| `webhook_code` | `str` | Required | `DEFAULT_UPDATE` |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `new_holdings` | `float` | Required | The number of new holdings reported since the last time this webhook was fired. |
| `updated_holdings` | `float` | Required | The number of updated holdings reported since the last time this webhook was fired. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type6",
  "webhook_code": "webhook_code4",
  "item_id": "item_id2",
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
  "new_holdings": 166.22,
  "updated_holdings": 140.52,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

