
# Taxform

*This model accepts additional fields of type Any.*

## Structure

`Taxform`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_type` | `str` | Required | The type of tax document. |
| `w_2` | [`W2`](../../doc/models/w2.md) | Optional | W2 is an object that represents income data taken from a W2 tax document. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "document_type": "document_type6",
  "w2": {
    "employer": {
      "name": "name2",
      "address": {
        "city": "city6",
        "street": "street6",
        "line1": "line18",
        "line2": "line20",
        "postal_code": "postal_code8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "employee": {
      "name": "name8",
      "address": {
        "city": "city6",
        "street": "street6",
        "line1": "line18",
        "line2": "line20",
        "postal_code": "postal_code8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "marital_status": "marital_status6",
      "taxpayer_id": {
        "id_type": "id_type8",
        "last_4_digits": "last_4_digits6",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "tax_year": "tax_year8",
    "employer_id_number": "employer_id_number8",
    "wages_tips_other_comp": "wages_tips_other_comp4",
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

