
# Historical Balance

An object representing a balance held by an account in the past

*This model accepts additional fields of type Any.*

## Structure

`HistoricalBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Required | The date of the calculated historical balance, in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD) |
| `current` | `float` | Required | The total amount of funds in the account, calculated from the `current` balance in the `balance` object by subtracting inflows and adding back outflows according to the posted date of each transaction.<br><br>If the account has any pending transactions, historical balance amounts on or after the date of the earliest pending transaction may differ if retrieved in subsequent Asset Reports as a result of those pending transactions posting. |
| `iso_currency_code` | `str` | Required | The ISO-4217 currency code of the balance. Always `null` if `unofficial_currency_code` is non-`null`. |
| `unofficial_currency_code` | `str` | Required | The unofficial currency code associated with the balance. Always `null` if `iso_currency_code` is non-`null`.<br><br>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "date": "2016-03-13",
  "current": 121.48,
  "iso_currency_code": "iso_currency_code8",
  "unofficial_currency_code": "unofficial_currency_code0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

