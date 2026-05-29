
# Transfer List Request

Defines the request schema for `/transfer/list`

*This model accepts additional fields of type Any.*

## Structure

`TransferListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `start_date` | `datetime` | Optional | The start datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`) |
| `end_date` | `datetime` | Optional | The end datetime of transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`) |
| `count` | `int` | Optional | The maximum number of transfers to return.<br><br>**Default**: `25`<br><br>**Constraints**: `>= 1`, `<= 25` |
| `offset` | `int` | Optional | The number of transfers to skip before returning results.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `origination_account_id` | `str` | Optional | Filter transfers to only those originated through the specified origination account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "count": 25,
  "offset": 0,
  "client_id": "client_id0",
  "secret": "secret4",
  "start_date": "2016-03-13T12:52:32.123Z",
  "end_date": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

