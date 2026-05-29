
# Transfer Failure

The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise.

*This model accepts additional fields of type Any.*

## Structure

`TransferFailure`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ach_return_code` | `str` | Optional | The ACH return code, e.g. `R01`.  A return code will be provided if and only if the transfer status is `reversed`. For a full listing of ACH return codes, see [Bank Transfers errors](https://plaid.com/docs/errors/bank-transfers/#ach-return-codes). |
| `description` | `str` | Optional | A human-readable description of the reason for the failure or reversal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "ach_return_code": "ach_return_code4",
  "description": "description8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

