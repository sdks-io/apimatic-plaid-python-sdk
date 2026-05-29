# Institutions

```python
institutions_api = client.institutions
```

## Class Name

`InstitutionsApi`

## Methods

* [Institutions Get by Id](../../doc/controllers/institutions.md#institutions-get-by-id)
* [Institutions Get](../../doc/controllers/institutions.md#institutions-get)
* [Institutions Search](../../doc/controllers/institutions.md#institutions-search)


# Institutions Get by Id

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

Find out more here: [/api/institutions/#institutionsget_by_id](/api/institutions/#institutionsget_by_id)

```python
def institutions_get_by_id(self,
                          body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InstitutionsGetByIdRequest`](../../doc/models/institutions-get-by-id-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InstitutionsGetByIdResponse`](../../doc/models/institutions-get-by-id-response.md).

## Example Usage

```python
body = InstitutionsGetByIdRequest(
    institution_id='institution_id4',
    country_codes=[
        CountryCode.CA
    ]
)

result = institutions_api.institutions_get_by_id(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "institution": {
    "country_codes": [
      "US"
    ],
    "institution_id": "ins_109512",
    "name": "Houndstooth Bank",
    "products": [
      "auth",
      "balance",
      "identity",
      "transactions"
    ],
    "routing_numbers": [
      "110000000"
    ],
    "oauth": false,
    "status": {
      "item_logins": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-15T15:53:00Z",
        "breakdown": {
          "success": 0.9,
          "error_plaid": 0.01,
          "error_institution": 0.09
        }
      },
      "transactions_updates": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-12T08:22:00Z",
        "breakdown": {
          "success": 0.95,
          "error_plaid": 0.02,
          "error_institution": 0.03,
          "refresh_interval": "NORMAL"
        }
      },
      "auth": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-15T15:53:00Z",
        "breakdown": {
          "success": 0.91,
          "error_plaid": 0.01,
          "error_institution": 0.08
        }
      },
      "balance": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-15T15:53:00Z",
        "breakdown": {
          "success": 0.89,
          "error_plaid": 0.02,
          "error_institution": 0.09
        }
      },
      "identity": {
        "status": "DEGRADED",
        "last_status_change": "2019-02-15T15:50:00Z",
        "breakdown": {
          "success": 0.42,
          "error_plaid": 0.08,
          "error_institution": 0.5
        }
      },
      "investments": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-15T15:53:00Z",
        "breakdown": {
          "success": 0.89,
          "error_plaid": 0.02,
          "error_institution": 0.09
        },
        "liabilities": {
          "status": "HEALTHY",
          "last_status_change": "2019-02-15T15:53:00Z",
          "breakdown": {
            "success": 0.89,
            "error_plaid": 0.02,
            "error_institution": 0.09
          }
        }
      },
      "investments_updates": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-12T08:22:00Z",
        "breakdown": {
          "success": 0.95,
          "error_plaid": 0.02,
          "error_institution": 0.03,
          "refresh_interval": "NORMAL"
        }
      },
      "liabilities_updates": {
        "status": "HEALTHY",
        "last_status_change": "2019-02-12T08:22:00Z",
        "breakdown": {
          "success": 0.95,
          "error_plaid": 0.02,
          "error_institution": 0.03,
          "refresh_interval": "NORMAL"
        }
      },
      "primary_color": "#004966",
      "url": "https://plaid.com",
      "logo": null
    }
  },
  "request_id": "m8MDnv9okwxFNBV"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Institutions Get

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

Find out more here: [/api/institutions/#institutionsget](/api/institutions/#institutionsget)

```python
def institutions_get(self,
                    body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InstitutionsGetRequest`](../../doc/models/institutions-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InstitutionsGetResponse`](../../doc/models/institutions-get-response.md).

## Example Usage

```python
body = InstitutionsGetRequest(
    count=52,
    offset=4,
    country_codes=[
        CountryCode.CA
    ]
)

result = institutions_api.institutions_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "institutions": [
    {
      "country_codes": [
        "US"
      ],
      "institution_id": "ins_1",
      "name": "Bank of America",
      "oauth": false,
      "products": [
        "assets",
        "auth",
        "balance",
        "transactions",
        "identity",
        "liabilities"
      ],
      "routing_numbers": [
        "011000138",
        "011200365",
        "011400495",
        "011500010",
        "011900254",
        "021000322",
        "021200339",
        "026009593",
        "031202084",
        "051000017",
        "052001633",
        "053000196",
        "053904483",
        "054001204",
        "061000052",
        "063100277",
        "064000020",
        "071214579",
        "072000805",
        "073000176",
        "081000032",
        "081904808",
        "082000073",
        "101100045",
        "103000017",
        "107000327",
        "111000025",
        "121000358",
        "122101706",
        "122400724",
        "123103716",
        "125000024",
        "323070380"
      ]
    }
  ],
  "request_id": "tbFyCEqkU774ZGG",
  "total": 11384
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Institutions Search

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

Find out more here: [/api/institutions/#institutionssearch](/api/institutions/#institutionssearch)

```python
def institutions_search(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InstitutionsSearchRequest`](../../doc/models/institutions-search-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InstitutionsSearchResponse`](../../doc/models/institutions-search-response.md).

## Example Usage

```python
body = InstitutionsSearchRequest(
    query='query6',
    products=[
        Products.BALANCE
    ],
    country_codes=[
        CountryCode.CA
    ]
)

result = institutions_api.institutions_search(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "institutions": [
    {
      "country_codes": [
        "US"
      ],
      "institution_id": "ins_118923",
      "name": "Red Platypus Bank - Red Platypus Bank",
      "oauth": false,
      "products": [
        "assets",
        "auth",
        "balance",
        "transactions",
        "identity"
      ],
      "routing_numbers": []
    }
  ],
  "request_id": "Ggmk0enW4smO2Tp"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

