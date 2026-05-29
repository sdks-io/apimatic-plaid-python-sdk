
# Warning

It is possible for an Asset Report to be returned with missing account owner information. In such cases, the Asset Report will contain warning data in the response, indicating why obtaining the owner information failed.

*This model accepts additional fields of type Any.*

## Structure

`Warning`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `warning_type` | `str` | Required | The warning type, which will always be `ASSET_REPORT_WARNING` |
| `warning_code` | `str` | Required | The warning code identifies a specific kind of warning. Currently, the only possible warning code is `OWNERS_UNAVAILABLE`, which indicates that account-owner information is not available. |
| `cause` | [`Cause`](../../doc/models/cause.md) | Required | An error object and associated `item_id` used to identify a specific Item and error when a batch operation operating on multiple Items has encountered an error in one of the Items. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "warning_type": "warning_type4",
  "warning_code": "OWNERS_UNAVAILABLE",
  "cause": {
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

