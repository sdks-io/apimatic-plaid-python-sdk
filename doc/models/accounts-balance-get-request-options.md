
# Accounts Balance Get Request Options

An optional object to filter `/accounts/balance/get` results.

*This model accepts additional fields of type Any.*

## Structure

`AccountsBalanceGetRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_ids` | `List[str]` | Optional | A list of `account_ids` to retrieve for the Item. The default value is `null`.<br><br>Note: An error will be returned if a provided `account_id` is not associated with the Item. |
| `min_last_updated_datetime` | `datetime` | Optional | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the oldest acceptable balance when making a request to `/accounts/balance/get`.<br><br>If the balance that is pulled for `ins_128026` (Capital One) is older than the given timestamp, an `INVALID_REQUEST` error with the code of `LAST_UPDATED_DATETIME_OUT_OF_RANGE` will be returned with the most recent timestamp for the requested account contained in the response.<br><br>This field is only used when the institution is `ins_128026` (Capital One), in which case a value must be provided or an `INVALID_REQUEST` error with the code of `INVALID_FIELD` will be returned. For all other institutions, this field is ignored. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_ids": [
    "account_ids5",
    "account_ids6",
    "account_ids7"
  ],
  "min_last_updated_datetime": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

