
# Standalone Currency Code List

The following currency codes are supported by Plaid.

*This model accepts additional fields of type Any.*

## Structure

`StandaloneCurrencyCodeList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iso_currency_code` | `str` | Required | Plaid supports all ISO 4217 currency codes. |
| `unofficial_currency_code` | [`UnofficialCurrencyCodeList`](../../doc/models/unofficial-currency-code-list.md) | Required | List of unofficial currency codes |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "iso_currency_code": "iso_currency_code8",
  "unofficial_currency_code": {
    "ADA": "ADA4",
    "BAT": "BAT8",
    "BCH": "BCH8",
    "BNB": "BNB4",
    "BTC": "BTC0",
    "BTG": "BTG6",
    "CNH": "CNH4",
    "DASH": "DASH6",
    "DOGE": "DOGE6",
    "ETC": "ETC0",
    "ETH": "ETH6",
    "GBX": "GBX8",
    "LSK": "LSK4",
    "NEO": "NEO8",
    "OMG": "OMG6",
    "QTUM": "QTUM8",
    "USDT": "USDT8",
    "XLM": "XLM2",
    "XMR": "XMR0",
    "XRP": "XRP0",
    "ZEC": "ZEC4",
    "ZRX": "ZRX2",
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

