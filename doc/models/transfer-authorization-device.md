
# Transfer Authorization Device

Information about the device being used to initiate the authorization.

*This model accepts additional fields of type Any.*

## Structure

`TransferAuthorizationDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The IP address of the device being used to initiate the authorization. |
| `user_agent` | `str` | Optional | The user agent of the device being used to initiate the authorization. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "ip_address": "ip_address6",
  "user_agent": "user_agent8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

