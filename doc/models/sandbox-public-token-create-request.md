
# Sandbox Public Token Create Request

SandboxPublicTokenCreateRequest defines the request schema for `/sandbox/public_token/create`

*This model accepts additional fields of type Any.*

## Structure

`SandboxPublicTokenCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `institution_id` | `str` | Required | The ID of the institution the Item will be associated with |
| `initial_products` | [`List[Products]`](../../doc/models/products.md) | Required | The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.<br><br>**Constraints**: *Minimum Items*: `1` |
| `options` | [`SandboxPublicTokenCreateRequestOptions`](../../doc/models/sandbox-public-token-create-request-options.md) | Optional | An optional set of options to be used when configuring the Item. If specified, must not be `null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id0",
  "secret": "secret4",
  "institution_id": "institution_id6",
  "initial_products": [
    "auth",
    "balance"
  ],
  "options": {
    "webhook": "webhook0",
    "override_username": "override_username0",
    "override_password": "override_password8",
    "transactions": {
      "start_date": "2016-03-13",
      "end_date": "2016-03-13",
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

