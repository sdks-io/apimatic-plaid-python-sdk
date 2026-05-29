
# Asset Report Transaction

*This model accepts additional fields of type Any.*

## Structure

`AssetReportTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`TransactionType`](../../doc/models/transaction-type.md) | Optional | Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.<br><br>`digital:` transactions that took place online.<br><br>`place:` transactions that were made at a physical location.<br><br>`special:` transactions that relate to banks, e.g. fees or deposits.<br><br>`unresolved:` transactions that do not fit into the other three types. |
| `pending_transaction_id` | `str` | Optional | The ID of a posted transaction's associated pending transaction, where applicable. |
| `category_id` | `str` | Optional | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).<br><br>If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `category` | `List[str]` | Optional | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).<br><br>If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `location` | [`TransactionLocation`](../../doc/models/transaction-location.md) | Optional | A representation of where a transaction took place |
| `payment_meta` | [`PaymentMeta`](../../doc/models/payment-meta.md) | Optional | Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.<br><br>If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `account_owner` | `str` | Optional | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. |
| `name` | `str` | Optional | The merchant name or transaction description.<br><br>If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `original_description` | `str` | Required | The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`. |
| `account_id` | `str` | Required | The ID of the account in which this transaction occurred. |
| `amount` | `float` | Required | The settled value of the transaction, denominated in the account's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. |
| `iso_currency_code` | `str` | Required | The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null. |
| `unofficial_currency_code` | `str` | Required | The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.<br><br>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. |
| `date` | `date` | Required | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). |
| `pending` | `bool` | Required | When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. |
| `transaction_id` | `str` | Required | The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive. |
| `date_transacted` | `str` | Optional | The date on which the transaction took place, in IS0 8601 format. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_type": "special",
  "pending_transaction_id": "pending_transaction_id6",
  "category_id": "category_id6",
  "category": [
    "category4",
    "category5",
    "category6"
  ],
  "location": {
    "address": "address0",
    "city": "city6",
    "region": "region0",
    "postal_code": "postal_code6",
    "country": "country8",
    "lat": 205.22,
    "lon": 217.68,
    "store_number": "store_number0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "original_description": "original_description0",
  "account_id": "account_id4",
  "amount": 130.94,
  "iso_currency_code": "iso_currency_code4",
  "unofficial_currency_code": "unofficial_currency_code4",
  "date": "2016-03-13",
  "pending": false,
  "transaction_id": "transaction_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

