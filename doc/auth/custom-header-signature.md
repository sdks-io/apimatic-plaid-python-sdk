
# Custom Header Signature



Documentation for accessing and setting credentials for PLAID-CLIENT-ID.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| PLAID-CLIENT-ID | `str` | - | `plaid_client_id` |



**Note:** Auth credentials can be set using `PlaidClientIdCredentials` object, passed in as named parameter `plaid_client_id_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from plaid.http.auth.plaid_client_id import PlaidClientIdCredentials
from plaid.plaid_client import PlaidClient

client = PlaidClient(
    plaid_client_id_credentials=PlaidClientIdCredentials(
        plaid_client_id='PLAID-CLIENT-ID'
    )
)
```


