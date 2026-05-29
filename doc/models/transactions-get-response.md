
# Transactions Get Response

TransactionsGetResponse defines the response schema for `/transactions/get`

*This model accepts additional fields of type Any.*

## Structure

`TransactionsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[Account]`](../../doc/models/account.md) | Required | An array containing the `accounts` associated with the Item for which transactions are being returned. Each transaction can be mapped to its corresponding account via the `account_id` field. |
| `transactions` | [`List[Transaction]`](../../doc/models/transaction.md) | Required | An array containing transactions from the account. Transactions are returned in reverse chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned is determined by the `count` parameter. |
| `total_transactions` | `int` | Required | The total number of transactions available within the date range specified. If `total_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter. |
| `item` | [`Item`](../../doc/models/item.md) | Required | Metadata about the Item. |
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
  "transactions": [
    {
      "transaction_type": "digital",
      "pending_transaction_id": "pending_transaction_id2",
      "category_id": "category_id0",
      "category": [
        "category0",
        "category1",
        "category2"
      ],
      "location": {
        "address": "address0",
        "city": "city6",
        "region": "region0",
        "postal_code": "postal_code6",
        "country": "country8",
        "lat": 205.22,
        "lon": 217.68,
        "store_number": "store_number0",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "payment_meta": {
        "reference_number": "reference_number2",
        "ppd_id": "ppd_id4",
        "payee": "payee2",
        "by_order_of": "by_order_of8",
        "payer": "payer2",
        "payment_method": "payment_method4",
        "payment_processor": "payment_processor4",
        "reason": "reason8",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "account_owner": "account_owner6",
      "name": "name8",
      "original_description": "original_description6",
      "account_id": "account_id0",
      "amount": 157.0,
      "iso_currency_code": "iso_currency_code8",
      "unofficial_currency_code": "unofficial_currency_code0",
      "date": "2016-03-13",
      "pending": false,
      "transaction_id": "transaction_id6",
      "payment_channel": "other",
      "merchant_name": "merchant_name0",
      "authorized_date": "2016-03-13",
      "authorized_datetime": "2016-03-13T12:52:32.123Z",
      "datetime": "2016-03-13T12:52:32.123Z",
      "check_number": "check_number0",
      "transaction_code": "cash",
      "personal_finance_category": {
        "primary": "primary4",
        "detailed": "detailed4",
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
  "total_transactions": 140,
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
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

