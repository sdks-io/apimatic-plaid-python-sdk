
# Transaction Type

Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.

`digital:` transactions that took place online.

`place:` transactions that were made at a physical location.

`special:` transactions that relate to banks, e.g. fees or deposits.

`unresolved:` transactions that do not fit into the other three types.

*This model accepts additional fields of type Any.*

## Enumeration

`TransactionType`

## Fields

| Name |
|  --- |
| `DIGITAL` |
| `PLACE` |
| `SPECIAL` |
| `UNRESOLVED` |

