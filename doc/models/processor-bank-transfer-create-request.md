
# Processor Bank Transfer Create Request

Defines the request schema for `/processor/bank_transfer/create`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorBankTransferCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `idempotency_key` | `str` | Required | A random key provided by the client, per unique bank transfer. Maximum of 50 characters.<br><br>The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created.<br><br>**Constraints**: *Maximum Length*: `50` |
| `processor_token` | `str` | Required | The processor token obtained from the Plaid integration partner. Processor tokens are in the format: `processor-<environment>-<identifier>` |
| `mtype` | [`BankTransferType`](../../doc/models/bank-transfer-type.md) | Required | The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account. |
| `network` | [`BankTransferNetwork`](../../doc/models/bank-transfer-network.md) | Required | The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`. |
| `amount` | `str` | Required | The amount of the bank transfer (decimal string with two digits of precision e.g. “10.00”). |
| `iso_currency_code` | `str` | Required | The currency of the transfer amount – should be set to "USD". |
| `description` | `str` | Required | The transfer description. Maximum of 10 characters.<br><br>**Constraints**: *Maximum Length*: `10` |
| `ach_class` | [`AchClass`](../../doc/models/ach-class.md) | Optional | Specifies the use case of the transfer.  Required for transfers on an ACH network.<br><br>`"arc"` - Accounts Receivable Entry<br><br>`"cbr`" - Cross Border Entry<br><br>`"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts<br><br>`"cie"` - Customer Initiated Entry<br><br>`"cor"` - Automated Notification of Change<br><br>`"ctx"` - Corporate Trade Exchange<br><br>`"iat"` - International<br><br>`"mte"` - Machine Transfer Entry<br><br>`"pbr"` - Cross Border Entry<br><br>`"pop"` - Point-of-Purchase Entry<br><br>`"pos"` - Point-of-Sale Entry<br><br>`"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment<br><br>`"rck"` - Re-presented Check Entry<br><br>`"tel"` - Telephone-Initiated Entry<br><br>`"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet |
| `user` | [`BankTransferUser`](../../doc/models/bank-transfer-user.md) | Required | The legal name and other information for the account holder. |
| `custom_tag` | `str` | Optional | An arbitrary string provided by the client for storage with the bank transfer. May be up to 100 characters.<br><br>**Constraints**: *Maximum Length*: `100` |
| `metadata` | `Dict[str, str]` | Optional | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply:<br><br>- The JSON values must be Strings (no nested JSON objects allowed)<br>- Only ASCII characters may be used<br>- Maximum of 50 key/value pairs<br>- Maximum key length of 40 characters<br>- Maximum value length of 500 characters |
| `origination_account_id` | `str` | Optional | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "idempotency_key": "idempotency_key0",
  "processor_token": "processor_token6",
  "type": "debit",
  "network": "same-day-ach",
  "amount": "amount6",
  "iso_currency_code": "iso_currency_code2",
  "description": "description6",
  "ach_class": "ctx",
  "user": {
    "legal_name": "legal_name8",
    "email_address": "email_address2",
    "routing_number": "routing_number4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "custom_tag": "custom_tag4",
  "metadata": {
    "key0": "metadata9",
    "key1": "metadata0"
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

