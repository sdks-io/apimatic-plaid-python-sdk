
# User Permission Revoked Webhook

The `USER_PERMISSION_REVOKED` webhook is fired to when an end user has used the [my.plaid.com portal](https://my.plaid.com) to revoke the permission that they previously granted to access an Item. Once access to an Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must be created for the user.

*This model accepts additional fields of type Any.*

## Structure

`UserPermissionRevokedWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `ITEM` |
| `webhook_code` | `str` | Required | `USER_PERMISSION_REVOKED` |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type0",
  "webhook_code": "webhook_code0",
  "item_id": "item_id6",
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
}
```

