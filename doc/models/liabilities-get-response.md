
# Liabilities Get Response

LiabilitiesGetResponse defines the response schema for `/liabilities/get`

*This model accepts additional fields of type Any.*

## Structure

`LiabilitiesGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[Account]`](../../doc/models/account.md) | Required | An array of accounts associated with the Item |
| `item` | [`Item`](../../doc/models/item.md) | Required | Metadata about the Item. |
| `liabilities` | [`LiabilitiesObject`](../../doc/models/liabilities-object.md) | Required | An object containing liability accounts |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accounts": [
    {
      "account_id": "account_id2",
      "balances": {
        "available": 142.32,
        "current": 79.74,
        "limit": 30.84,
        "iso_currency_code": "iso_currency_code6",
        "unofficial_currency_code": "unofficial_currency_code2",
        "last_updated_datetime": "2016-03-13T12:52:32.123Z",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "mask": "mask4",
      "name": "name0",
      "official_name": "official_name2",
      "type": "depository",
      "subtype": "consumer",
      "verification_status": "automatically_verified",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "item": {
    "item_id": "item_id2",
    "institution_id": "institution_id0",
    "webhook": "webhook0",
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
    "available_products": [
      "transfer",
      "assets"
    ],
    "billed_products": [
      "deposit_switch",
      "standing_orders"
    ],
    "consent_expiration_time": "2016-03-13T12:52:32.123Z",
    "update_type": "background",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "liabilities": {
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
  },
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

