
# Item Status

An object with information about the status of the Item.

*This model accepts additional fields of type Any.*

## Structure

`ItemStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `investments` | [`ItemStatusInvestments`](../../doc/models/item-status-investments.md) | Optional | Information about the last successful and failed investments update for the Item. |
| `transactions` | [`ItemStatusTransactions`](../../doc/models/item-status-transactions.md) | Optional | Information about the last successful and failed transactions update for the Item. |
| `last_webhook` | [`ItemStatusLastWebhook`](../../doc/models/item-status-last-webhook.md) | Optional | Information about the last webhook fired for the Item. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "investments": {
    "last_successful_update": "2016-03-13T12:52:32.123Z",
    "last_failed_update": "2016-03-13T12:52:32.123Z",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "transactions": {
    "last_successful_update": "2016-03-13T12:52:32.123Z",
    "last_failed_update": "2016-03-13T12:52:32.123Z",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "last_webhook": {
    "sent_at": "2016-03-13T12:52:32.123Z",
    "code_sent": "code_sent2",
    "exampleAdditionalProperty": {
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

