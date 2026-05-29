
# Account Type

`investment:` Investment account

`credit:` Credit card

`depository:` Depository account

`loan:` Loan account

`brokerage`: An investment account. Used for `/assets/` endpoints only; other endpoints use `investment`.

`other:` Non-specified account type

See the [Account type schema](https://plaid.com/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.

*This model accepts additional fields of type Any.*

## Enumeration

`AccountType`

## Fields

| Name |
|  --- |
| `INVESTMENT` |
| `CREDIT` |
| `DEPOSITORY` |
| `LOAN` |
| `BROKERAGE` |
| `OTHER` |

