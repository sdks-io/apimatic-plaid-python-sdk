
# Product Access

The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed.

*This model accepts additional fields of type Any.*

## Structure

`ProductAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statements` | `bool` | Optional | Allow access to statements. If unset, defaults to `true`.<br><br>**Default**: `True` |
| `identity` | `bool` | Optional | Allow access to the Identity product (name, email, phone, address). If unset, defaults to `true`.<br><br>**Default**: `True` |
| `auth` | `bool` | Optional | Allow access to account number details. If unset, defaults to `true`.<br><br>**Default**: `True` |
| `transactions` | `bool` | Optional | Allow access to transaction details. If unset, defaults to `true`.<br><br>**Default**: `True` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "statements": true,
  "identity": true,
  "auth": true,
  "transactions": true,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

