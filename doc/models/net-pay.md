
# Net Pay

An object representing information about the net pay amount on the paystub.

*This model accepts additional fields of type Any.*

## Structure

`NetPay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distribution_details` | [`List[DistributionDetails]`](../../doc/models/distribution-details.md) | Optional | - |
| `total` | [`Total`](../../doc/models/total.md) | Optional | An object representing both the current pay period and year to date amount for a category. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "distribution_details": [
    {
      "account_number": "account_number0",
      "bank_account_type": "bank_account_type8",
      "bank_name": "bank_name4",
      "current_pay": {
        "amount": 45.16,
        "currency": "currency4",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "description": "description0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "total": {
    "canonical_description": "NOT_FOUND",
    "description": "description0",
    "current_pay": {
      "amount": 45.16,
      "currency": "currency4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "ytd_pay": {
      "amount": 28.98,
      "currency": "currency0",
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
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

