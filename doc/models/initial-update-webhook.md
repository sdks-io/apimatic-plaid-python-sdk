
# Initial Update Webhook

Fired when an Item's initial transaction pull is completed. Once this webhook has been fired, transaction data for the most recent 30 days can be fetched for the Item. If [Account Select v2](https://plaid.com/docs/link/customization/#account-select) is enabled, this webhook will also be fired if account selections for the Item are updated, with `num_transactions` set to the number of net new transactions pulled after the account selection update.

*This model accepts additional fields of type Any.*

## Structure

`InitialUpdateWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `TRANSACTIONS` |
| `webhook_code` | `str` | Required | `INITIAL_UPDATE` |
| `error` | `str` | Optional | The error code associated with the webhook. |
| `new_transactions` | `float` | Required | The number of new, unfetched transactions available. |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type2",
  "webhook_code": "webhook_code2",
  "error": "error2",
  "new_transactions": 168.68,
  "item_id": "item_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

