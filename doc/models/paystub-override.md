
# Paystub Override

An object representing data from a paystub.

*This model accepts additional fields of type Any.*

## Structure

`PaystubOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employer` | [`Employer3`](../../doc/models/employer-3.md) | Optional | The employer on the paystub. |
| `employee` | [`Employee2`](../../doc/models/employee-2.md) | Optional | The employee on the paystub. |
| `income_breakdown` | [`List[IncomeBreakdown]`](../../doc/models/income-breakdown.md) | Optional | - |
| `pay_period_details` | [`PayPeriodDetails`](../../doc/models/pay-period-details.md) | Optional | Details about the pay period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
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
```

