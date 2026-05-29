
# Buy Type

Buying an investment

*This model accepts additional fields of type Any.*

## Structure

`BuyType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assignment` | `str` | Optional | Assignment of short option holding |
| `contribution` | `str` | Optional | Inflow of assets into a tax-advantaged account |
| `buy` | `str` | Optional | Purchase to open or increase a position |
| `buy_to_cover` | `str` | Optional | Purchase to close a short position |
| `dividend_reinvestment` | `str` | Optional | Purchase using proceeds from a cash dividend |
| `interest_reinvestment` | `str` | Optional | Purchase using proceeds from a cash interest payment |
| `long_term_capital_gain_reinvestment` | `str` | Optional | Purchase using long-term capital gain cash proceeds |
| `short_term_capital_gain_reinvestment` | `str` | Optional | Purchase using short-term capital gain cash proceeds |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "assignment": "assignment8",
  "contribution": "contribution2",
  "buy": "buy6",
  "buy to cover": "buy to cover8",
  "dividend reinvestment": "dividend reinvestment2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

