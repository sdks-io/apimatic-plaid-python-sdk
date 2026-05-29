
# Sell Type

Selling an investment

*This model accepts additional fields of type Any.*

## Structure

`SellType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distribution` | `str` | Optional | Outflow of assets from a tax-advantaged account |
| `exercise` | `str` | Optional | Exercise of an option or warrant contract |
| `sell` | `str` | Optional | Sell to close or decrease an existing holding |
| `sell_short` | `str` | Optional | Sell to open a short position |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "distribution": "distribution8",
  "exercise": "exercise0",
  "sell": "sell0",
  "sell short": "sell short0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

