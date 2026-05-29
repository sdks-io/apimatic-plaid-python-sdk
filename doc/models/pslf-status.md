
# Pslf Status

Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`).

*This model accepts additional fields of type Any.*

## Structure

`PslfStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_eligibility_date` | `date` | Required | The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `payments_made` | `float` | Required | The number of qualifying payments that have been made. |
| `payments_remaining` | `float` | Required | The number of qualifying payments remaining. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "estimated_eligibility_date": "2016-03-13",
  "payments_made": 18.4,
  "payments_remaining": 64.38,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

