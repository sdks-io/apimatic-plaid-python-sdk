
# Item Get Response

ItemGetResponse defines the response schema for `/item/get` and `/item/webhook/update`

*This model accepts additional fields of type Any.*

## Structure

`ItemGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`Item`](../../doc/models/item.md) | Required | Metadata about the Item. |
| `status` | [`ItemStatusNullable`](../../doc/models/item-status-nullable.md) | Optional | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "item": {
    "item_id": "item_id2",
    "institution_id": "institution_id0",
    "webhook": "webhook0",
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
    "available_products": [
      "transfer",
      "assets"
    ],
    "billed_products": [
      "deposit_switch",
      "standing_orders"
    ],
    "consent_expiration_time": "2016-03-13T12:52:32.123Z",
    "update_type": "background",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": {
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
  },
  "request_id": "request_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

