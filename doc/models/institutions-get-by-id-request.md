
# Institutions Get by Id Request

InstitutionsGetByIdRequest defines the request schema for `/institutions/get_by_id`

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsGetByIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `institution_id` | `str` | Required | The ID of the institution to get details about |
| `country_codes` | [`List[CountryCode]`](../../doc/models/country-code.md) | Required | Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard. |
| `options` | [`InstitutionsGetByIdRequestOptions`](../../doc/models/institutions-get-by-id-request-options.md) | Optional | Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "institution_id": "institution_id2",
  "country_codes": [
    "US",
    "GB",
    "ES"
  ],
  "options": {
    "include_optional_metadata": false,
    "include_status": false,
    "include_auth_metadata": false,
    "include_payment_initiation_metadata": false,
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

