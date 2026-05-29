
# Transfer User Address in Request

The address associated with the account holder.

*This model accepts additional fields of type Any.*

## Structure

`TransferUserAddressInRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | The street number and name (i.e., "100 Market St."). |
| `city` | `str` | Optional | Ex. "San Francisco" |
| `region` | `str` | Optional | The state or province (e.g., "California"). |
| `postal_code` | `str` | Optional | The postal code (e.g., "94103"). |
| `country` | `str` | Optional | A two-letter country code (e.g., "US"). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "street": "street0",
  "city": "city0",
  "region": "region6",
  "postal_code": "postal_code2",
  "country": "country4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

