
# Employers Search Response

EmployersSearchResponse defines the response schema for `/employers/search`.

*This model accepts additional fields of type Any.*

## Structure

`EmployersSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employers` | [`List[Employer]`](../../doc/models/employer.md) | Required | A list of employers matching the search criteria. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "employers": [
    {
      "employer_id": "employer_id0",
      "name": "name6",
      "address": {
        "city": "city6",
        "region": "region2",
        "street": "street6",
        "postal_code": "postal_code8",
        "country": "country0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "confidence_score": 240.36,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

