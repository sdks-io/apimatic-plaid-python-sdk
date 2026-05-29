
# Employers Search Request

EmployersSearchRequest defines the request schema for `/employers/search`.

*This model accepts additional fields of type Any.*

## Structure

`EmployersSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `query` | `str` | Required | The employer name to be searched for. |
| `products` | `List[str]` | Required | The Plaid products the returned employers should support. Currently, this field must be set to `"deposit_switch"`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "query": "query4",
  "products": [
    "products2",
    "products3",
    "products4"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

