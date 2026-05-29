
# Decision

A decision regarding the proposed transfer.

`approved` – The proposed transfer has received the end user's consent and has been approved for processing. Plaid has also reviewed the proposed transfer and has approved it for processing.

`permitted` – Plaid was unable to fetch the information required to approve or decline the proposed transfer. You may proceed with the transfer, but further review is recommended. Plaid is awaiting further instructions from the client.

`declined` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details.

*This model accepts additional fields of type Any.*

## Enumeration

`Decision`

## Fields

| Name |
|  --- |
| `APPROVED` |
| `PERMITTED` |
| `DECLINED` |

