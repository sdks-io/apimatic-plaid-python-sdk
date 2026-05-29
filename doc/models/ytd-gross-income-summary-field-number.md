
# Ytd Gross Income Summary Field Number

*This model accepts additional fields of type Any.*

## Structure

`YtdGrossIncomeSummaryFieldNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Required | The value of the field. |
| `verification_status` | [`VerificationStatus`](../../doc/models/verification-status.md) | Required | The verification status. One of the following:<br><br>`"VERIFIED"`: The information was successfully verified.<br><br>`"UNVERIFIED"`: The verification has not yet been performed.<br><br>`"NEEDS_INFO"`: The verification was attempted but could not be completed due to missing information.<br><br>"`UNABLE_TO_VERIFY`": The verification was performed and the information could not be verified.<br><br>`"UNKNOWN"`: The verification status is unknown. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "value": 122.8,
  "verification_status": "UNABLE_TO_VERIFY",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

