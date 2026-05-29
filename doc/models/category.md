
# Category

Information describing a transaction category

*This model accepts additional fields of type Any.*

## Structure

`Category`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_id` | `str` | Required | An identifying number for the category. `category_id` is a Plaid-specific identifier and does not necessarily correspond to merchant category codes. |
| `group` | `str` | Required | `place` for physical transactions or `special` for other transactions such as bank charges. |
| `hierarchy` | `List[str]` | Required | A hierarchical array of the categories to which this `category_id` belongs. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "category_id": "category_id0",
  "group": "group6",
  "hierarchy": [
    "hierarchy4",
    "hierarchy5"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

