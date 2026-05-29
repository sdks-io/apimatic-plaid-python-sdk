
# Paystub Ytd Details

The amount of income earned year to date, as based on paystub data.

*This model accepts additional fields of type Any.*

## Structure

`PaystubYtdDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gross_earnings` | `float` | Optional | Year-to-date gross earnings. |
| `net_earnings` | `float` | Optional | Year-to-date net (take home) earnings. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "gross_earnings": 11.24,
  "net_earnings": 55.46,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

