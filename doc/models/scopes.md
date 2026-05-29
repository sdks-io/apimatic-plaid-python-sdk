
# Scopes

The scopes object

*This model accepts additional fields of type Any.*

## Structure

`Scopes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_access` | [`ProductAccess`](../../doc/models/product-access.md) | Optional | The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed. |
| `accounts` | [`List[AccountAccess]`](../../doc/models/account-access.md) | Optional | - |
| `new_accounts` | `bool` | Optional | Allow access to newly opened accounts as they are opened. If unset, defaults to `true`.<br><br>**Default**: `True` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "new_accounts": true,
  "product_access": {
    "statements": false,
    "identity": false,
    "auth": false,
    "transactions": false,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "accounts": [
    {
      "unique_id": "unique_id6",
      "authorized": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "unique_id": "unique_id6",
      "authorized": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

