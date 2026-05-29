
# W2 State and Local Wages

*This model accepts additional fields of type Any.*

## Structure

`W2StateAndLocalWages`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `str` | Optional | State associated with the wage. |
| `employer_state_id_number` | `str` | Optional | State identification number of the employer. |
| `state_wages_tips` | `str` | Optional | Wages and tips from the specified state. |
| `state_income_tax` | `str` | Optional | Income tax from the specified state. |
| `local_wages_tips` | `str` | Optional | Wages and tips from the locality. |
| `local_income_tax` | `str` | Optional | Income tax from the locality. |
| `locality_name` | `str` | Optional | Name of the locality. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "state": "state8",
  "employer_state_id_number": "employer_state_id_number4",
  "state_wages_tips": "state_wages_tips4",
  "state_income_tax": "state_income_tax0",
  "local_wages_tips": "local_wages_tips4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

