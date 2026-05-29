
# Liability Override

Used to configure Sandbox test data for the Liabilities product

*This model accepts additional fields of type Any.*

## Structure

`LiabilityOverride`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox. |
| `purchase_apr` | `float` | Required | The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`. |
| `cash_apr` | `float` | Required | The cash APR percentage value. Can only be set if `type` is `credit`. |
| `balance_transfer_apr` | `float` | Required | The balance transfer APR percentage value. Can only be set if `type` is `credit`. Can only be set if `type` is `credit`. |
| `special_apr` | `float` | Required | The special APR percentage value. Can only be set if `type` is `credit`. |
| `last_payment_amount` | `float` | Required | Override the `last_payment_amount` field. Can only be set if `type` is `credit`. |
| `minimum_payment_amount` | `float` | Required | Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`. |
| `is_overdue` | `bool` | Required | Override the `is_overdue` field |
| `origination_date` | `date` | Required | The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if `type` is `student`. |
| `principal` | `float` | Required | The original loan principal. Can only be set if `type` is `student`. |
| `nominal_apr` | `float` | Required | The interest rate on the loan as a percentage. Can only be set if `type` is `student`. |
| `interest_capitalization_grace_period_months` | `float` | Required | If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`. |
| `repayment_model` | [`StudentLoanRepaymentModel`](../../doc/models/student-loan-repayment-model.md) | Required | Student loan repayment information used to configure Sandbox test data for the Liabilities product |
| `expected_payoff_date` | `date` | Required | Override the `expected_payoff_date` field. Can only be set if `type` is `student`. |
| `guarantor` | `str` | Required | Override the `guarantor` field. Can only be set if `type` is `student`. |
| `is_federal` | `bool` | Required | Override the `is_federal` field. Can only be set if `type` is `student`. |
| `loan_name` | `str` | Required | Override the `loan_name` field. Can only be set if `type` is `student`. |
| `loan_status` | [`StudentLoanStatus`](../../doc/models/student-loan-status.md) | Required | An object representing the status of the student loan |
| `payment_reference_number` | `str` | Required | Override the `payment_reference_number` field. Can only be set if `type` is `student`. |
| `pslf_status` | [`PslfStatus`](../../doc/models/pslf-status.md) | Required | Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`). |
| `repayment_plan_description` | `str` | Required | Override the `repayment_plan.description` field. Can only be set if `type` is `student`. |
| `repayment_plan_type` | `str` | Required | Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `"extended graduated"`, `"extended standard"`, `"graduated"`, `"income-contingent repayment"`, `"income-based repayment"`, `"interest only"`, `"other"`, `"pay as you earn"`, `"revised pay as you earn"`, or `"standard"`. |
| `sequence_number` | `str` | Required | Override the `sequence_number` field. Can only be set if `type` is `student`. |
| `servicer_address` | [`Address`](../../doc/models/address.md) | Required | A physical mailing address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "type0",
  "purchase_apr": 195.92,
  "cash_apr": 167.26,
  "balance_transfer_apr": 185.3,
  "special_apr": 120.06,
  "last_payment_amount": 23.8,
  "minimum_payment_amount": 5.34,
  "is_overdue": false,
  "origination_date": "2016-03-13",
  "principal": 188.3,
  "nominal_apr": 174.26,
  "interest_capitalization_grace_period_months": 125.62,
  "repayment_model": {
    "type": "type8",
    "non_repayment_months": 34.06,
    "repayment_months": 100.72,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "expected_payoff_date": "2016-03-13",
  "guarantor": "guarantor0",
  "is_federal": false,
  "loan_name": "loan_name6",
  "loan_status": {
    "end_date": "2016-03-13",
    "type": "cancelled",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "payment_reference_number": "payment_reference_number0",
  "pslf_status": {
    "estimated_eligibility_date": "2016-03-13",
    "payments_made": 175.34,
    "payments_remaining": 221.32,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "repayment_plan_description": "repayment_plan_description6",
  "repayment_plan_type": "repayment_plan_type4",
  "sequence_number": "sequence_number0",
  "servicer_address": {
    "data": {
      "city": "city0",
      "region": "region6",
      "street": "street0",
      "postal_code": "postal_code2",
      "country": "country4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "primary": false,
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

