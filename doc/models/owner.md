
# Owner

Data returned from the financial institution about the owner or owners of an account. Only the `names` array must be non-empty.

*This model accepts additional fields of type Any.*

## Structure

`Owner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `names` | `List[str]` | Required | A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. If the name of a business is reported, please contact Plaid Support. In the case of a joint account, Plaid will make a best effort to report the names of all account holders.<br><br>If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array. |
| `phone_numbers` | [`List[PhoneNumber]`](../../doc/models/phone-number.md) | Required | A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. |
| `emails` | [`List[Email]`](../../doc/models/email.md) | Required | A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Required | Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "names": [
    "names0"
  ],
  "phone_numbers": [
    {
      "data": "data0",
      "primary": false,
      "type": "office",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "emails": [
    {
      "data": "data6",
      "primary": false,
      "type": "other",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "addresses": [
    {
      "data": {
        "city": "city0",
        "region": "region6",
        "street": "street0",
        "postal_code": "postal_code2",
        "country": "country4",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "primary": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

