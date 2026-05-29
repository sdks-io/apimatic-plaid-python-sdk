
# Transaction

A representation of a transaction

*This model accepts additional fields of type Any.*

## Structure

`Transaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`TransactionType`](../../doc/models/transaction-type.md) | Optional | Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.<br><br>`digital:` transactions that took place online.<br><br>`place:` transactions that were made at a physical location.<br><br>`special:` transactions that relate to banks, e.g. fees or deposits.<br><br>`unresolved:` transactions that do not fit into the other three types. |
| `pending_transaction_id` | `str` | Required | The ID of a posted transaction's associated pending transaction, where applicable. |
| `category_id` | `str` | Required | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).<br><br>If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `category` | `List[str]` | Required | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).<br><br>If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `location` | [`TransactionLocation`](../../doc/models/transaction-location.md) | Required | A representation of where a transaction took place |
| `payment_meta` | [`PaymentMeta`](../../doc/models/payment-meta.md) | Required | Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.<br><br>If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `account_owner` | `str` | Required | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. |
| `name` | `str` | Required | The merchant name or transaction description.<br><br>If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights. |
| `original_description` | `str` | Optional | The string returned by the financial institution to describe the transaction. For transactions returned by `/transactions/get`, this field is in beta and will be omitted unless the client is both enrolled in the closed beta program and has set `options.include_original_description` to `true`. |
| `account_id` | `str` | Required | The ID of the account in which this transaction occurred. |
| `amount` | `float` | Required | The settled value of the transaction, denominated in the account's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. |
| `iso_currency_code` | `str` | Required | The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null. |
| `unofficial_currency_code` | `str` | Required | The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.<br><br>See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s. |
| `date` | `date` | Required | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). |
| `pending` | `bool` | Required | When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. |
| `transaction_id` | `str` | Required | The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive. |
| `payment_channel` | [`PaymentChannel`](../../doc/models/payment-channel.md) | Required | The channel used to make a payment.<br>`online:` transactions that took place online.<br><br>`in store:` transactions that were made at a physical location.<br><br>`other:` transactions that relate to banks, e.g. fees or deposits.<br><br>This field replaces the `transaction_type` field. |
| `merchant_name` | `str` | Required | The merchant name, as extracted by Plaid from the `name` field. |
| `authorized_date` | `date` | Required | The date that the transaction was authorized. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DD` ). |
| `authorized_datetime` | `datetime` | Required | Date and time when a transaction was authorized in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ).<br><br>This field is only populated for UK institutions. For institutions in other countries, will be `null`. |
| `datetime` | `datetime` | Required | Date and time when a transaction was posted in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ( `YYYY-MM-DDTHH:mm:ssZ` ).<br><br>This field is only populated for UK institutions. For institutions in other countries, will be `null`. |
| `check_number` | `str` | Required | The check number of the transaction. This field is only populated for check transactions. |
| `transaction_code` | [`TransactionCode`](../../doc/models/transaction-code.md) | Required | An identifier classifying the transaction type.<br><br>This field is only populated for European institutions. For institutions in the US and Canada, this field is set to `null`.<br><br>`adjustment:` Bank adjustment<br><br>`atm:` Cash deposit or withdrawal via an automated teller machine<br><br>`bank charge:` Charge or fee levied by the institution<br><br>`bill payment`: Payment of a bill<br><br>`cash:` Cash deposit or withdrawal<br><br>`cashback:` Cash withdrawal while making a debit card purchase<br><br>`cheque:` Document ordering the payment of money to another person or organization<br><br>`direct debit:` Automatic withdrawal of funds initiated by a third party at a regular interval<br><br>`interest:` Interest earned or incurred<br><br>`purchase:` Purchase made with a debit or credit card<br><br>`standing order:` Payment instructed by the account holder to a third party at a regular interval<br><br>`transfer:` Transfer of money between accounts |
| `personal_finance_category` | [`PersonalFinanceCategory2`](../../doc/models/personal-finance-category-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_type": "digital",
  "pending_transaction_id": "pending_transaction_id2",
  "category_id": "category_id4",
  "category": [
    "category8",
    "category7",
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
  "payment_meta": {
    "reference_number": "reference_number2",
    "ppd_id": "ppd_id4",
    "payee": "payee2",
    "by_order_of": "by_order_of8",
    "payer": "payer2",
    "payment_method": "payment_method4",
    "payment_processor": "payment_processor4",
    "reason": "reason8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "account_owner": "account_owner2",
  "name": "name4",
  "original_description": "original_description2",
  "account_id": "account_id6",
  "amount": 20.56,
  "iso_currency_code": "iso_currency_code2",
  "unofficial_currency_code": "unofficial_currency_code6",
  "date": "2016-03-13",
  "pending": false,
  "transaction_id": "transaction_id2",
  "payment_channel": "online",
  "merchant_name": "merchant_name6",
  "authorized_date": "2016-03-13",
  "authorized_datetime": "2016-03-13T12:52:32.123Z",
  "datetime": "2016-03-13T12:52:32.123Z",
  "check_number": "check_number4",
  "transaction_code": "interest",
  "personal_finance_category": {
    "primary": "primary4",
    "detailed": "detailed4",
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

