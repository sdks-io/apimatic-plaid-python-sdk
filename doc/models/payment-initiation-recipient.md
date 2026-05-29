
# Payment Initiation Recipient

PaymentInitiationRecipient defines a payment initiation recipient

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationRecipient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_id` | `str` | Required | The ID of the recipient. |
| `name` | `str` | Required | The name of the recipient. |
| `address` | [`PaymentInitiationAddress`](../../doc/models/payment-initiation-address.md) | Optional | The optional address of the payment recipient. This object is not currently required to make payments from UK institutions and should not be populated, though may be necessary for future European expansion. |
| `iban` | `str` | Optional | The International Bank Account Number (IBAN) for the recipient. |
| `bacs` | [`RecipientBacsNullable`](../../doc/models/recipient-bacs-nullable.md) | Optional | - |
| `emi_recipient_id` | `str` | Optional | The EMI (E-Money Institution) recipient that this recipient is associated with, if any. This EMI recipient is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "recipient_id": "recipient_id8",
  "name": "name2",
  "address": {
    "street": [
      "street1"
    ],
    "city": "city6",
    "postal_code": "postal_code8",
    "country": "country0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "iban": "iban6",
  "bacs": {
    "account": "account4",
    "sort_code": "sort_code4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "emi_recipient_id": "emi_recipient_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

