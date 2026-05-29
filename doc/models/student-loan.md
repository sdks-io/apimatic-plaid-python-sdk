
# Student Loan

Contains details about a student loan account

*This model accepts additional fields of type Any.*

## Structure

`StudentLoan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The ID of the account that this liability belongs to. |
| `account_number` | `str` | Required | The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last 4 digits instead of the entire number). |
| `disbursement_dates` | `List[date]` | Required | The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `expected_payoff_date` | `date` | Required | The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `guarantor` | `str` | Required | The guarantor of the student loan. |
| `interest_rate_percentage` | `float` | Required | The interest rate on the loan as a percentage. |
| `is_overdue` | `bool` | Required | `true` if a payment is currently overdue. Availability for this field is limited. |
| `last_payment_amount` | `float` | Required | The amount of the last payment. |
| `last_payment_date` | `date` | Required | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `last_statement_issue_date` | `date` | Required | The date of the last statement. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `loan_name` | `str` | Required | The type of loan, e.g., "Consolidation Loans". |
| `loan_status` | [`StudentLoanStatus`](../../doc/models/student-loan-status.md) | Required | An object representing the status of the student loan |
| `minimum_payment_amount` | `float` | Required | The minimum payment due for the next billing cycle. There are some exceptions:<br>Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`).<br>Firstmark (`ins_116295` ) will display as $0 if there is an autopay program in effect. |
| `next_payment_due_date` | `date` | Required | The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `origination_date` | `date` | Required | The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `origination_principal_amount` | `float` | Required | The original principal balance of the loan. |
| `outstanding_interest_amount` | `float` | Required | The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`. |
| `payment_reference_number` | `str` | Required | The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match a`ccount_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different. |
| `pslf_status` | [`PslfStatus`](../../doc/models/pslf-status.md) | Required | Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is Fedloan (`ins_116527`). |
| `repayment_plan` | [`StudentRepaymentPlan`](../../doc/models/student-repayment-plan.md) | Required | An object representing the repayment plan for the student loan |
| `sequence_number` | `str` | Required | The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available. |
| `servicer_address` | [`ServicerAddressData`](../../doc/models/servicer-address-data.md) | Required | The address of the student loan servicer. This is generally the remittance address to which payments should be sent. |
| `ytd_interest_paid` | `float` | Required | The year to date (YTD) interest paid. Availability for this field is limited. |
| `ytd_principal_paid` | `float` | Required | The year to date (YTD) principal paid. Availability for this field is limited. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_id": "account_id0",
  "account_number": "account_number8",
  "disbursement_dates": [
    "2016-03-13",
    "2016-03-13"
  ],
  "expected_payoff_date": "2016-03-13",
  "guarantor": "guarantor8",
  "interest_rate_percentage": 51.16,
  "is_overdue": false,
  "last_payment_amount": 84.52,
  "last_payment_date": "2016-03-13",
  "last_statement_issue_date": "2016-03-13",
  "loan_name": "loan_name4",
  "loan_status": {
    "end_date": "2016-03-13",
    "type": "cancelled",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "minimum_payment_amount": 153.02,
  "next_payment_due_date": "2016-03-13",
  "origination_date": "2016-03-13",
  "origination_principal_amount": 25.96,
  "outstanding_interest_amount": 143.24,
  "payment_reference_number": "payment_reference_number8",
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
  "sequence_number": "sequence_number8",
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
  "ytd_interest_paid": 136.66,
  "ytd_principal_paid": 86.36,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

