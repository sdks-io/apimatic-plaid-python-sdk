
# Document Metadata

An object representing metadata from the end user's uploaded document.

*This model accepts additional fields of type Any.*

## Structure

`DocumentMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the document. |
| `status` | `str` | Optional | The processing status of the document. |
| `doc_id` | `str` | Optional | An identifier of the document that is also present in the paystub response. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name4",
  "status": "status6",
  "doc_id": "doc_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

