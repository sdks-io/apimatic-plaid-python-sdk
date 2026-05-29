
# Loan Account

A loan type account. Supported products for `loan` accounts are: Balance, Liabilities, and Transactions.

*This model accepts additional fields of type Any.*

## Structure

`LoanAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto` | `str` | Required | Auto loan |
| `business` | `str` | Required | Business loan |
| `commercial` | `str` | Required | Commercial loan |
| `construction` | `str` | Required | Construction loan |
| `consumer` | `str` | Required | Consumer loan |
| `home_equity` | `str` | Required | Home Equity Line of Credit (HELOC) |
| `loan` | `str` | Required | General loan |
| `mortgage` | `str` | Required | Mortgage loan |
| `overdraft` | `str` | Required | Pre-approved overdraft account, usually tied to a checking account |
| `line_of_credit` | `str` | Required | Pre-approved line of credit |
| `student` | `str` | Required | Student loan |
| `other` | `str` | Required | Other loan type or unknown loan type |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "auto": "auto2",
  "business": "business4",
  "commercial": "commercial2",
  "construction": "construction2",
  "consumer": "consumer8",
  "home equity": "home equity4",
  "loan": "loan4",
  "mortgage": "mortgage2",
  "overdraft": "overdraft2",
  "line of credit": "line of credit0",
  "student": "student6",
  "other": "other8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

