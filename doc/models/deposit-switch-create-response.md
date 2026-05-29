
# Deposit Switch Create Response

DepositSwitchCreateResponse defines the response schema for `/deposit_switch/create`

*This model accepts additional fields of type Any.*

## Structure

`DepositSwitchCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_switch_id` | `str` | Required | ID of the deposit switch. This ID is persisted throughout the lifetime of the deposit switch. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "deposit_switch_id": "deposit_switch_id8",
  "request_id": "request_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

