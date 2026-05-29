
# Fee Type

Fees on the account, e.g. commission, bookkeeping, options-related.

*This model accepts additional fields of type Any.*

## Structure

`FeeType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_fee` | `str` | Optional | Fees paid for account maintenance |
| `adjustment` | `str` | Optional | Increase or decrease in quantity of item |
| `dividend` | `str` | Optional | Inflow of cash from a dividend |
| `interest` | `str` | Optional | Inflow of cash from interest |
| `interest_receivable` | `str` | Optional | Inflow of cash from interest receivable |
| `long_term_capital_gain` | `str` | Optional | Long-term capital gain received as cash |
| `legal_fee` | `str` | Optional | Fees paid for legal charges or services |
| `management_fee` | `str` | Optional | Fees paid for investment management of a mutual fund or other pooled investment vehicle |
| `margin_expense` | `str` | Optional | Fees paid for maintaining margin debt |
| `non_qualified_dividend` | `str` | Optional | Inflow of cash from a non-qualified dividend |
| `non_resident_tax` | `str` | Optional | Taxes paid on behalf of the investor for non-residency in investment jurisdiction |
| `qualified_dividend` | `str` | Optional | Inflow of cash from a qualified dividend |
| `return_of_principal` | `str` | Optional | Repayment of loan principal |
| `short_term_capital_gain` | `str` | Optional | Short-term capital gain received as cash |
| `stock_distribution` | `str` | Optional | Inflow of stock from a distribution |
| `tax` | `str` | Optional | Taxes paid on behalf of the investor |
| `tax_withheld` | `str` | Optional | Taxes withheld on behalf of the customer |
| `transfer_fee` | `str` | Optional | Fees incurred for transfer of a holding or account |
| `trust_fee` | `str` | Optional | Fees related to adminstration of a trust account |
| `unqualified_gain` | `str` | Optional | Unqualified capital gain received as cash |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account fee": "account fee4",
  "adjustment": "adjustment4",
  "dividend": "dividend4",
  "interest": "interest0",
  "interest receivable": "interest receivable0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

