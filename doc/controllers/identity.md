# Identity

```python
identity_api = client.identity
```

## Class Name

`IdentityApi`


# Identity Get

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

Note: This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Find out more here: [/api/products/#identityget](/api/products/#identityget)

```python
def identity_get(self,
                body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`IdentityGetRequest`](../../doc/models/identity-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IdentityGetResponse`](../../doc/models/identity-get-response.md).

## Example Usage

```python
body = IdentityGetRequest(
    access_token='access_token4'
)

result = identity_api.identity_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

