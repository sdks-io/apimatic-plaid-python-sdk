
# User Custom Password

Custom test accounts are configured with a JSON configuration object formulated according to the schema below. All fields are optional. Sending an empty object as a configuration will result in an account configured with random balances and transaction history.

*This model accepts additional fields of type Any.*

## Structure

`UserCustomPassword`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Optional | The version of the password schema to use, possible values are 1 or 2. The default value is 2. You should only specify 1 if you know it is necessary for your test suite. |
| `seed` | `str` | Required | A seed, in the form of a string, that will be used to randomly generate account and transaction data, if this data is not specified using the `override_accounts` argument. If no seed is specified, the randomly generated data will be different each time.<br><br>Note that transactions data is generated relative to the Item's creation date. Different Items created on different dates with the same seed for transactions data will have different dates for the transactions. The number of days between each transaction and the Item creation will remain constant. For example, an Item created on December 15 might show a transaction on December 14. An Item created on December 20, using the same seed, would show that same transaction occurring on December 19. |
| `override_accounts` | [`List[OverrideAccounts]`](../../doc/models/override-accounts.md) | Required | An array of account overrides to configure the accounts for the Item. By default, if no override is specified, transactions and account data will be randomly generated based on the account type and subtype, and other products will have fixed or empty data. |
| `mfa` | [`Mfa`](../../doc/models/mfa.md) | Required | Specifies the multi-factor authentication settings to use with this test account |
| `recaptcha` | `str` | Required | You may trigger a reCAPTCHA in Plaid Link in the Sandbox environment by using the recaptcha field. Possible values are `good` or `bad`. A value of `good` will result in successful Item creation and `bad` will result in a `RECAPTCHA_BAD` error to simulate a failed reCAPTCHA. Both values require the reCAPTCHA to be manually solved within Plaid Link. |
| `force_error` | `str` | Required | An error code to force on Item creation. Possible values are:<br><br>`"INSTITUTION_NOT_RESPONDING"`<br>`"INSTITUTION_NO_LONGER_SUPPORTED"`<br>`"INVALID_CREDENTIALS"`<br>`"INVALID_MFA"`<br>`"ITEM_LOCKED"`<br>`"ITEM_LOGIN_REQUIRED"`<br>`"ITEM_NOT_SUPPORTED"`<br>`"INVALID_LINK_TOKEN"`<br>`"MFA_NOT_SUPPORTED"`<br>`"NO_ACCOUNTS"`<br>`"PLAID_ERROR"`<br>`"PRODUCTS_NOT_SUPPORTED"`<br>`"USER_SETUP_REQUIRED"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "seed": "seed2",
  "override_accounts": [
    {
      "type": "payroll",
      "subtype": "rewards",
      "starting_balance": 200.22,
      "force_available_balance": 130.0,
      "currency": "currency0",
      "meta": {
        "name": "name2",
        "official_name": "official_name4",
        "limit": 16.62,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "numbers": {
        "account": "account0",
        "ach_routing": "ach_routing0",
        "ach_wire_routing": "ach_wire_routing0",
        "eft_institution": "eft_institution4",
        "eft_branch": "eft_branch4",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "transactions": [
        {
          "date_transacted": "2016-03-13",
          "date_posted": "2016-03-13",
          "amount": 157.0,
          "description": "description8",
          "currency": "currency8",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "identity": {
        "names": [
          "names4",
          "names3",
          "names2"
        ],
        "phone_numbers": [
          {
            "data": "data0",
            "primary": false,
            "type": "office",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "emails": [
          {
            "data": "data6",
            "primary": false,
            "type": "other",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "addresses": [
          {
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
          }
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "liability": {
        "type": "type0",
        "purchase_apr": 210.82,
        "cash_apr": 182.16,
        "balance_transfer_apr": 200.2,
        "special_apr": 134.96,
        "last_payment_amount": 217.3,
        "minimum_payment_amount": 20.24,
        "is_overdue": false,
        "origination_date": "2016-03-13",
        "principal": 52.8,
        "nominal_apr": 189.16,
        "interest_capitalization_grace_period_months": 115.48,
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
        "repayment_plan_type": "repayment_plan_type6",
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
      },
      "inflow_model": {
        "type": "type6",
        "income_amount": 45.12,
        "payment_day_of_month": 53.32,
        "transaction_name": "transaction_name6",
        "statement_day_of_month": "statement_day_of_month2",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "holdings": {
        "institution_price": 182.32,
        "institution_price_as_of": "2016-03-13",
        "cost_basis": 171.84,
        "quantity": 180.32,
        "currency": "currency6",
        "security": {
          "isin": "isin4",
          "cusip": "cusip4",
          "sedol": "sedol0",
          "name": "name6",
          "ticker_symbol": "ticker_symbol8",
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
      "investment_transactions": {
        "date": "2016-03-13",
        "name": "name6",
        "quantity": 152.52,
        "price": 204.16,
        "fees": 1.46,
        "type": "type4",
        "currency": "currency4",
        "security": {
          "isin": "isin4",
          "cusip": "cusip4",
          "sedol": "sedol0",
          "name": "name6",
          "ticker_symbol": "ticker_symbol8",
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
      "income": {
        "paystubs": [
          {
            "employer": {
              "name": "name2",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "employee": {
              "name": "name8",
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
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "income_breakdown": [
              {
                "type": "bonus",
                "rate": 29.56,
                "hours": 6.52,
                "total": 118.76,
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              {
                "type": "bonus",
                "rate": 29.56,
                "hours": 6.52,
                "total": 118.76,
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              }
            ],
            "pay_period_details": {
              "start_date": "2016-03-13",
              "end_date": "2016-03-13",
              "pay_day": "2016-03-13",
              "gross_earnings": 59.04,
              "check_amount": 134.86,
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
  "mfa": {
    "type": "type8",
    "question_rounds": 209.6,
    "questions_per_round": 201.56,
    "selection_rounds": 158.12,
    "selections_per_question": 192.86,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "recaptcha": "recaptcha6",
  "force_error": "force_error4",
  "version": "version8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

