
# Personal Finance Category 2

*This model accepts additional fields of type Any.*

## Structure

`PersonalFinanceCategory2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary` | `str` | Required | A high level category that communicates the broad category of the transaction. |
| `detailed` | `str` | Required | Provides additional granularity to the primary categorization. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "primary": "primary6",
  "detailed": "detailed6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

