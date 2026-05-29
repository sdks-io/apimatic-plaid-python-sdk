
# Payment Initiation Payment List Response

PaymentInitiationPaymentListResponse defines the response schema for `/payment_initiation/payment/list`

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationPaymentListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payments` | [`List[PaymentInitiationPayment]`](../../doc/models/payment-initiation-payment.md) | Required | An array of payments that have been created, associated with the given `client_id`. |
| `next_cursor` | `datetime` | Required | The value that, when used as the optional `cursor` parameter to `/payment_initiation/payment/list`, will return the next unreturned payment as its first payment. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payments": [
    {
      "payment_id": "payment_id2",
      "amount": {
        "currency": "GBP",
        "value": 52.3,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "status": "PAYMENT_STATUS_INSUFFICIENT_FUNDS",
      "recipient_id": "recipient_id8",
      "reference": "reference2",
      "adjusted_reference": "adjusted_reference6",
      "last_status_update": "2016-03-13T12:52:32.123Z",
      "schedule": {
        "interval": "WEEKLY",
        "interval_execution_day": 88,
        "start_date": "2016-03-13",
        "end_date": "2016-03-13",
        "adjusted_start_date": "2016-03-13",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "refund_details": {
        "name": "name8",
        "iban": "iban2",
        "bacs": {
          "account": "account4",
          "sort_code": "sort_code4",
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
      "bacs": {
        "account": "account4",
        "sort_code": "sort_code4",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "iban": "iban6",
      "initiated_refunds": [
        {
          "refund_id": "refund_id0",
          "amount": {
            "currency": "GBP",
            "value": 52.3,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "status": "INITIATED",
          "last_status_update": "2016-03-13T12:52:32.123Z",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        {
          "refund_id": "refund_id0",
          "amount": {
            "currency": "GBP",
            "value": 52.3,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "status": "INITIATED",
          "last_status_update": "2016-03-13T12:52:32.123Z",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "emi_account_id": "emi_account_id4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "next_cursor": "2016-03-13T12:52:32.123Z",
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

