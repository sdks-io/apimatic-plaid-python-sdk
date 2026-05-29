
# Transfer List Response

Defines the response schema for `/transfer/list`

*This model accepts additional fields of type Any.*

## Structure

`TransferListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfers` | [`List[Transfer]`](../../doc/models/transfer.md) | Required | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "transfers": [
    {
      "id": "id4",
      "ach_class": "arc",
      "account_id": "account_id6",
      "type": "debit",
      "user": {
        "legal_name": "legal_name8",
        "phone_number": "phone_number2",
        "email_address": "email_address2",
        "address": {
          "street": "street6",
          "city": "city6",
          "region": "region2",
          "postal_code": "postal_code8",
          "country": "country0",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "amount": "amount6",
      "description": "description6",
      "created": "2016-03-13T12:52:32.123Z",
      "status": "reversed",
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
      "metadata": {
        "key0": "metadata9"
      },
      "origination_account_id": "origination_account_id4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "request_id": "request_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

