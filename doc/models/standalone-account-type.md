
# Standalone Account Type

The schema below describes the various `types` and corresponding `subtypes` that Plaid recognizes and reports for financial institution accounts.

*This model accepts additional fields of type Any.*

## Structure

`StandaloneAccountType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `depository` | [`DepositoryAccount`](../../doc/models/depository-account.md) | Required | An account type holding cash, in which funds are deposited. Supported products for `depository` accounts are: Auth, Balance, Transactions, Identity, Payment Initiation, and Assets. |
| `credit` | [`CreditAccount`](../../doc/models/credit-account.md) | Required | A credit card type account. Supported products for `credit` accounts are: Balance, Transactions, Identity, and Liabilities. |
| `loan` | [`LoanAccount`](../../doc/models/loan-account.md) | Required | A loan type account. Supported products for `loan` accounts are: Balance, Liabilities, and Transactions. |
| `investment` | [`InvestmentAccountSubtype`](../../doc/models/investment-account-subtype.md) | Required | An investment account. Supported products for `investment` accounts are: Balance and Investments. |
| `other` | `str` | Required | Other or unknown account type. Supported products for `other` accounts are: Balance, Transactions, Identity, and Assets. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "depository": {
    "checking": "checking8",
    "savings": "savings0",
    "hsa": "hsa2",
    "cd": "cd6",
    "money market": "money market4",
    "paypal": "paypal6",
    "prepaid": "prepaid4",
    "cash management": "cash management4",
    "ebt": "ebt4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "credit": {
    "credit card": "credit card2",
    "paypal": "paypal4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "loan": {
    "auto": "auto8",
    "business": "business0",
    "commercial": "commercial8",
    "construction": "construction8",
    "consumer": "consumer4",
    "home equity": "home equity0",
    "loan": "loan0",
    "mortgage": "mortgage2",
    "overdraft": "overdraft8",
    "line of credit": "line of credit6",
    "student": "student2",
    "other": "other4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "investment": {
    "529a": "529a8",
    "401a": "401a8",
    "401k": "401k4",
    "403b": "403b6",
    "457b": "457b0",
    "brokerage": "brokerage6",
    "cash isa": "cash isa2",
    "education savings account": "education savings account6",
    "fixed annuity": "fixed annuity2",
    "gic": "gic4",
    "health reimbursement arrangement": "health reimbursement arrangement2",
    "hsa": "hsa6",
    "ira": "ira0",
    "isa": "isa8",
    "keogh": "keogh4",
    "lif": "lif4",
    "life insurance": "life insurance2",
    "lira": "lira8",
    "lrif": "lrif4",
    "lrsp": "lrsp8",
    "mutual fund": "mutual fund0",
    "non-taxable brokerage account": "non-taxable brokerage account2",
    "other": "other6",
    "other annuity": "other annuity6",
    "other insurance": "other insurance8",
    "pension": "pension8",
    "prif": "prif8",
    "profit sharing plan": "profit sharing plan8",
    "qshr": "qshr6",
    "rdsp": "rdsp0",
    "resp": "resp2",
    "retirement": "retirement0",
    "rlif": "rlif6",
    "roth": "roth8",
    "roth 401k": "roth 401k2",
    "rrif": "rrif4",
    "rrsp": "rrsp2",
    "sarsep": "sarsep0",
    "sep ira": "sep ira6",
    "simple ira": "simple ira8",
    "sipp": "sipp2",
    "stock plan": "stock plan8",
    "tfsa": "tfsa8",
    "trust": "trust8",
    "ugma": "ugma4",
    "utma": "utma2",
    "variable annuity": "variable annuity2",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "other": "other6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

