
# Liabilities Object

An object containing liability accounts

*This model accepts additional fields of type Any.*

## Structure

`LiabilitiesObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit` | [`List[CreditCardLiability]`](../../doc/models/credit-card-liability.md) | Required | The credit accounts returned. |
| `mortgage` | [`List[MortgageLiability]`](../../doc/models/mortgage-liability.md) | Required | The mortgage accounts returned. |
| `student` | [`List[StudentLoan]`](../../doc/models/student-loan.md) | Required | The student loan accounts returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "credit": [
    {
      "account_id": "account_id0",
      "aprs": [
        {
          "apr_percentage": 185.0,
          "apr_type": "balance_transfer_apr",
          "balance_subject_to_apr": 23.44,
          "interest_charge_amount": 112.32,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "is_overdue": false,
      "last_payment_amount": 50.32,
      "last_payment_date": "2016-03-13",
      "last_statement_issue_date": "2016-03-13",
      "minimum_payment_amount": 187.22,
      "next_payment_due_date": "2016-03-13",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "mortgage": [
    {
      "account_id": "account_id6",
      "account_number": "account_number4",
      "current_late_fee": 43.54,
      "escrow_balance": 44.9,
      "has_pmi": false,
      "has_prepayment_penalty": false,
      "interest_rate": {
        "percentage": 105.9,
        "type": "type2",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "last_payment_amount": 35.66,
      "last_payment_date": "2016-03-13",
      "loan_type_description": "loan_type_description8",
      "loan_term": "loan_term0",
      "maturity_date": "2016-03-13",
      "next_monthly_payment": 38.14,
      "next_payment_due_date": "2016-03-13",
      "origination_date": "2016-03-13",
      "origination_principal_amount": 74.82,
      "past_due_amount": 177.38,
      "property_address": {
        "city": "city0",
        "country": "country4",
        "postal_code": "postal_code2",
        "region": "region6",
        "street": "street0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "ytd_interest_paid": 185.52,
      "ytd_principal_paid": 218.5,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "student": [
    {
      "account_id": "account_id2",
      "account_number": "account_number0",
      "disbursement_dates": [
        "2016-03-13",
        "2016-03-13"
      ],
      "expected_payoff_date": "2016-03-13",
      "guarantor": "guarantor0",
      "interest_rate_percentage": 102.78,
      "is_overdue": false,
      "last_payment_amount": 32.9,
      "last_payment_date": "2016-03-13",
      "last_statement_issue_date": "2016-03-13",
      "loan_name": "loan_name6",
      "loan_status": {
        "end_date": "2016-03-13",
        "type": "cancelled",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "minimum_payment_amount": 204.64,
      "next_payment_due_date": "2016-03-13",
      "origination_date": "2016-03-13",
      "origination_principal_amount": 77.58,
      "outstanding_interest_amount": 194.86,
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
      "repayment_plan": {
        "description": "description6",
        "type": "income-based repayment",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "sequence_number": "sequence_number0",
      "servicer_address": {
        "city": "city2",
        "region": "region8",
        "street": "street2",
        "postal_code": "postal_code4",
        "country": "country6",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "ytd_interest_paid": 188.28,
      "ytd_principal_paid": 221.26,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

