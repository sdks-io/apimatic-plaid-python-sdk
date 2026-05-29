
# Signal Evaluate Core Attributes

The core attributes object contains additional data that can be used to assess the ACH return risk, such as past ACH return events, balance/transaction history, the Item’s connection history in the Plaid network, and identity change history.

*This model accepts additional fields of type Any.*

## Structure

`SignalEvaluateCoreAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unauthorized_transactions_count_7_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited. |
| `unauthorized_transactions_count_30_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited. |
| `unauthorized_transactions_count_60_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited. |
| `unauthorized_transactions_count_90_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited. |
| `nsf_overdraft_transactions_count_7_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited. |
| `nsf_overdraft_transactions_count_30_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited. |
| `nsf_overdraft_transactions_count_60_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited. |
| `nsf_overdraft_transactions_count_90_d` | `int` | Optional | We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited. |
| `days_since_first_plaid_connection` | `int` | Optional | The number of days since the first time the Item was connected to an application via Plaid |
| `plaid_connections_count_7_d` | `int` | Optional | The number of times the Item has been connected to applications via Plaid over the past 7 days |
| `plaid_connections_count_30_d` | `int` | Optional | The number of times the Item has been connected to applications via Plaid over the past 30 days |
| `total_plaid_connections_count` | `int` | Optional | The total number of times the Item has been connected to applications via Plaid |
| `is_savings_or_money_market_account` | `bool` | Optional | Indicates if the ACH transaction funding account is a savings/money market account |
| `total_credit_transactions_amount_10_d` | `float` | Optional | The total credit (inflow) transaction amount over the past 10 days from the account that will be debited |
| `total_debit_transactions_amount_10_d` | `float` | Optional | The total debit (outflow) transaction amount over the past 10 days from the account that will be debited |
| `p_50_credit_transactions_amount_28_d` | `float` | Optional | The 50th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited |
| `p_50_debit_transactions_amount_28_d` | `float` | Optional | The 50th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited |
| `p_95_credit_transactions_amount_28_d` | `float` | Optional | The 95th percentile of all credit (inflow) transaction amounts over the past 28 days from the account that will be debited |
| `p_95_debit_transactions_amount_28_d` | `float` | Optional | The 95th percentile of all debit (outflow) transaction amounts over the past 28 days from the account that will be debited |
| `days_with_negative_balance_count_90_d` | `int` | Optional | The number of days within the past 90 days when the account that will be debited had a negative end-of-day available balance |
| `p_90_eod_balance_30_d` | `float` | Optional | The 90th percentile of the end-of-day available balance over the past 30 days of the account that will be debited |
| `p_90_eod_balance_60_d` | `float` | Optional | The 90th percentile of the end-of-day available balance over the past 60 days of the account that will be debited |
| `p_90_eod_balance_90_d` | `float` | Optional | The 90th percentile of the end-of-day available balance over the past 90 days of the account that will be debited |
| `p_10_eod_balance_30_d` | `float` | Optional | The 10th percentile of the end-of-day available balance over the past 30 days of the account that will be debited |
| `p_10_eod_balance_60_d` | `float` | Optional | The 10th percentile of the end-of-day available balance over the past 60 days of the account that will be debited |
| `p_10_eod_balance_90_d` | `float` | Optional | The 10th percentile of the end-of-day available balance over the past 90 days of the account that will be debited |
| `available_balance` | `float` | Optional | Available balance, as of the `balance_last_updated` time. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account. |
| `current_balance` | `float` | Optional | Current balance, as of the `balance_last_updated` time. The current balance is the total amount of funds in the account. |
| `balance_last_updated` | `datetime` | Optional | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DDTHH:mm:ssZ) indicating the last time that the balance for the given account has been updated. |
| `phone_change_count_28_d` | `int` | Optional | The number of times the account's phone numbers on file have changed over the past 28 days |
| `phone_change_count_90_d` | `int` | Optional | The number of times the account's phone numbers on file have changed over the past 90 days |
| `email_change_count_28_d` | `int` | Optional | The number of times the account's email addresses on file have changed over the past 28 days |
| `email_change_count_90_d` | `int` | Optional | The number of times the account's email addresses on file have changed over the past 90 days |
| `address_change_count_28_d` | `int` | Optional | The number of times the account's addresses on file have changed over the past 28 days |
| `address_change_count_90_d` | `int` | Optional | The number of times the account's addresses on file have changed over the past 90 days |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "unauthorized_transactions_count_7d": 214,
  "unauthorized_transactions_count_30d": 98,
  "unauthorized_transactions_count_60d": 22,
  "unauthorized_transactions_count_90d": 138,
  "nsf_overdraft_transactions_count_7d": 70,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

