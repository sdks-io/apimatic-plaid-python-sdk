
# Transfer Authorization Create Response

Defines the response schema for `/transfer/authorization/create`

*This model accepts additional fields of type Any.*

## Structure

`TransferAuthorizationCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | [`TransferAuthorization`](../../doc/models/transfer-authorization.md) | Required | TransferAuthorization contains the authorization decision for a proposed transfer |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "authorization": {
    "id": "id6",
    "created": "created6",
    "decision": "approved",
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
  },
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

