
# Bank Transfer List Response

Defines the response schema for `/bank_transfer/list`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_transfers` | [`List[BankTransfer]`](../../doc/models/bank-transfer.md) | Required | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "bank_transfers": [
    {
      "id": "id6",
      "ach_class": "rck",
      "account_id": "account_id8",
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
      "amount": "amount2",
      "iso_currency_code": "iso_currency_code0",
      "description": "description4",
      "created": "2016-03-13T12:52:32.123Z",
      "status": "cancelled",
      "network": "ach",
      "cancellable": false,
      "failure_reason": {
        "ach_return_code": "ach_return_code6",
        "description": "description0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "custom_tag": "custom_tag2",
      "metadata": {
        "key0": "metadata7"
      },
      "origination_account_id": "origination_account_id6",
      "direction": "outbound",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "request_id": "request_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

