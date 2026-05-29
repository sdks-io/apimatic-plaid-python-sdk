
# Income Verification Taxforms Get Response

IncomeVerificationTaxformsGetResponse defines the response schema for `/income/verification/taxforms/get`

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationTaxformsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `taxforms` | [`List[Taxform]`](../../doc/models/taxform.md) | Required | A list of taxforms. |
| `document_metadata` | [`List[DocumentMetadata]`](../../doc/models/document-metadata.md) | Required | - |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "taxforms": [
    {
      "document_type": "document_type8",
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
  ],
  "document_metadata": [
    {
      "name": "name2",
      "status": "status6",
      "doc_id": "doc_id6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "request_id": "request_id2",
  "error": {
    "error_type": "RECAPTCHA_ERROR",
    "error_code": "error_code6",
    "error_message": "error_message6",
    "display_message": "display_message8",
    "request_id": "request_id4",
    "causes": [
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "status": 217.06,
    "documentation_url": "documentation_url6",
    "suggested_action": "suggested_action0",
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

