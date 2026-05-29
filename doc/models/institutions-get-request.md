
# Institutions Get Request

InstitutionsGetRequest defines the request schema for `/institutions/get`

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `count` | `int` | Required | The total number of Institutions to return.<br><br>**Constraints**: `<= 500` |
| `offset` | `int` | Required | The number of Institutions to skip. |
| `country_codes` | [`List[CountryCode]`](../../doc/models/country-code.md) | Required | Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.<br><br>**Constraints**: *Minimum Items*: `1` |
| `options` | [`InstitutionsGetRequestOptions`](../../doc/models/institutions-get-request-options.md) | Optional | An optional object to filter `/institutions/get` results. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id2",
  "secret": "secret6",
  "count": 10,
  "offset": 58,
  "country_codes": [
    "NL",
    "FR",
    "IE"
  ],
  "options": {
    "products": [
      "balance"
    ],
    "routing_numbers": [
      "routing_numbers6"
    ],
    "oauth": false,
    "include_optional_metadata": false,
    "include_auth_metadata": false,
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

