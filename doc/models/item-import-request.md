
# Item Import Request

ItemImportRequest defines the request schema for `/item/import`

*This model accepts additional fields of type Any.*

## Structure

`ItemImportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `products` | [`List[Products]`](../../doc/models/products.md) | Required | Array of product strings<br><br>**Constraints**: *Minimum Items*: `1` |
| `user_auth` | [`ItemImportRequestUserAuth`](../../doc/models/item-import-request-user-auth.md) | Required | Object of user ID and auth token pair, permitting Plaid to aggregate a user’s accounts |
| `options` | [`ItemImportRequestOptions`](../../doc/models/item-import-request-options.md) | Optional | An optional object to configure `/item/import` request. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id0",
  "secret": "secret4",
  "products": [
    "investments",
    "liabilities",
    "payment_initiation"
  ],
  "user_auth": {
    "user_id": "user_id2",
    "auth_token": "auth_token0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "options": {
    "webhook": "webhook0",
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

