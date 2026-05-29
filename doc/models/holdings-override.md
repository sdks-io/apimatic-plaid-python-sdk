
# Holdings Override

Specify the holdings on the account.

*This model accepts additional fields of type Any.*

## Structure

`HoldingsOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `institution_price` | `float` | Required | The last price given by the institution for this security |
| `institution_price_as_of` | `date` | Optional | The date at which `institution_price` was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date. |
| `cost_basis` | `float` | Optional | The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported. |
| `quantity` | `float` | Required | The total quantity of the asset held, as reported by the financial institution. |
| `currency` | `str` | Required | Either a valid `iso_currency_code` or `unofficial_currency_code` |
| `security` | [`SecurityOverride`](../../doc/models/security-override.md) | Required | Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "institution_price": 221.38,
  "institution_price_as_of": "2016-03-13",
  "cost_basis": 210.9,
  "quantity": 219.38,
  "currency": "currency2",
  "security": {
    "isin": "isin4",
    "cusip": "cusip4",
    "sedol": "sedol0",
    "name": "name6",
    "ticker_symbol": "ticker_symbol8",
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

