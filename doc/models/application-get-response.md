
# Application Get Response

The request ID associated with this call.

*This model accepts additional fields of type Any.*

## Structure

`ApplicationGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `application` | [`Application`](../../doc/models/application.md) | Required | Metadata about the application |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "request_id": "request_id8",
  "application": {
    "application_id": "application_id0",
    "name": "name4",
    "created_at": "2016-03-13",
    "logo_url": "logo_url4",
    "application_url": "application_url4",
    "reason_for_access": "reason_for_access2",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

