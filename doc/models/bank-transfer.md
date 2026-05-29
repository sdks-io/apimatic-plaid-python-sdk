
# Bank Transfer

Represents a bank transfer within the Bank Transfers API.

*This model accepts additional fields of type Any.*

## Structure

`BankTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Plaid’s unique identifier for a bank transfer. |
| `ach_class` | [`AchClass`](../../doc/models/ach-class.md) | Required | Specifies the use case of the transfer.  Required for transfers on an ACH network.<br><br>`"arc"` - Accounts Receivable Entry<br><br>`"cbr`" - Cross Border Entry<br><br>`"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts<br><br>`"cie"` - Customer Initiated Entry<br><br>`"cor"` - Automated Notification of Change<br><br>`"ctx"` - Corporate Trade Exchange<br><br>`"iat"` - International<br><br>`"mte"` - Machine Transfer Entry<br><br>`"pbr"` - Cross Border Entry<br><br>`"pop"` - Point-of-Purchase Entry<br><br>`"pos"` - Point-of-Sale Entry<br><br>`"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment<br><br>`"rck"` - Re-presented Check Entry<br><br>`"tel"` - Telephone-Initiated Entry<br><br>`"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet |
| `account_id` | `str` | Required | The account ID that should be credited/debited for this bank transfer. |
| `mtype` | [`BankTransferType`](../../doc/models/bank-transfer-type.md) | Required | The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account. |
| `user` | [`BankTransferUser`](../../doc/models/bank-transfer-user.md) | Required | The legal name and other information for the account holder. |
| `amount` | `str` | Required | The amount of the bank transfer (decimal string with two digits of precision e.g. “10.00”). |
| `iso_currency_code` | `str` | Required | The currency of the transfer amount, e.g. "USD" |
| `description` | `str` | Required | The description of the transfer. |
| `created` | `datetime` | Required | The datetime when this bank transfer was created. This will be of the form `2006-01-02T15:04:05Z` |
| `status` | [`BankTransferStatus`](../../doc/models/bank-transfer-status.md) | Required | The status of the transfer. |
| `network` | [`BankTransferNetwork`](../../doc/models/bank-transfer-network.md) | Required | The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`. |
| `cancellable` | `bool` | Required | When `true`, you can still cancel this bank transfer. |
| `failure_reason` | [`BankTransferFailure`](../../doc/models/bank-transfer-failure.md) | Required | The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise. |
| `custom_tag` | `str` | Required | A string containing the custom tag provided by the client in the create request. Will be null if not provided. |
| `metadata` | `Dict[str, str]` | Required | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:<br><br>- The JSON values must be Strings (no nested JSON objects allowed)<br>- Only ASCII characters may be used<br>- Maximum of 50 key/value pairs<br>- Maximum key length of 40 characters<br>- Maximum value length of 500 characters |
| `origination_account_id` | `str` | Required | Plaid’s unique identifier for the origination account that was used for this transfer. |
| `direction` | [`BankTransferDirection`](../../doc/models/bank-transfer-direction.md) | Required | Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "ach_class": "cbr",
  "account_id": "account_id2",
  "type": "debit",
  "user": {
    "legal_name": "legal_name8",
    "email_address": "email_address2",
    "routing_number": "routing_number4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "amount": "amount2",
  "iso_currency_code": "iso_currency_code6",
  "description": "description0",
  "created": "2016-03-13T12:52:32.123Z",
  "status": "cancelled",
  "network": "same-day-ach",
  "cancellable": false,
  "failure_reason": {
    "ach_return_code": "ach_return_code6",
    "description": "description0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "custom_tag": "custom_tag2",
  "metadata": {
    "key0": "metadata7",
    "key1": "metadata6",
    "key2": "metadata5"
  },
  "origination_account_id": "origination_account_id0",
  "direction": "outbound",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

