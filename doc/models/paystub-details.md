
# Paystub Details

An object representing details that can be found on the paystub.

*This model accepts additional fields of type Any.*

## Structure

`PaystubDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pay_period_start_date` | `date` | Optional | Beginning date of the pay period on the paystub in the 'YYYY-MM-DD' format. |
| `pay_period_end_date` | `date` | Optional | Ending date of the pay period on the paystub in the 'YYYY-MM-DD' format. |
| `pay_date` | `date` | Optional | Pay date on the paystub in the 'YYYY-MM-DD' format. |
| `paystub_provider` | `str` | Optional | The name of the payroll provider that generated the paystub, e.g. ADP |
| `pay_frequency` | [`PayFrequency1`](../../doc/models/pay-frequency-1.md) | Optional | The frequency at which the employee is paid. Possible values: `MONTHLY`, `BI-WEEKLY`, `WEEKLY`, `SEMI-MONTHLY`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "pay_period_start_date": "2016-03-13",
  "pay_period_end_date": "2016-03-13",
  "pay_date": "2016-03-13",
  "paystub_provider": "paystub_provider8",
  "pay_frequency": "WEEKLY",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

