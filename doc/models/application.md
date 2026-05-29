
# Application

Metadata about the application

*This model accepts additional fields of type Any.*

## Structure

`Application`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_id` | `str` | Required | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. |
| `name` | `str` | Required | The name of the application |
| `created_at` | `date` | Required | The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. |
| `logo_url` | `str` | Required | A URL that links to the application logo image. |
| `application_url` | `str` | Required | The URL for the application's website |
| `reason_for_access` | `str` | Required | A string provided by the connected app stating why they use their respective enabled products. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "application_id": "application_id8",
  "name": "name2",
  "created_at": "2016-03-13",
  "logo_url": "logo_url8",
  "application_url": "application_url2",
  "reason_for_access": "reason_for_access0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

