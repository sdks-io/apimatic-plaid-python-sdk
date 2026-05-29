
# Payment Initiation Address

The optional address of the payment recipient. This object is not currently required to make payments from UK institutions and should not be populated, though may be necessary for future European expansion.

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `List[str]` | Required | An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters.<br><br>**Constraints**: *Minimum Items*: `1`, *Minimum Length*: `1` |
| `city` | `str` | Required | The city where the recipient is located. Maximum of 35 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `postal_code` | `str` | Required | The postal code where the recipient is located. Maximum of 16 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `country` | `str` | Required | The ISO 3166-1 alpha-2 country code where the recipient is located.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "street": [
    "street7",
    "street8"
  ],
  "city": "city2",
  "postal_code": "postal_code4",
  "country": "country6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

