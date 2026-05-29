
# Link Token Create Request Deposit Switch

Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array.

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestDepositSwitch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_switch_id` | `str` | Required | The `deposit_switch_id` provided by the `/deposit_switch/create` endpoint. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "deposit_switch_id": "deposit_switch_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

