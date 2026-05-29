
# Link Token Create Request Account Subtypes

By default, Link will only display account types that are compatible with all products supplied in the `products` parameter of `/link/token/create`. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `"all"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link.

For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#accounts-schema).

For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in the OAuth window.

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestAccountSubtypes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `depository` | [`Depository`](../../doc/models/depository.md) | Optional | A filter to apply to `depository`-type accounts |
| `credit` | [`Credit`](../../doc/models/credit.md) | Optional | A filter to apply to `credit`-type accounts |
| `loan` | [`Loan`](../../doc/models/loan.md) | Optional | A filter to apply to `loan`-type accounts |
| `investment` | [`Investment`](../../doc/models/investment.md) | Optional | A filter to apply to `investment`-type accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "depository": {
    "account_subtypes": [
      "non-taxable brokerage account",
      "other"
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "credit": {
    "account_subtypes": [
      "ugma",
      "utma",
      "variable annuity"
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "loan": {
    "account_subtypes": [
      "checking",
      "savings",
      "money market"
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "investment": {
    "account_subtypes": [
      "consumer",
      "home"
    ],
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

