
# Signal Evaluate Device

Details about the end user's device

*This model accepts additional fields of type Any.*

## Structure

`SignalEvaluateDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | The IP address of the device that initiated the transaction |
| `user_agent` | `str` | Optional | The user agent of the device that initiated the transaction (e.g. "Mozilla/5.0") |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "ip_address": "ip_address8",
  "user_agent": "user_agent0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

