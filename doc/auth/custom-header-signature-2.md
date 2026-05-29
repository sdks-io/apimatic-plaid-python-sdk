
# Custom Header Signature



Documentation for accessing and setting credentials for Plaid-Version.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Plaid-Version | `str` | - | `plaid_version` |



**Note:** Auth credentials can be set using `PlaidVersionCredentials` object, passed in as named parameter `plaid_version_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from plaid.http.auth.plaid_version import PlaidVersionCredentials
from plaid.plaid_client import PlaidClient

client = PlaidClient(
    plaid_version_credentials=PlaidVersionCredentials(
        plaid_version='Plaid-Version'
    )
)
```


