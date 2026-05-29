
# Transfer Type

Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer

*This model accepts additional fields of type Any.*

## Structure

`TransferType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignment` | `str` | Optional | Assignment of short option holding |
| `adjustment` | `str` | Optional | Increase or decrease in quantity of item |
| `exercise` | `str` | Optional | Exercise of an option or warrant contract |
| `expire` | `str` | Optional | Expiration of an option or warrant contract |
| `merger` | `str` | Optional | Stock exchanged at a pre-defined ratio as part of a merger between companies |
| `spin_off` | `str` | Optional | Inflow of stock from spin-off transaction of an existing holding |
| `split` | `str` | Optional | Inflow of stock from a forward split of an existing holding |
| `transfer` | `str` | Optional | Movement of assets into or out of an account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "assignment": "assignment8",
  "adjustment": "adjustment6",
  "exercise": "exercise4",
  "expire": "expire4",
  "merger": "merger2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

