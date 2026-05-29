
# Taxpayer Id

*This model accepts additional fields of type Any.*

## Structure

`TaxpayerId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_type` | `str` | Optional | Type of ID, e.g. 'SSN' |
| `last_4_digits` | `str` | Optional | Last 4 digits of unique number of ID.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "id_type": "id_type4",
  "last_4_digits": "last_4_digits0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

