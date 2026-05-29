
# Pay Period Details

Details about the pay period.

*This model accepts additional fields of type Any.*

## Structure

`PayPeriodDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `date` | Required | The pay period start date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd". |
| `end_date` | `date` | Required | The pay period end date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd". |
| `pay_day` | `date` | Required | The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd"). |
| `gross_earnings` | `float` | Required | Total earnings before tax. |
| `check_amount` | `float` | Required | The net amount of the paycheck. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "start_date": "2016-03-13",
  "end_date": "2016-03-13",
  "pay_day": "2016-03-13",
  "gross_earnings": 169.08,
  "check_amount": 244.9,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

