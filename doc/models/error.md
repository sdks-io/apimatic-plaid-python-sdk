
# Error

We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred.

*This model accepts additional fields of type Any.*

## Structure

`Error`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_type` | [`ErrorType`](../../doc/models/error-type.md) | Required | A broad categorization of the error. Safe for programatic use. |
| `error_code` | `str` | Required | The particular error code. Safe for programmatic use. |
| `error_message` | `str` | Required | A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use. |
| `display_message` | `str` | Required | A user-friendly representation of the error code. `null` if the error is not related to user action.<br><br>This may change over time and is not safe for programmatic use. |
| `request_id` | `str` | Optional | A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks. |
| `causes` | `List[Any]` | Optional | In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.<br><br>`causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. |
| `status` | `float` | Optional | The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook. |
| `documentation_url` | `str` | Optional | The URL of a Plaid documentation page with more information about the error |
| `suggested_action` | `str` | Optional | Suggested steps for resolving the error |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "error_type": "PAYMENT_ERROR",
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
  "status": 45.24,
  "documentation_url": "documentation_url6",
  "suggested_action": "suggested_action0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

