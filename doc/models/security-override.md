
# Security Override

Specify the security associated with the holding or investment transaction. When inputting custom security data to the Sandbox, Plaid will perform post-data-retrieval normalization and enrichment. These processes may cause the data returned by the Sandbox to be slightly different from the data you input. An ISO-4217 currency code and a security identifier (`ticker_symbol`, `cusip`, `isin`, or `sedol`) are required.

*This model accepts additional fields of type Any.*

## Structure

`SecurityOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `isin` | `str` | Optional | 12-character ISIN, a globally unique securities identifier. |
| `cusip` | `str` | Optional | 9-character CUSIP, an identifier assigned to North American securities. |
| `sedol` | `str` | Optional | 7-character SEDOL, an identifier assigned to securities in the UK. |
| `name` | `str` | Optional | A descriptive name for the security, suitable for display. |
| `ticker_symbol` | `str` | Optional | The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available. |
| `currency` | `str` | Optional | Either a valid `iso_currency_code` or `unofficial_currency_code` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "isin": "isin6",
  "cusip": "cusip2",
  "sedol": "sedol2",
  "name": "name4",
  "ticker_symbol": "ticker_symbol0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

