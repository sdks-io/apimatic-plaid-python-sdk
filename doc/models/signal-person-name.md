
# Signal Person Name

The user's legal name

*This model accepts additional fields of type Any.*

## Structure

`SignalPersonName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prefix` | `str` | Optional | The user's name prefix (e.g. "Mr.") |
| `given_name` | `str` | Optional | The user's given name. If the user has a one-word name, it should be provided in this field. |
| `middle_name` | `str` | Optional | The user's middle name |
| `family_name` | `str` | Optional | The user's family name / surname |
| `suffix` | `str` | Optional | The user's name suffix (e.g. "II") |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "prefix": "prefix6",
  "given_name": "given_name0",
  "middle_name": "middle_name8",
  "family_name": "family_name2",
  "suffix": "suffix8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

