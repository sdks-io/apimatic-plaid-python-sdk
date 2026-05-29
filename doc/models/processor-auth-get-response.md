
# Processor Auth Get Response

ProcessorAuthGetResponse defines the response schema for `/processor/auth/get`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorAuthGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `numbers` | [`ProcessorNumber`](../../doc/models/processor-number.md) | Required | An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned. |
| `account` | [`Account`](../../doc/models/account.md) | Required | A single account at a financial institution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "request_id": "request_id2",
  "numbers": {
    "ach": {
      "account_id": "account_id8",
      "account": "account6",
      "routing": "routing2",
      "wire_routing": "wire_routing4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "eft": {
      "account_id": "account_id4",
      "account": "account2",
      "institution": "institution2",
      "branch": "branch8",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "international": {
      "account_id": "account_id2",
      "iban": "iban4",
      "bic": "bic2",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "bacs": {
      "account_id": "account_id6",
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
  "account": {
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
    "type": "brokerage",
    "subtype": "tfsa",
    "verification_status": "pending_manual_verification",
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

