# Asset Report

```python
asset_report_api = client.asset_report
```

## Class Name

`AssetReportApi`

## Methods

* [Asset Report Audit Copy Create](../../doc/controllers/asset-report.md#asset-report-audit-copy-create)
* [Asset Report Refresh](../../doc/controllers/asset-report.md#asset-report-refresh)
* [Asset Report Filter](../../doc/controllers/asset-report.md#asset-report-filter)
* [Asset Report Create](../../doc/controllers/asset-report.md#asset-report-create)
* [Asset Report Remove](../../doc/controllers/asset-report.md#asset-report-remove)
* [Asset Report Pdf Get](../../doc/controllers/asset-report.md#asset-report-pdf-get)
* [Asset Report Get](../../doc/controllers/asset-report.md#asset-report-get)
* [Asset Report Audit Copy Remove](../../doc/controllers/asset-report.md#asset-report-audit-copy-remove)
* [Asset Report Audit Copy Get](../../doc/controllers/asset-report.md#asset-report-audit-copy-get)


# Asset Report Audit Copy Create

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

Find out more here: [/api/products/#asset_reportaudit_copycreate](/api/products/#asset_reportaudit_copycreate)

```python
def asset_report_audit_copy_create(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportAuditCopyCreateRequest`](../../doc/models/asset-report-audit-copy-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportAuditCopyCreateResponse`](../../doc/models/asset-report-audit-copy-create-response.md).

## Example Usage

```python
body = AssetReportAuditCopyCreateRequest(
    asset_report_token='asset_report_token6',
    auditor_id='auditor_id2'
)

result = asset_report_api.asset_report_audit_copy_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "audit_copy_token": "a-sandbox-3TAU2CWVYBDVRHUCAAAI27ULU4",
  "request_id": "Iam3b"
}
```


# Asset Report Refresh

An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

Find out more here: [/api/products/#asset_reportrefresh](/api/products/#asset_reportrefresh)

```python
def asset_report_refresh(self,
                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportRefreshRequest`](../../doc/models/asset-report-refresh-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportRefreshResponse`](../../doc/models/asset-report-refresh-response.md).

## Example Usage

```python
body = AssetReportRefreshRequest(
    asset_report_token='asset_report_token6'
)

result = asset_report_api.asset_report_refresh(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "asset_report_id": "c33ebe8b-6a63-4d74-a83d-d39791231ac0",
  "asset_report_token": "assets-sandbox-8218d5f8-6d6d-403d-92f5-13a9afaa4398",
  "request_id": "NBZaq"
}
```


# Asset Report Filter

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/webhooks) webhook once generation of the filtered Asset Report has completed.

Find out more here: [/api/products/#asset_reportfilter](/api/products/#asset_reportfilter)

```python
def asset_report_filter(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportFilterRequest`](../../doc/models/asset-report-filter-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportFilterResponse`](../../doc/models/asset-report-filter-response.md).

## Example Usage

```python
body = AssetReportFilterRequest(
    asset_report_token='asset_report_token6',
    account_ids_to_exclude=[
        'account_ids_to_exclude7',
        'account_ids_to_exclude8'
    ]
)

result = asset_report_api.asset_report_filter(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "asset_report_token": "assets-sandbox-bc410c6a-4653-4c75-985c-e757c3497c5c",
  "asset_report_id": "fdc09207-0cef-4d88-b5eb-0d970758ebd9",
  "request_id": "qEg07"
}
```


# Asset Report Create

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/webhooks/#Assets-webhooks).

The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

Find out more here: [/api/products/#asset_reportcreate](/api/products/#asset_reportcreate)

```python
def asset_report_create(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportCreateRequest`](../../doc/models/asset-report-create-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportCreateResponse`](../../doc/models/asset-report-create-response.md).

## Example Usage

```python
body = AssetReportCreateRequest(
    access_tokens=[
        'access_tokens8',
        'access_tokens9',
        'access_tokens0'
    ],
    days_requested=64
)

result = asset_report_api.asset_report_create(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "asset_report_token": "assets-sandbox-6f12f5bb-22dd-4855-b918-f47ec439198a",
  "asset_report_id": "1f414183-220c-44f5-b0c8-bc0e6d4053bb",
  "request_id": "Iam3b"
}
```


# Asset Report Remove

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

Find out more here: [/api/products/#asset_reportremove](/api/products/#asset_reportremove)

```python
def asset_report_remove(self,
                       body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportRemoveRequest`](../../doc/models/asset-report-remove-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportRemoveResponse`](../../doc/models/asset-report-remove-response.md).

## Example Usage

```python
body = AssetReportRemoveRequest(
    asset_report_token='asset_report_token6'
)

result = asset_report_api.asset_report_remove(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "removed": true,
  "request_id": "I6zHN"
}
```


# Asset Report Pdf Get

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/webhooks) webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

Find out more here: [/api/products/#asset_reportpdfget](/api/products/#asset_reportpdfget)

```python
def asset_report_pdf_get(self,
                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportPdfGetRequest`](../../doc/models/asset-report-pdf-get-request.md) | Body, Required | - |

## Response Type

**200**: A PDF of the Asset Report

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = AssetReportPdfGetRequest(
    asset_report_token='asset_report_token6'
)

result = asset_report_api.asset_report_pdf_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Asset Report Get

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/webhooks) webhook to fire, indicating that the Report is ready to be retrieved.

By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.

To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

Find out more here: [/api/products/#asset_reportget](/api/products/#asset_reportget)

```python
def asset_report_get(self,
                    body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportGetRequest`](../../doc/models/asset-report-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportGetResponse`](../../doc/models/asset-report-get-response.md).

## Example Usage

```python
body = AssetReportGetRequest(
    asset_report_token='asset_report_token6'
)

result = asset_report_api.asset_report_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "report": {
    "asset_report_id": "bf3a0490-344c-4620-a219-2693162e4b1d",
    "client_report_id": "123abc",
    "date_generated": "2020-06-05T22:47:53Z",
    "days_requested": 3,
    "items": [
      {
        "accounts": [
          {
            "account_id": "3gE5gnRzNyfXpBK5wEEKcymJ5albGVUqg77gr",
            "balances": {
              "available": 200,
              "current": 210,
              "iso_currency_code": "USD",
              "limit": null,
              "unofficial_currency_code": null
            },
            "days_available": 3,
            "historical_balances": [
              {
                "current": 210,
                "date": "2020-06-04",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              },
              {
                "current": 210,
                "date": "2020-06-03",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              },
              {
                "current": 210,
                "date": "2020-06-02",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              }
            ],
            "mask": "1111",
            "name": "Plaid Saving",
            "official_name": "Plaid Silver Standard 0.1% Interest Saving",
            "owners": [
              {
                "addresses": [
                  {
                    "data": {
                      "city": "Malakoff",
                      "country": "US",
                      "postal_code": "14236",
                      "region": "NY",
                      "street": "2992 Cameron Road"
                    },
                    "primary": true
                  },
                  {
                    "data": {
                      "city": "San Matias",
                      "country": "US",
                      "postal_code": "93405-2255",
                      "region": "CA",
                      "street": "2493 Leisure Lane"
                    },
                    "primary": false
                  }
                ],
                "emails": [
                  {
                    "data": "accountholder0@example.com",
                    "primary": true,
                    "type": "primary"
                  },
                  {
                    "data": "accountholder1@example.com",
                    "primary": false,
                    "type": "secondary"
                  },
                  {
                    "data": "extraordinarily.long.email.username.123456@reallylonghostname.com",
                    "primary": false,
                    "type": "other"
                  }
                ],
                "names": [
                  "Alberta Bobbeth Charleson"
                ],
                "phone_numbers": [
                  {
                    "data": "1112223333",
                    "primary": false,
                    "type": "home"
                  },
                  {
                    "data": "1112224444",
                    "primary": false,
                    "type": "work"
                  },
                  {
                    "data": "1112225555",
                    "primary": false,
                    "type": "mobile"
                  }
                ]
              }
            ],
            "ownership_type": null,
            "subtype": "savings",
            "transactions": [],
            "type": "depository"
          },
          {
            "account_id": "BxBXxLj1m4HMXBm9WZJyUg9XLd4rKEhw8Pb1J",
            "balances": {
              "available": null,
              "current": 56302.06,
              "iso_currency_code": "USD",
              "limit": null,
              "unofficial_currency_code": null
            },
            "days_available": 3,
            "historical_balances": [],
            "mask": "8888",
            "name": "Plaid Mortgage",
            "official_name": null,
            "owners": [
              {
                "addresses": [
                  {
                    "data": {
                      "city": "Malakoff",
                      "country": "US",
                      "postal_code": "14236",
                      "region": "NY",
                      "street": "2992 Cameron Road"
                    },
                    "primary": true
                  },
                  {
                    "data": {
                      "city": "San Matias",
                      "country": "US",
                      "postal_code": "93405-2255",
                      "region": "CA",
                      "street": "2493 Leisure Lane"
                    },
                    "primary": false
                  }
                ],
                "emails": [
                  {
                    "data": "accountholder0@example.com",
                    "primary": true,
                    "type": "primary"
                  },
                  {
                    "data": "accountholder1@example.com",
                    "primary": false,
                    "type": "secondary"
                  },
                  {
                    "data": "extraordinarily.long.email.username.123456@reallylonghostname.com",
                    "primary": false,
                    "type": "other"
                  }
                ],
                "names": [
                  "Alberta Bobbeth Charleson"
                ],
                "phone_numbers": [
                  {
                    "data": "1112223333",
                    "primary": false,
                    "type": "home"
                  },
                  {
                    "data": "1112224444",
                    "primary": false,
                    "type": "work"
                  },
                  {
                    "data": "1112225555",
                    "primary": false,
                    "type": "mobile"
                  }
                ]
              }
            ],
            "ownership_type": null,
            "subtype": "mortgage",
            "transactions": [],
            "type": "loan"
          },
          {
            "account_id": "dVzbVMLjrxTnLjX4G66XUp5GLklm4oiZy88yK",
            "balances": {
              "available": null,
              "current": 410,
              "iso_currency_code": "USD",
              "limit": null,
              "unofficial_currency_code": null
            },
            "days_available": 3,
            "historical_balances": [
              {
                "current": 410,
                "date": "2020-06-04",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              },
              {
                "current": 410,
                "date": "2020-06-03",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              },
              {
                "current": 410,
                "date": "2020-06-02",
                "iso_currency_code": "USD",
                "unofficial_currency_code": null
              }
            ],
            "mask": "3333",
            "name": "Plaid Credit Card",
            "official_name": "Plaid Diamond 12.5% APR Interest Credit Card",
            "owners": [
              {
                "addresses": [
                  {
                    "data": {
                      "city": "Malakoff",
                      "country": "US",
                      "postal_code": "14236",
                      "region": "NY",
                      "street": "2992 Cameron Road"
                    },
                    "primary": true
                  },
                  {
                    "data": {
                      "city": "San Matias",
                      "country": "US",
                      "postal_code": "93405-2255",
                      "region": "CA",
                      "street": "2493 Leisure Lane"
                    },
                    "primary": false
                  }
                ],
                "emails": [
                  {
                    "data": "accountholder0@example.com",
                    "primary": true,
                    "type": "primary"
                  },
                  {
                    "data": "accountholder1@example.com",
                    "primary": false,
                    "type": "secondary"
                  },
                  {
                    "data": "extraordinarily.long.email.username.123456@reallylonghostname.com",
                    "primary": false,
                    "type": "other"
                  }
                ],
                "names": [
                  "Alberta Bobbeth Charleson"
                ],
                "phone_numbers": [
                  {
                    "data": "1112223333",
                    "primary": false,
                    "type": "home"
                  },
                  {
                    "data": "1112224444",
                    "primary": false,
                    "type": "work"
                  },
                  {
                    "data": "1112225555",
                    "primary": false,
                    "type": "mobile"
                  }
                ]
              }
            ],
            "ownership_type": null,
            "subtype": "credit card",
            "transactions": [],
            "type": "credit"
          }
        ],
        "date_last_updated": "2020-06-05T22:47:52Z",
        "institution_id": "ins_3",
        "institution_name": "Chase",
        "item_id": "eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBFL9DrE6"
      }
    ],
    "user": {
      "client_user_id": "123456789",
      "email": "accountholder0@example.com",
      "first_name": "Alberta",
      "last_name": "Charleson",
      "middle_name": "Bobbeth",
      "phone_number": "111-222-3333",
      "ssn": "123-45-6789"
    }
  },
  "request_id": "eYupqX1mZkEuQRx",
  "warnings": []
}
```


# Asset Report Audit Copy Remove

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

Find out more here: [/api/products/#asset_reportaudit_copyremove](/api/products/#asset_reportaudit_copyremove)

```python
def asset_report_audit_copy_remove(self,
                                  body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportAuditCopyRemoveRequest`](../../doc/models/asset-report-audit-copy-remove-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportAuditCopyRemoveResponse`](../../doc/models/asset-report-audit-copy-remove-response.md).

## Example Usage

```python
body = AssetReportAuditCopyRemoveRequest(
    audit_copy_token='audit_copy_token4'
)

result = asset_report_api.asset_report_audit_copy_remove(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "removed": true,
  "request_id": "m8MDnv9okwxFNBV"
}
```


# Asset Report Audit Copy Get

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

Find out more here: [/none/](/none/)

```python
def asset_report_audit_copy_get(self,
                               body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssetReportAuditCopyGetRequest`](../../doc/models/asset-report-audit-copy-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssetReportGetResponse`](../../doc/models/asset-report-get-response.md).

## Example Usage

```python
body = AssetReportAuditCopyGetRequest(
    audit_copy_token='audit_copy_token4'
)

result = asset_report_api.asset_report_audit_copy_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

