
# Item Import Request User Auth

Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts

*This model accepts additional fields of type Any.*

## Structure

`ItemImportRequestUserAuth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Required | Opaque user identifier |
| `auth_token` | `str` | Required | Authorization token Plaid will use to aggregate this user’s accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "user_id": "user_id2",
  "auth_token": "auth_token0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

