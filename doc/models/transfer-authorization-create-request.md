
# Transfer Authorization Create Request

Defines the request schema for `/transfer/authorization/create`

*This model accepts additional fields of type Any.*

## Structure

`TransferAuthorizationCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The Plaid `access_token` for the account that will be debited or credited. |
| `account_id` | `str` | Required | The Plaid `account_id` for the account that will be debited or credited. |
| `mtype` | [`TransferType1`](../../doc/models/transfer-type-1.md) | Required | The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account. |
| `network` | [`TransferNetwork`](../../doc/models/transfer-network.md) | Required | The network or rails used for the transfer. Valid options are `ach` or `same-day-ach`. |
| `amount` | `str` | Required | The amount of the transfer (decimal string with two digits of precision e.g. “10.00”). |
| `ach_class` | [`AchClass`](../../doc/models/ach-class.md) | Required | Specifies the use case of the transfer.  Required for transfers on an ACH network.<br><br>`"arc"` - Accounts Receivable Entry<br><br>`"cbr`" - Cross Border Entry<br><br>`"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts<br><br>`"cie"` - Customer Initiated Entry<br><br>`"cor"` - Automated Notification of Change<br><br>`"ctx"` - Corporate Trade Exchange<br><br>`"iat"` - International<br><br>`"mte"` - Machine Transfer Entry<br><br>`"pbr"` - Cross Border Entry<br><br>`"pop"` - Point-of-Purchase Entry<br><br>`"pos"` - Point-of-Sale Entry<br><br>`"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment<br><br>`"rck"` - Re-presented Check Entry<br><br>`"tel"` - Telephone-Initiated Entry<br><br>`"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet |
| `user` | [`TransferUserInRequest`](../../doc/models/transfer-user-in-request.md) | Required | The legal name and other information for the account holder. |
| `device` | [`TransferAuthorizationDevice`](../../doc/models/transfer-authorization-device.md) | Optional | Information about the device being used to initiate the authorization. |
| `origination_account_id` | `str` | Optional | Plaid's unique identifier for the origination account for this authorization. If not specified, the default account will be used. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "access_token": "access_token2",
  "account_id": "account_id6",
  "type": "debit",
  "network": "ach",
  "amount": "amount6",
  "ach_class": "pos",
  "user": {
    "legal_name": "legal_name8",
    "phone_number": "phone_number2",
    "email_address": "email_address2",
    "address": {
      "street": "street6",
      "city": "city6",
      "region": "region2",
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
  "device": {
    "ip_address": "ip_address6",
    "user_agent": "user_agent8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "origination_account_id": "origination_account_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

