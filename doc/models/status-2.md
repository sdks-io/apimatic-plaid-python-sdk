
# Status 2

The status of the refund.

`PROCESSING`: The refund is currently being processed. The refund will automatically exit this state when processing is complete.

`INITIATED`: The refund has been successfully initiated.

`EXECUTED`: Indicates that the refund has been successfully executed.

`FAILED`: The refund has failed to be executed. This error is retryable once the root cause is resolved.

*This model accepts additional fields of type Any.*

## Enumeration

`Status2`

## Fields

| Name |
|  --- |
| `PROCESSING` |
| `EXECUTED` |
| `INITIATED` |
| `FAILED` |

