
# Institutions Search Request

InstitutionsSearchRequest defines the request schema for `/institutions/search`

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `query` | `str` | Required | The search query. Institutions with names matching the query are returned |
| `products` | [`List[Products]`](../../doc/models/products.md) | Required | Filter the Institutions based on whether they support all products listed in `products`. Provide `null` to get institutions regardless of supported products. Note that when `auth` is specified as a product, if you are enabled for Instant Match or Automated Micro-deposits, institutions that support those products will be returned even if `auth` is not present in their product array.<br><br>**Constraints**: *Minimum Items*: `1` |
| `country_codes` | [`List[CountryCode]`](../../doc/models/country-code.md) | Required | Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. |
| `options` | [`InstitutionsSearchRequestOptions`](../../doc/models/institutions-search-request-options.md) | Optional | An optional object to filter `/institutions/search` results. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id4",
  "secret": "secret8",
  "query": "query2",
  "products": [
    "balance",
    "identity"
  ],
  "country_codes": [
    "CA",
    "US"
  ],
  "options": {
    "oauth": false,
    "include_optional_metadata": false,
    "include_auth_metadata": false,
    "include_payment_initiation_metadata": false,
    "payment_initiation": {
      "payment_id": "payment_id6",
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

