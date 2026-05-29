
# Investments Holdings Get Response

InvestmentsHoldingsGetResponse defines the response schema for `/investments/holdings/get`

*This model accepts additional fields of type Any.*

## Structure

`InvestmentsHoldingsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[Account]`](../../doc/models/account.md) | Required | The accounts associated with the Item |
| `holdings` | [`List[Holding]`](../../doc/models/holding.md) | Required | The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field. |
| `securities` | [`List[Security]`](../../doc/models/security.md) | Required | Objects describing the securities held in the accounts associated with the Item. |
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
  "holdings": [
    {
      "account_id": "account_id8",
      "security_id": "security_id6",
      "institution_price": 182.32,
      "institution_price_as_of": "2016-03-13",
      "institution_value": 21.52,
      "cost_basis": 171.84,
      "quantity": 180.32,
      "iso_currency_code": "iso_currency_code0",
      "unofficial_currency_code": "unofficial_currency_code8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "securities": [
    {
      "security_id": "security_id2",
      "isin": "isin8",
      "cusip": "cusip0",
      "sedol": "sedol4",
      "institution_security_id": "institution_security_id4",
      "institution_id": "institution_id0",
      "proxy_security_id": "proxy_security_id6",
      "name": "name2",
      "ticker_symbol": "ticker_symbol2",
      "is_cash_equivalent": false,
      "type": "type8",
      "close_price": 88.1,
      "close_price_as_of": "2016-03-13",
      "iso_currency_code": "iso_currency_code4",
      "unofficial_currency_code": "unofficial_currency_code4",
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
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

