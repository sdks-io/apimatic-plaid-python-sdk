
# Asset Report User

The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program.

*This model accepts additional fields of type Any.*

## Structure

`AssetReportUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_user_id` | `str` | Optional | An identifier you determine and submit for the user. |
| `first_name` | `str` | Optional | The user's first name. Required for the Fannie Mae Day 1 Certainty™ program. |
| `middle_name` | `str` | Optional | The user's middle name |
| `last_name` | `str` | Optional | The user's last name.  Required for the Fannie Mae Day 1 Certainty™ program. |
| `ssn` | `str` | Optional | The user's Social Security Number. Required for the Fannie Mae Day 1 Certainty™ program.<br><br>Format: "ddd-dd-dddd" |
| `phone_number` | `str` | Optional | The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers provided in other formats will be parsed on a best-effort basis. |
| `email` | `str` | Optional | The user's email address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_user_id": "client_user_id0",
  "first_name": "first_name6",
  "middle_name": "middle_name6",
  "last_name": "last_name4",
  "ssn": "ssn2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

