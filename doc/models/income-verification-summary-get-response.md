
# Income Verification Summary Get Response

IncomeVerificationSummaryGetResponse defines the response schema for `/income/verification/summary/get`.

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationSummaryGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `income_summaries` | [`List[IncomeSummary]`](../../doc/models/income-summary.md) | Required | A list of income summaries. |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "income_summaries": [
    {
      "employer_name": {
        "value": "value8",
        "verification_status": "UNKNOWN",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "employee_name": {
        "value": "value4",
        "verification_status": "UNABLE_TO_VERIFY",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "ytd_gross_income": {
        "value": 80.36,
        "verification_status": "UNKNOWN",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "ytd_net_income": {
        "value": 101.8,
        "verification_status": "UNABLE_TO_VERIFY",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "pay_frequency": {
        "value": "monthly",
        "verification_status": "UNABLE_TO_VERIFY",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "projected_wage": {
        "value": 108.54,
        "verification_status": "NEEDS_INFO",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "verified_transaction": {
        "description": "description8",
        "amount": 228.3,
        "date": "2016-03-13",
        "account_id": "account_id0",
        "transaction_id": "transaction_id6",
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
  "request_id": "request_id0",
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

