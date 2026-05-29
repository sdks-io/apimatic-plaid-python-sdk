
# Cash Type

Activity that modifies a cash position

*This model accepts additional fields of type Any.*

## Structure

`CashType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_fee` | `str` | Optional | Fees paid for account maintenance |
| `contribution` | `str` | Optional | Inflow of assets into a tax-advantaged account |
| `deposit` | `str` | Optional | Inflow of cash into an account |
| `dividend` | `str` | Optional | Inflow of cash from a dividend |
| `stock_distribution` | `str` | Optional | Inflow of stock from a distribution |
| `interest` | `str` | Optional | Inflow of cash from interest |
| `legal_fee` | `str` | Optional | Fees paid for legal charges or services |
| `long_term_capital_gain` | `str` | Optional | Long-term capital gain received as cash |
| `management_fee` | `str` | Optional | Fees paid for investment management of a mutual fund or other pooled investment vehicle |
| `margin_expense` | `str` | Optional | Fees paid for maintaining margin debt |
| `non_qualified_dividend` | `str` | Optional | Inflow of cash from a non-qualified dividend |
| `non_resident_tax` | `str` | Optional | Taxes paid on behalf of the investor for non-residency in investment jurisdiction |
| `pending_credit` | `str` | Optional | Pending inflow of cash |
| `pending_debit` | `str` | Optional | Pending outflow of cash |
| `qualified_dividend` | `str` | Optional | Inflow of cash from a qualified dividend |
| `short_term_capital_gain` | `str` | Optional | Short-term capital gain received as cash |
| `tax` | `str` | Optional | Taxes paid on behalf of the investor |
| `tax_withheld` | `str` | Optional | Taxes withheld on behalf of the customer |
| `transfer_fee` | `str` | Optional | Fees incurred for transfer of a holding or account |
| `trust_fee` | `str` | Optional | Fees related to adminstration of a trust account |
| `unqualified_gain` | `str` | Optional | Unqualified capital gain received as cash |
| `withdrawal` | `str` | Optional | Outflow of cash from an account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account fee": "account fee6",
  "contribution": "contribution0",
  "deposit": "deposit6",
  "dividend": "dividend6",
  "stock distribution": "stock distribution2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

