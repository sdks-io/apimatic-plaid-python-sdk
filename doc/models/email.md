
# Email

An object representing an email address

*This model accepts additional fields of type Any.*

## Structure

`Email`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | `str` | Required | The email address. |
| `primary` | `bool` | Required | When `true`, identifies the email address as the primary email on an account. |
| `mtype` | [`Type1`](../../doc/models/type-1.md) | Required | The type of email account as described by the financial institution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "data": "data4",
  "primary": false,
  "type": "other",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

