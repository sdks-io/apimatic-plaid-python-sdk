
# Payment Initiation Payment List Request

PaymentInitiationPaymentListRequest defines the request schema for `/payment_initiation/payment/list`

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationPaymentListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `count` | `int` | Optional | The maximum number of payments to return. If `count` is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified).<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 200` |
| `cursor` | `datetime` | Optional | A string in RFC 3339 format (i.e. "2019-12-06T22:35:49Z"). Only payments created before the cursor will be returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "count": 10,
  "client_id": "client_id4",
  "secret": "secret8",
  "cursor": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

