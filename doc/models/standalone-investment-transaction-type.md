
# Standalone Investment Transaction Type

Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash will appear as negative amounts, outflow of cash will appear as positive amounts.

*This model accepts additional fields of type Any.*

## Structure

`StandaloneInvestmentTransactionType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `buy` | [`BuyType`](../../doc/models/buy-type.md) | Required | Buying an investment |
| `sell` | [`SellType`](../../doc/models/sell-type.md) | Required | Selling an investment |
| `cancel` | `str` | Required | A cancellation of a pending transaction |
| `cash` | [`CashType`](../../doc/models/cash-type.md) | Required | Activity that modifies a cash position |
| `fee` | [`FeeType`](../../doc/models/fee-type.md) | Required | Fees on the account, e.g. commission, bookkeeping, options-related. |
| `transfer` | [`TransferType`](../../doc/models/transfer-type.md) | Required | Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "buy": {
    "assignment": "assignment6",
    "contribution": "contribution0",
    "buy": "buy4",
    "buy to cover": "buy to cover6",
    "dividend reinvestment": "dividend reinvestment0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "sell": {
    "distribution": "distribution0",
    "exercise": "exercise2",
    "sell": "sell2",
    "sell short": "sell short8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "cancel": "cancel4",
  "cash": {
    "account fee": "account fee4",
    "contribution": "contribution8",
    "deposit": "deposit4",
    "dividend": "dividend4",
    "stock distribution": "stock distribution0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "fee": {
    "account fee": "account fee6",
    "adjustment": "adjustment2",
    "dividend": "dividend6",
    "interest": "interest8",
    "interest receivable": "interest receivable2",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "transfer": {
    "assignment": "assignment2",
    "adjustment": "adjustment6",
    "exercise": "exercise4",
    "expire": "expire4",
    "merger": "merger2",
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

