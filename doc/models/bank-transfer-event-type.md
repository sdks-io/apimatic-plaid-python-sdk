
# Bank Transfer Event Type

The type of event that this bank transfer represents.

`pending`: A new transfer was created; it is in the pending state.

`cancelled`: The transfer was cancelled by the client.

`failed`: The transfer failed, no funds were moved.

`posted`: The transfer has been successfully submitted to the payment network.

`reversed`: A posted transfer was reversed.

`receiver_pending`: The matching transfer was found as a pending transaction in the receiver's account

`receiver_posted`: The matching transfer was found as a posted transaction in the receiver's account

*This model accepts additional fields of type Any.*

## Enumeration

`BankTransferEventType`

## Fields

| Name |
|  --- |
| `PENDING` |
| `CANCELLED` |
| `FAILED` |
| `POSTED` |
| `REVERSED` |
| `RECEIVER_PENDING` |
| `RECEIVER_POSTED` |

