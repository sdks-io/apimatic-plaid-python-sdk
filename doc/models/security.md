
# Security

Contains details about a security

*This model accepts additional fields of type Any.*

## Structure

`Security`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `security_id` | `str` | Required | A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid identifiers, the `security_id` is case sensitive. |
| `isin` | `str` | Required | 12-character ISIN, a globally unique securities identifier. |
| `cusip` | `str` | Required | 9-character CUSIP, an identifier assigned to North American securities. |
| `sedol` | `str` | Required | 7-character SEDOL, an identifier assigned to securities in the UK. |
| `institution_security_id` | `str` | Required | An identifier given to the security by the institution |
| `institution_id` | `str` | Required | If `institution_security_id` is present, this field indicates the Plaid `institution_id` of the institution to whom the identifier belongs. |
| `proxy_security_id` | `str` | Required | In certain cases, Plaid will provide the ID of another security whose performance resembles this security, typically when the original security has low volume, or when a private security can be modeled with a publicly traded security. |
| `name` | `str` | Required | A descriptive name for the security, suitable for display. |
| `ticker_symbol` | `str` | Required | The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available. |
| `is_cash_equivalent` | `bool` | Required | Indicates that a security is a highly liquid asset and can be treated like cash. |
| `mtype` | `str` | Required | The security type of the holding. Valid security types are:<br><br>`cash`: Cash, currency, and money market funds<br><br>`derivative`: Options, warrants, and other derivative instruments<br><br>`equity`: Domestic and foreign equities<br><br>`etf`: Multi-asset exchange-traded investment funds<br><br>`fixed income`: Bonds and certificates of deposit (CDs)<br><br>`loan`: Loans and loan receivables.<br><br>`mutual fund`: Open- and closed-end vehicles pooling funds of multiple investors.<br><br>`other`: Unknown or other investment types |
| `close_price` | `float` | Required | Price of the security at the close of the previous trading session. `null` for non-public securities. If the security is a foreign currency or a cryptocurrency this field will be updated daily and will be priced in USD. |
| `close_price_as_of` | `date` | Required | Date for which `close_price` is accurate. Always `null` if `close_price` is `null`. |
| `iso_currency_code` | `str` | Required | The ISO-4217 currency code of the price given. Always `null` if `unofficial_currency_code` is non-`null`. |
| `unofficial_currency_code` | `str` | Required | The unofficial currency code associated with the security. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.<br><br>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "security_id": "security_id0",
  "isin": "isin0",
  "cusip": "cusip8",
  "sedol": "sedol4",
  "institution_security_id": "institution_security_id2",
  "institution_id": "institution_id8",
  "proxy_security_id": "proxy_security_id2",
  "name": "name0",
  "ticker_symbol": "ticker_symbol4",
  "is_cash_equivalent": false,
  "type": "type0",
  "close_price": 53.98,
  "close_price_as_of": "2016-03-13",
  "iso_currency_code": "iso_currency_code6",
  "unofficial_currency_code": "unofficial_currency_code2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

