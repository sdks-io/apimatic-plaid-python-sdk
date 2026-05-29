
# Liabilities Default Update Webhook

The webhook of type `LIABILITIES` and code `DEFAULT_UPDATE` will be fired when new or updated liabilities have been detected on a liabilities item.

*This model accepts additional fields of type Any.*

## Structure

`LiabilitiesDefaultUpdateWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `LIABILITIES` |
| `webhook_code` | `str` | Required | `DEFAULT_UPDATE` |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `error` | [`Error`](../../doc/models/error.md) | Required | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `account_ids_with_new_liabilities` | `List[str]` | Required | An array of `account_id`'s for accounts that contain new liabilities. |
| `account_ids_with_updated_liabilities` | `Dict[str, Any]` | Required | An object with keys of `account_id`'s that are mapped to their respective liabilities fields that changed.<br><br>Example: `{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["past_amount_due"] }` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type8",
  "webhook_code": "webhook_code8",
  "item_id": "item_id4",
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
  "account_ids_with_new_liabilities": [
    "account_ids_with_new_liabilities7"
  ],
  "account_ids_with_updated_liabilities": {
    "key0": {
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

