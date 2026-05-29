# Application

```python
application_api = client.application
```

## Class Name

`ApplicationApi`


# Application Get

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

```python
def application_get(self,
                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApplicationGetRequest`](../../doc/models/application-get-request.md) | Body, Required | - |

## Response Type

**200**: success

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApplicationGetResponse`](../../doc/models/application-get-response.md).

## Example Usage

```python
body = ApplicationGetRequest(
    client_id='client_id8',
    secret='secret8',
    application_id='application_id8'
)

result = application_api.application_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

