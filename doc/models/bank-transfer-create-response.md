
# Bank Transfer Create Response

Defines the response schema for `/bank_transfer/create`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_transfer` | [`BankTransfer`](../../doc/models/bank-transfer.md) | Required | Represents a bank transfer within the Bank Transfers API. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "bank_transfer": {
    "id": "id2",
    "ach_class": "pbr",
    "account_id": "account_id4",
    "type": "debit",
    "user": {
      "legal_name": "legal_name8",
      "email_address": "email_address2",
      "routing_number": "routing_number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "amount": "amount4",
    "iso_currency_code": "iso_currency_code4",
    "description": "description2",
    "created": "2016-03-13T12:52:32.123Z",
    "status": "reversed",
    "network": "wire",
    "cancellable": false,
    "failure_reason": {
      "ach_return_code": "ach_return_code6",
      "description": "description0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "custom_tag": "custom_tag4",
    "metadata": {
      "key0": "metadata9",
      "key1": "metadata8"
    },
    "origination_account_id": "origination_account_id2",
    "direction": "outbound",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

