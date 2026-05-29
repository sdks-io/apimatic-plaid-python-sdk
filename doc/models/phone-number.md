
# Phone Number

A phone number

*This model accepts additional fields of type Any.*

## Structure

`PhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The phone number. |
| `primary` | `bool` | Required | When `true`, identifies the phone number as the primary number on an account. |
| `mtype` | [`Type`](../../doc/models/type.md) | Required | The type of phone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "data": "data2",
  "primary": false,
  "type": "home",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

