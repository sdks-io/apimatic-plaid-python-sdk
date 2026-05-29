
# Custom Header Signature



Documentation for accessing and setting credentials for PLAID-SECRET.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| PLAID-SECRET | `str` | - | `plaid_secret` |



**Note:** Auth credentials can be set using `PlaidSecretCredentials` object, passed in as named parameter `plaid_secret_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from plaid.http.auth.plaid_secret import PlaidSecretCredentials
from plaid.plaid_client import PlaidClient

client = PlaidClient(
    plaid_secret_credentials=PlaidSecretCredentials(
        plaid_secret='PLAID-SECRET'
    )
)
```


