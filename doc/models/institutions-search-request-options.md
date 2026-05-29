
# Institutions Search Request Options

An optional object to filter `/institutions/search` results.

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsSearchRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `oauth` | `bool` | Optional | Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with European country codes |
| `include_optional_metadata` | `bool` | Optional | When true, return the institution's homepage URL, logo and primary brand color. |
| `include_auth_metadata` | `bool` | Optional | When `true`, returns metadata related to the Auth product indicating which auth methods are supported.<br><br>**Default**: `False` |
| `include_payment_initiation_metadata` | `bool` | Optional | When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.<br><br>**Default**: `False` |
| `payment_initiation` | [`InstitutionsSearchPaymentInitiationOptions`](../../doc/models/institutions-search-payment-initiation-options.md) | Optional | Additional options that will be used to filter institutions by various Payment Initiation configurations. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "include_auth_metadata": false,
  "include_payment_initiation_metadata": false,
  "oauth": false,
  "include_optional_metadata": false,
  "payment_initiation": {
    "payment_id": "payment_id6",
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

