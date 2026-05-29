
# Item

Metadata about the Item.

*This model accepts additional fields of type Any.*

## Structure

`Item`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `str` | Required | The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive. |
| `institution_id` | `str` | Optional | The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits. |
| `webhook` | `str` | Required | The URL registered to receive webhooks for the Item. |
| `error` | [`Error`](../../doc/models/error.md) | Required | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `available_products` | [`List[Products]`](../../doc/models/products.md) | Required | A list of products available for the Item that have not yet been accessed. |
| `billed_products` | [`List[Products]`](../../doc/models/products.md) | Required | A list of products that have been billed for the Item. Note - `billed_products` is populated in all environments but only requests in Production are billed. |
| `consent_expiration_time` | `datetime` | Required | The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the `ITEM_LOGIN_REQUIRED` error state. To circumvent the `ITEM_LOGIN_REQUIRED` error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.<br><br>Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be null. |
| `update_type` | [`UpdateType`](../../doc/models/update-type.md) | Required | Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.<br><br>`background` - Item can be updated in the background<br><br>`user_present_required` - Item requires user interaction to be updated |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
    "auth",
    "balance",
    "identity"
  ],
  "billed_products": [
    "transfer",
    "assets",
    "auth"
  ],
  "consent_expiration_time": "2016-03-13T12:52:32.123Z",
  "update_type": "background",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

