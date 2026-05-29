
# Mortgage Liability

Contains details about a mortgage account.

*This model accepts additional fields of type Any.*

## Structure

`MortgageLiability`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The ID of the account that this liability belongs to. |
| `account_number` | `str` | Required | The account number of the loan. |
| `current_late_fee` | `float` | Required | The current outstanding amount charged for late payment. |
| `escrow_balance` | `float` | Required | Total amount held in escrow to pay taxes and insurance on behalf of the borrower. |
| `has_pmi` | `bool` | Required | Indicates whether the borrower has private mortgage insurance in effect. |
| `has_prepayment_penalty` | `bool` | Required | Indicates whether the borrower will pay a penalty for early payoff of mortgage. |
| `interest_rate` | [`MortgageInterestRate`](../../doc/models/mortgage-interest-rate.md) | Required | Object containing metadata about the interest rate for the mortgage. |
| `last_payment_amount` | `float` | Required | The amount of the last payment. |
| `last_payment_date` | `date` | Required | The date of the last payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `loan_type_description` | `str` | Required | Description of the type of loan, for example `conventional`, `fixed`, or `variable`. This field is provided directly from the loan servicer and does not have an enumerated set of possible values. |
| `loan_term` | `str` | Required | Full duration of mortgage as at origination (e.g. `10 year`). |
| `maturity_date` | `date` | Required | Original date on which mortgage is due in full. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `next_monthly_payment` | `float` | Required | The amount of the next payment. |
| `next_payment_due_date` | `date` | Required | The due date for the next payment. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `origination_date` | `date` | Required | The date on which the loan was initially lent. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). |
| `origination_principal_amount` | `float` | Required | The original principal balance of the mortgage. |
| `past_due_amount` | `float` | Required | Amount of loan (principal + interest) past due for payment. |
| `property_address` | [`MortgagePropertyAddress`](../../doc/models/mortgage-property-address.md) | Required | Object containing fields describing property address. |
| `ytd_interest_paid` | `float` | Required | The year to date (YTD) interest paid. |
| `ytd_principal_paid` | `float` | Required | The YTD principal paid. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_id": "account_id6",
  "account_number": "account_number4",
  "current_late_fee": 37.04,
  "escrow_balance": 38.4,
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
  "last_payment_amount": 42.16,
  "last_payment_date": "2016-03-13",
  "loan_type_description": "loan_type_description8",
  "loan_term": "loan_term0",
  "maturity_date": "2016-03-13",
  "next_monthly_payment": 31.64,
  "next_payment_due_date": "2016-03-13",
  "origination_date": "2016-03-13",
  "origination_principal_amount": 68.32,
  "past_due_amount": 170.88,
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
  "ytd_interest_paid": 179.02,
  "ytd_principal_paid": 212.0,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

