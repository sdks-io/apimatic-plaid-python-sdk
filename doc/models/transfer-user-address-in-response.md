
# Transfer User Address in Response

The address associated with the account holder.

*This model accepts additional fields of type Any.*

## Structure

`TransferUserAddressInResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Required | The street number and name (i.e., "100 Market St."). |
| `city` | `str` | Required | Ex. "San Francisco" |
| `region` | `str` | Required | The state or province (e.g., "California"). |
| `postal_code` | `str` | Required | The postal code (e.g., "94103"). |
| `country` | `str` | Required | A two-letter country code (e.g., "US"). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "street": "street8",
  "city": "city2",
  "region": "region4",
  "postal_code": "postal_code0",
  "country": "country2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

