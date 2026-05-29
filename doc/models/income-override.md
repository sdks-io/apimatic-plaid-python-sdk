
# Income Override

Specify payroll data on the account.

*This model accepts additional fields of type Any.*

## Structure

`IncomeOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paystubs` | [`List[PaystubOverride]`](../../doc/models/paystub-override.md) | Optional | A list of paystubs associated with the account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "paystubs": [
    {
      "employer": {
        "name": "name2",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "employee": {
        "name": "name8",
        "address": {
          "city": "city6",
          "region": "region2",
          "street": "street6",
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
      "income_breakdown": [
        {
          "type": "bonus",
          "rate": 29.56,
          "hours": 6.52,
          "total": 118.76,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        {
          "type": "bonus",
          "rate": 29.56,
          "hours": 6.52,
          "total": 118.76,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "pay_period_details": {
        "start_date": "2016-03-13",
        "end_date": "2016-03-13",
        "pay_day": "2016-03-13",
        "gross_earnings": 59.04,
        "check_amount": 134.86,
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
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

