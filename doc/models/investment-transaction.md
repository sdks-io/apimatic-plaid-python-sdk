
# Investment Transaction

A transaction within an investment account.

*This model accepts additional fields of type Any.*

## Structure

`InvestmentTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `investment_transaction_id` | `str` | Required | The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive. |
| `cancel_transaction_id` | `str` | Optional | A legacy field formerly used internally by Plaid to identify certain canceled transactions. |
| `account_id` | `str` | Required | The `account_id` of the account against which this transaction posted. |
| `security_id` | `str` | Required | The `security_id` to which this transaction is related. |
| `date` | `date` | Required | The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction, or transacted date for pending transactions. |
| `name` | `str` | Required | The institution’s description of the transaction. |
| `quantity` | `float` | Required | The number of units of the security involved in this transaction. |
| `amount` | `float` | Required | The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities. |
| `price` | `float` | Required | The price of the security at which this transaction occurred. |
| `fees` | `float` | Required | The combined value of all fees applied to this transaction |
| `mtype` | [`Type4`](../../doc/models/type-4.md) | Required | Value is one of the following:<br>`buy`: Buying an investment<br>`sell`: Selling an investment<br>`cancel`: A cancellation of a pending transaction<br>`cash`: Activity that modifies a cash position<br>`fee`: A fee on the account<br>`transfer`: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer<br><br>For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema). |
| `subtype` | [`Subtype`](../../doc/models/subtype.md) | Required | For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema). |
| `iso_currency_code` | `str` | Required | The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`. |
| `unofficial_currency_code` | `str` | Required | The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.<br><br>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "investment_transaction_id": "investment_transaction_id8",
  "cancel_transaction_id": "cancel_transaction_id4",
  "account_id": "account_id4",
  "security_id": "security_id2",
  "date": "2016-03-13",
  "name": "name2",
  "quantity": 34.58,
  "amount": 84.64,
  "price": 66.1,
  "fees": 139.52,
  "type": "fee",
  "subtype": "spin off",
  "iso_currency_code": "iso_currency_code4",
  "unofficial_currency_code": "unofficial_currency_code4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

