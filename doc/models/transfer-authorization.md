
# Transfer Authorization

TransferAuthorization contains the authorization decision for a proposed transfer

*This model accepts additional fields of type Any.*

## Structure

`TransferAuthorization`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Plaid’s unique identifier for a transfer authorization. |
| `created` | `str` | Required | The datetime representing when the authorization was created, in the format "2006-01-02T15:04:05Z". |
| `decision` | [`Decision`](../../doc/models/decision.md) | Required | A decision regarding the proposed transfer.<br><br>`approved` – The proposed transfer has received the end user's consent and has been approved for processing. Plaid has also reviewed the proposed transfer and has approved it for processing.<br><br>`permitted` – Plaid was unable to fetch the information required to approve or decline the proposed transfer. You may proceed with the transfer, but further review is recommended. Plaid is awaiting further instructions from the client.<br><br>`declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details. |
| `decision_rationale` | [`TransferAuthorizationDecisionRationale`](../../doc/models/transfer-authorization-decision-rationale.md) | Required | The rationale for Plaid's decision regarding a proposed transfer. Will be null for `approved` decisions. |
| `proposed_transfer` | [`TransferAuthorizationProposedTransfer`](../../doc/models/transfer-authorization-proposed-transfer.md) | Required | Details regarding the proposed transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id6",
  "created": "created6",
  "decision": "declined",
  "decision_rationale": {
    "code": "RISK",
    "description": "description8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "proposed_transfer": {
    "ach_class": "web",
    "account_id": "account_id0",
    "type": "debit",
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
    "amount": "amount0",
    "network": "network6",
    "origination_account_id": "origination_account_id8",
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
```

