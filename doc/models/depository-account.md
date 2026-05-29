
# Depository Account

An account type holding cash, in which funds are deposited. Supported products for `depository` accounts are: Auth, Balance, Transactions, Identity, Payment Initiation, and Assets.

*This model accepts additional fields of type Any.*

## Structure

`DepositoryAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checking` | `str` | Required | Checking account |
| `savings` | `str` | Required | Savings account |
| `hsa` | `str` | Required | Health Savings Account (US only) that can only hold cash |
| `cd` | `str` | Required | Certificate of deposit account |
| `money_market` | `str` | Required | Money market account |
| `paypal` | `str` | Required | PayPal depository account |
| `prepaid` | `str` | Required | Prepaid debit card |
| `cash_management` | `str` | Required | A cash management account, typically a cash account at a brokerage |
| `ebt` | `str` | Required | An Electronic Benefit Transfer (EBT) account, used by certain public assistance programs to distribute funds (US only) |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "checking": "checking2",
  "savings": "savings4",
  "hsa": "hsa2",
  "cd": "cd0",
  "money market": "money market8",
  "paypal": "paypal2",
  "prepaid": "prepaid8",
  "cash management": "cash management8",
  "ebt": "ebt0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

