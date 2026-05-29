
# Deposit Switch Alt Create Request

DepositSwitchAltCreateRequest defines the request schema for `/deposit_switch/alt/create`

*This model accepts additional fields of type Any.*

## Structure

`DepositSwitchAltCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `target_account` | [`DepositSwitchTargetAccount`](../../doc/models/deposit-switch-target-account.md) | Required | - |
| `target_user` | [`DepositSwitchTargetUser`](../../doc/models/deposit-switch-target-user.md) | Required | - |
| `options` | [`DepositSwitchCreateRequestOptions`](../../doc/models/deposit-switch-create-request-options.md) | Optional | Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`. |
| `country_code` | [`CountryCode1`](../../doc/models/country-code-1.md) | Optional | ISO-3166-1 alpha-2 country code standard. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret8",
  "target_account": {
    "account_number": "account_number8",
    "routing_number": "routing_number6",
    "account_name": "account_name0",
    "account_subtype": "checking",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "target_user": {
    "given_name": "given_name6",
    "family_name": "family_name8",
    "phone": "phone4",
    "email": "email2",
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
    "tax_payer_id": "tax_payer_id2",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "options": {
    "webhook": "webhook0",
    "transaction_item_access_tokens": [
      "transaction_item_access_tokens4",
      "transaction_item_access_tokens5",
      "transaction_item_access_tokens6"
    ],
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "country_code": "US",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

