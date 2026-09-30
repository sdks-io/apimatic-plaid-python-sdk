# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [ThePlaidApiClient](the_plaid_api/client.py)

## Accounts

> Source: [Accounts](the_plaid_api/apis/accounts.py)

<details>
<summary><code>def accounts_balance_get(body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AccountsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.accounts.accounts_balance_get(
        AccountsBalanceGetRequest(
            access_token="string",
            secret="string",
            client_id="string",
            options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.accounts.accounts_balance_get(
        AccountsBalanceGetRequest(
            access_token="string",
            secret="string",
            client_id="string",
            options=AccountsBalanceGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountsBalanceGetRequest](the_plaid_api/models/accounts_balance_get_request.py) \| [AccountsBalanceGetRequestDict](the_plaid_api/models/accounts_balance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def accounts_get(body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AccountsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/accounts/get`  endpoint can be used to retrieve information for any linked Item. Note that some information is nullable. Plaid will only return active bank accounts, i.e. accounts that are not closed and are capable of carrying a balance.

This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.accounts.accounts_get(
        AccountsGetRequest(
            client_id="string",
            secret="string",
            access_token="string",
            options=AccountsGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.accounts.accounts_get(
        AccountsGetRequest(
            client_id="string",
            secret="string",
            access_token="string",
            options=AccountsGetRequestOptions(account_ids=["string"]),
        ),
    )
    # TODO: Handle 'response' of type AccountsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountsGetRequest](the_plaid_api/models/accounts_get_request.py) \| [AccountsGetRequestDict](the_plaid_api/models/accounts_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AccountsGetResponse](the_plaid_api/models/accounts_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ApplicationApi

> Source: [ApplicationApi](the_plaid_api/apis/application_api.py)

<details>
<summary><code>def application_get(body: ApplicationGetRequest | ApplicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApplicationGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.application_api.application_get(
        ApplicationGetRequest(
            client_id="some example string", secret="some example string", application_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ApplicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.application_api.application_get(
        ApplicationGetRequest(
            client_id="some example string", secret="some example string", application_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ApplicationGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ApplicationGetRequest](the_plaid_api/models/application_get_request.py) \| [ApplicationGetRequestDict](the_plaid_api/models/application_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApplicationGetResponse](the_plaid_api/models/application_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AssetReportApi

> Source: [AssetReportApi](the_plaid_api/apis/asset_report_api.py)

<details>
<summary><code>def asset_report_audit_copy_create(body: AssetReportAuditCopyCreateRequest | AssetReportAuditCopyCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportAuditCopyCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_audit_copy_create(
        AssetReportAuditCopyCreateRequest(asset_report_token="some example string", auditor_id="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_audit_copy_create(
        AssetReportAuditCopyCreateRequest(asset_report_token="some example string", auditor_id="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyCreateRequest](the_plaid_api/models/asset_report_audit_copy_create_request.py) \| [AssetReportAuditCopyCreateRequestDict](the_plaid_api/models/asset_report_audit_copy_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportAuditCopyCreateResponse](the_plaid_api/models/asset_report_audit_copy_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_get(body: AssetReportAuditCopyGetRequest | AssetReportAuditCopyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_audit_copy_get(
        AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_audit_copy_get(
        AssetReportAuditCopyGetRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyGetRequest](the_plaid_api/models/asset_report_audit_copy_get_request.py) \| [AssetReportAuditCopyGetRequestDict](the_plaid_api/models/asset_report_audit_copy_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_audit_copy_remove(body: AssetReportAuditCopyRemoveRequest | AssetReportAuditCopyRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportAuditCopyRemoveResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_audit_copy_remove(
        AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_audit_copy_remove(
        AssetReportAuditCopyRemoveRequest(audit_copy_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportAuditCopyRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportAuditCopyRemoveRequest](the_plaid_api/models/asset_report_audit_copy_remove_request.py) \| [AssetReportAuditCopyRemoveRequestDict](the_plaid_api/models/asset_report_audit_copy_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportAuditCopyRemoveResponse](the_plaid_api/models/asset_report_audit_copy_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_create(body: AssetReportCreateRequest | AssetReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/webhooks/#Assets-webhooks).

The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_create(
        AssetReportCreateRequest(access_tokens=["some example string"], days_requested=1)
    )
    # TODO: Handle 'response' of type AssetReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_create(
        AssetReportCreateRequest(access_tokens=["some example string"], days_requested=1)
    )
    # TODO: Handle 'response' of type AssetReportCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportCreateRequest](the_plaid_api/models/asset_report_create_request.py) \| [AssetReportCreateRequestDict](the_plaid_api/models/asset_report_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportCreateResponse](the_plaid_api/models/asset_report_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_filter(body: AssetReportFilterRequest | AssetReportFilterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportFilterResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

Plaid will fire a https://plaid.com/docs/api/webhooks webhook once generation of the filtered Asset Report has completed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_filter(
        AssetReportFilterRequest(
            asset_report_token="some example string", account_ids_to_exclude=["some example string"]
        ),
    )
    # TODO: Handle 'response' of type AssetReportFilterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_filter(
        AssetReportFilterRequest(
            asset_report_token="some example string", account_ids_to_exclude=["some example string"]
        ),
    )
    # TODO: Handle 'response' of type AssetReportFilterResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportFilterRequest](the_plaid_api/models/asset_report_filter_request.py) \| [AssetReportFilterRequestDict](the_plaid_api/models/asset_report_filter_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportFilterResponse](the_plaid_api/models/asset_report_filter_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_get(body: AssetReportGetRequest | AssetReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the https://plaid.com/docs/api/webhooks webhook to fire, indicating that the Report is ready to be retrieved.

By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.

To retrieve an Asset Report with Insights, call the `/asset_report/get` endpoint with `include_insights` set to `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_get(AssetReportGetRequest(asset_report_token="some example string"))
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_get(
        AssetReportGetRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportGetRequest](the_plaid_api/models/asset_report_get_request.py) \| [AssetReportGetRequestDict](the_plaid_api/models/asset_report_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportGetResponse](the_plaid_api/models/asset_report_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_pdf_get(body: AssetReportPdfgetRequest | AssetReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the https://plaid.com/docs/api/webhooks webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.asset_report_api.asset_report_pdf_get(AssetReportPdfgetRequest(asset_report_token="some example string"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.asset_report_api.asset_report_pdf_get(
        AssetReportPdfgetRequest(asset_report_token="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportPdfgetRequest](the_plaid_api/models/asset_report_pdfget_request.py) \| [AssetReportPdfgetRequestDict](the_plaid_api/models/asset_report_pdfget_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_refresh(body: AssetReportRefreshRequest | AssetReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportRefreshResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_refresh(
        AssetReportRefreshRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_refresh(
        AssetReportRefreshRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportRefreshRequest](the_plaid_api/models/asset_report_refresh_request.py) \| [AssetReportRefreshRequestDict](the_plaid_api/models/asset_report_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportRefreshResponse](the_plaid_api/models/asset_report_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def asset_report_remove(body: AssetReportRemoveRequest | AssetReportRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AssetReportRemoveResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.asset_report_api.asset_report_remove(
        AssetReportRemoveRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.asset_report_api.asset_report_remove(
        AssetReportRemoveRequest(asset_report_token="some example string")
    )
    # TODO: Handle 'response' of type AssetReportRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssetReportRemoveRequest](the_plaid_api/models/asset_report_remove_request.py) \| [AssetReportRemoveRequestDict](the_plaid_api/models/asset_report_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AssetReportRemoveResponse](the_plaid_api/models/asset_report_remove_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AuthApi

> Source: [AuthApi](the_plaid_api/apis/auth_api.py)

<details>
<summary><code>def auth_get(body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AuthGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.

Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Also note that `/auth/get` will not return data for any new accounts opened after the Item was created. To obtain data for new accounts, create a new Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auth_api.auth_get(AuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type AuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.auth_api.auth_get(AuthGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type AuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AuthGetRequest](the_plaid_api/models/auth_get_request.py) \| [AuthGetRequestDict](the_plaid_api/models/auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AuthGetResponse](the_plaid_api/models/auth_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## BankTransferApi

> Source: [BankTransferApi](the_plaid_api/apis/bank_transfer_api.py)

<details>
<summary><code>def bank_transfer_balance_get(body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferBalanceGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_balance_get(BankTransferBalanceGetRequest())
    # TODO: Handle 'response' of type BankTransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_balance_get(BankTransferBalanceGetRequest())
    # TODO: Handle 'response' of type BankTransferBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferBalanceGetRequest](the_plaid_api/models/bank_transfer_balance_get_request.py) \| [BankTransferBalanceGetRequestDict](the_plaid_api/models/bank_transfer_balance_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferBalanceGetResponse](the_plaid_api/models/bank_transfer_balance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_cancel(body: BankTransferCancelRequest | BankTransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferCancelResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_cancel(
        BankTransferCancelRequest(bank_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type BankTransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_cancel(
        BankTransferCancelRequest(bank_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type BankTransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferCancelRequest](the_plaid_api/models/bank_transfer_cancel_request.py) \| [BankTransferCancelRequestDict](the_plaid_api/models/bank_transfer_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferCancelResponse](the_plaid_api/models/bank_transfer_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_create(body: BankTransferCreateRequest | BankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_create(
        BankTransferCreateRequest(
            idempotency_key="some example string",
            access_token="some example string",
            account_id="some example string",
            type_=BankTransferType.DEBIT,
            network=BankTransferNetwork.ACH,
            amount="some example string",
            iso_currency_code="some example string",
            description="some example string",
            user=BankTransferUser(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type BankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_create(
        BankTransferCreateRequest(
            idempotency_key="some example string",
            access_token="some example string",
            account_id="some example string",
            type_=BankTransferType.DEBIT,
            network=BankTransferNetwork.ACH,
            amount="some example string",
            iso_currency_code="some example string",
            description="some example string",
            user=BankTransferUser(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type BankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferCreateRequest](the_plaid_api/models/bank_transfer_create_request.py) \| [BankTransferCreateRequestDict](the_plaid_api/models/bank_transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferCreateResponse](the_plaid_api/models/bank_transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_list(body: BankTransferEventListRequest | BankTransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferEventListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/event/list` endpoint to get a list of bank transfer events based on specified filter criteria.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_event_list(BankTransferEventListRequest())
    # TODO: Handle 'response' of type BankTransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_event_list(BankTransferEventListRequest())
    # TODO: Handle 'response' of type BankTransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferEventListRequest](the_plaid_api/models/bank_transfer_event_list_request.py) \| [BankTransferEventListRequestDict](the_plaid_api/models/bank_transfer_event_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferEventListResponse](the_plaid_api/models/bank_transfer_event_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_event_sync(body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferEventSyncResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/bank_transfer/event/sync` allows you to request up to the next 25 bank transfer events that happened after a specific `event_id`. Use the `/bank_transfer/event/sync` endpoint to guarantee you have seen all bank transfer events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type BankTransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_event_sync(BankTransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type BankTransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferEventSyncRequest](the_plaid_api/models/bank_transfer_event_sync_request.py) \| [BankTransferEventSyncRequestDict](the_plaid_api/models/bank_transfer_event_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferEventSyncResponse](the_plaid_api/models/bank_transfer_event_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_get(body: BankTransferGetRequest | BankTransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_get(
        BankTransferGetRequest(bank_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type BankTransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_get(
        BankTransferGetRequest(bank_transfer_id="some example string")
    )
    # TODO: Handle 'response' of type BankTransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferGetRequest](the_plaid_api/models/bank_transfer_get_request.py) \| [BankTransferGetRequestDict](the_plaid_api/models/bank_transfer_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferGetResponse](the_plaid_api/models/bank_transfer_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_list(body: BankTransferListRequest | BankTransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_list(BankTransferListRequest())
    # TODO: Handle 'response' of type BankTransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_list(BankTransferListRequest())
    # TODO: Handle 'response' of type BankTransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferListRequest](the_plaid_api/models/bank_transfer_list_request.py) \| [BankTransferListRequestDict](the_plaid_api/models/bank_transfer_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferListResponse](the_plaid_api/models/bank_transfer_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_migrate_account(body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferMigrateAccountResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_migrate_account(
        BankTransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type BankTransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_migrate_account(
        BankTransferMigrateAccountRequest(
            account_number="some example string",
            routing_number="some example string",
            account_type="some example string",
        ),
    )
    # TODO: Handle 'response' of type BankTransferMigrateAccountResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferMigrateAccountRequest](the_plaid_api/models/bank_transfer_migrate_account_request.py) \| [BankTransferMigrateAccountRequestDict](the_plaid_api/models/bank_transfer_migrate_account_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferMigrateAccountResponse](the_plaid_api/models/bank_transfer_migrate_account_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_get(body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferSweepGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_sweep_get(BankTransferSweepGetRequest(sweep_id=1))
    # TODO: Handle 'response' of type BankTransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_sweep_get(BankTransferSweepGetRequest(sweep_id=1))
    # TODO: Handle 'response' of type BankTransferSweepGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferSweepGetRequest](the_plaid_api/models/bank_transfer_sweep_get_request.py) \| [BankTransferSweepGetRequestDict](the_plaid_api/models/bank_transfer_sweep_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferSweepGetResponse](the_plaid_api/models/bank_transfer_sweep_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_transfer_sweep_list(body: BankTransferSweepListRequest | BankTransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BankTransferSweepListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bank_transfer_api.bank_transfer_sweep_list(BankTransferSweepListRequest())
    # TODO: Handle 'response' of type BankTransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bank_transfer_api.bank_transfer_sweep_list(BankTransferSweepListRequest())
    # TODO: Handle 'response' of type BankTransferSweepListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BankTransferSweepListRequest](the_plaid_api/models/bank_transfer_sweep_list_request.py) \| [BankTransferSweepListRequestDict](the_plaid_api/models/bank_transfer_sweep_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BankTransferSweepListResponse](the_plaid_api/models/bank_transfer_sweep_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Categories

> Source: [Categories](the_plaid_api/apis/categories.py)

<details>
<summary><code>def categories_get(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> CategoriesGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a request to the `/categories/get`  endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.categories_get({})
    # TODO: Handle 'response' of type CategoriesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.categories_get({})
    # TODO: Handle 'response' of type CategoriesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoriesGetResponse](the_plaid_api/models/categories_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DepositSwitch

> Source: [DepositSwitch](the_plaid_api/apis/deposit_switch.py)

<details>
<summary><code>def deposit_switch_alt_create(body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DepositSwitchAltCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.deposit_switch.deposit_switch_alt_create(
        DepositSwitchAltCreateRequest(
            target_account=DepositSwitchTargetAccount(
                account_number="some example string",
                routing_number="some example string",
                account_name="some example string",
                account_subtype=AccountSubtype1.CHECKING,
            ),
            target_user=DepositSwitchTargetUser(
                given_name="some example string",
                family_name="some example string",
                phone="some example string",
                email="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type DepositSwitchAltCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.deposit_switch.deposit_switch_alt_create(
        DepositSwitchAltCreateRequest(
            target_account=DepositSwitchTargetAccount(
                account_number="some example string",
                routing_number="some example string",
                account_name="some example string",
                account_subtype=AccountSubtype1.CHECKING,
            ),
            target_user=DepositSwitchTargetUser(
                given_name="some example string",
                family_name="some example string",
                phone="some example string",
                email="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type DepositSwitchAltCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DepositSwitchAltCreateRequest](the_plaid_api/models/deposit_switch_alt_create_request.py) \| [DepositSwitchAltCreateRequestDict](the_plaid_api/models/deposit_switch_alt_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DepositSwitchAltCreateResponse](the_plaid_api/models/deposit_switch_alt_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_switch_create(body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DepositSwitchCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.deposit_switch.deposit_switch_create(
        DepositSwitchCreateRequest(target_access_token="some example string", target_account_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.deposit_switch.deposit_switch_create(
        DepositSwitchCreateRequest(target_access_token="some example string", target_account_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DepositSwitchCreateRequest](the_plaid_api/models/deposit_switch_create_request.py) \| [DepositSwitchCreateRequestDict](the_plaid_api/models/deposit_switch_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DepositSwitchCreateResponse](the_plaid_api/models/deposit_switch_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_switch_get(body: DepositSwitchGetRequest | DepositSwitchGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DepositSwitchGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.deposit_switch.deposit_switch_get(
        DepositSwitchGetRequest(deposit_switch_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.deposit_switch.deposit_switch_get(
        DepositSwitchGetRequest(deposit_switch_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DepositSwitchGetRequest](the_plaid_api/models/deposit_switch_get_request.py) \| [DepositSwitchGetRequestDict](the_plaid_api/models/deposit_switch_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DepositSwitchGetResponse](the_plaid_api/models/deposit_switch_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deposit_switch_token_create(body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DepositSwitchTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.deposit_switch.deposit_switch_token_create(
        DepositSwitchTokenCreateRequest(deposit_switch_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.deposit_switch.deposit_switch_token_create(
        DepositSwitchTokenCreateRequest(deposit_switch_id="some example string")
    )
    # TODO: Handle 'response' of type DepositSwitchTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DepositSwitchTokenCreateRequest](the_plaid_api/models/deposit_switch_token_create_request.py) \| [DepositSwitchTokenCreateRequestDict](the_plaid_api/models/deposit_switch_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DepositSwitchTokenCreateResponse](the_plaid_api/models/deposit_switch_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Employers

> Source: [Employers](the_plaid_api/apis/employers.py)

<details>
<summary><code>def employers_search(body: EmployersSearchRequest | EmployersSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> EmployersSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.employers.employers_search(
        EmployersSearchRequest(query="some example string", products=["some example string"])
    )
    # TODO: Handle 'response' of type EmployersSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.employers.employers_search(
        EmployersSearchRequest(query="some example string", products=["some example string"])
    )
    # TODO: Handle 'response' of type EmployersSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[EmployersSearchRequest](the_plaid_api/models/employers_search_request.py) \| [EmployersSearchRequestDict](the_plaid_api/models/employers_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[EmployersSearchResponse](the_plaid_api/models/employers_search_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Identity

> Source: [Identity](the_plaid_api/apis/identity.py)

<details>
<summary><code>def identity_get(body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IdentityGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

Note: This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.identity.identity_get(IdentityGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.identity.identity_get(IdentityGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type IdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IdentityGetRequest](the_plaid_api/models/identity_get_request.py) \| [IdentityGetRequestDict](the_plaid_api/models/identity_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IdentityGetResponse](the_plaid_api/models/identity_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Income

> Source: [Income](the_plaid_api/apis/income.py)

<details>
<summary><code>def income_verification_create(body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_create(IncomeVerificationCreateRequest(webhook="some example string"))
    # TODO: Handle 'response' of type IncomeVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_create(
        IncomeVerificationCreateRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type IncomeVerificationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationCreateRequest](the_plaid_api/models/income_verification_create_request.py) \| [IncomeVerificationCreateRequestDict](the_plaid_api/models/income_verification_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationCreateResponse](the_plaid_api/models/income_verification_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_documents_download(body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/documents/download` provides the ability to download the source paystub PDF that the end user uploaded via Paystub Import.

The response to `/income/verification/documents/download` is a ZIP file in binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

For Payroll Income, the most recent file available for download with the payroll provider will also be available from this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.income.income_verification_documents_download(IncomeVerificationDocumentsDownloadRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.income.income_verification_documents_download(IncomeVerificationDocumentsDownloadRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationDocumentsDownloadRequest](the_plaid_api/models/income_verification_documents_download_request.py) \| [IncomeVerificationDocumentsDownloadRequestDict](the_plaid_api/models/income_verification_documents_download_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_paystub_get(body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationPaystubGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

(Deprecated) Retrieve information from a single paystub used for income verification

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_paystub_get(IncomeVerificationPaystubGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_paystub_get(IncomeVerificationPaystubGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationPaystubGetRequest](the_plaid_api/models/income_verification_paystub_get_request.py) \| [IncomeVerificationPaystubGetRequestDict](the_plaid_api/models/income_verification_paystub_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationPaystubGetResponse](the_plaid_api/models/income_verification_paystub_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_paystubs_get(body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationPaystubsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_paystubs_get(IncomeVerificationPaystubsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationPaystubsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationPaystubsGetRequest](the_plaid_api/models/income_verification_paystubs_get_request.py) \| [IncomeVerificationPaystubsGetRequestDict](the_plaid_api/models/income_verification_paystubs_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationPaystubsGetResponse](the_plaid_api/models/income_verification_paystubs_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_precheck(body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationPrecheckResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/precheck` returns whether a given user is supportable by the income product

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_precheck(IncomeVerificationPrecheckRequest())
    # TODO: Handle 'response' of type IncomeVerificationPrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_precheck(IncomeVerificationPrecheckRequest())
    # TODO: Handle 'response' of type IncomeVerificationPrecheckResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationPrecheckRequest](the_plaid_api/models/income_verification_precheck_request.py) \| [IncomeVerificationPrecheckRequestDict](the_plaid_api/models/income_verification_precheck_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationPrecheckResponse](the_plaid_api/models/income_verification_precheck_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_refresh(body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationRefreshResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/refresh` refreshes a given income verification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_refresh(IncomeVerificationRefreshRequest())
    # TODO: Handle 'response' of type IncomeVerificationRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_refresh(IncomeVerificationRefreshRequest())
    # TODO: Handle 'response' of type IncomeVerificationRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationRefreshRequest](the_plaid_api/models/income_verification_refresh_request.py) \| [IncomeVerificationRefreshRequestDict](the_plaid_api/models/income_verification_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationRefreshResponse](the_plaid_api/models/income_verification_refresh_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_summary_get(body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationSummaryGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/summary/get` returns a verification summary for the income that was verified for an end user. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_summary_get(IncomeVerificationSummaryGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationSummaryGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_summary_get(IncomeVerificationSummaryGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationSummaryGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationSummaryGetRequest](the_plaid_api/models/income_verification_summary_get_request.py) \| [IncomeVerificationSummaryGetRequestDict](the_plaid_api/models/income_verification_summary_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationSummaryGetResponse](the_plaid_api/models/income_verification_summary_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def income_verification_taxforms_get(body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IncomeVerificationTaxformsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/income/verification/taxforms/get` returns the information collected from taxforms that were used to verify an end user's. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.income.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationTaxformsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.income.income_verification_taxforms_get(IncomeVerificationTaxformsGetRequest())
    # TODO: Handle 'response' of type IncomeVerificationTaxformsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[IncomeVerificationTaxformsGetRequest](the_plaid_api/models/income_verification_taxforms_get_request.py) \| [IncomeVerificationTaxformsGetRequestDict](the_plaid_api/models/income_verification_taxforms_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[IncomeVerificationTaxformsGetResponse](the_plaid_api/models/income_verification_taxforms_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Institutions

> Source: [Institutions](the_plaid_api/apis/institutions.py)

<details>
<summary><code>def institutions_get(body: InstitutionsGetRequest | InstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.institutions.institutions_get(
        InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions.institutions_get(
        InstitutionsGetRequest(count=1, offset=1, country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsGetRequest](the_plaid_api/models/institutions_get_request.py) \| [InstitutionsGetRequestDict](the_plaid_api/models/institutions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InstitutionsGetResponse](the_plaid_api/models/institutions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_get_by_id(body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsGetByIdResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.institutions.institutions_get_by_id(
        InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetByIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions.institutions_get_by_id(
        InstitutionsGetByIdRequest(institution_id="some example string", country_codes=[CountryCode.US])
    )
    # TODO: Handle 'response' of type InstitutionsGetByIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsGetByIdRequest](the_plaid_api/models/institutions_get_by_id_request.py) \| [InstitutionsGetByIdRequestDict](the_plaid_api/models/institutions_get_by_id_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InstitutionsGetByIdResponse](the_plaid_api/models/institutions_get_by_id_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutions_search(body: InstitutionsSearchRequest | InstitutionsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InstitutionsSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.institutions.institutions_search(
        InstitutionsSearchRequest(
            query="some example string", products=[Products.ASSETS], country_codes=[CountryCode.US]
        ),
    )
    # TODO: Handle 'response' of type InstitutionsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.institutions.institutions_search(
        InstitutionsSearchRequest(
            query="some example string", products=[Products.ASSETS], country_codes=[CountryCode.US]
        ),
    )
    # TODO: Handle 'response' of type InstitutionsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InstitutionsSearchRequest](the_plaid_api/models/institutions_search_request.py) \| [InstitutionsSearchRequestDict](the_plaid_api/models/institutions_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InstitutionsSearchResponse](the_plaid_api/models/institutions_search_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Investments

> Source: [Investments](the_plaid_api/apis/investments.py)

<details>
<summary><code>def investments_holdings_get(body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsHoldingsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.investments.investments_holdings_get(
        InvestmentsHoldingsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type InvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments.investments_holdings_get(
        InvestmentsHoldingsGetRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type InvestmentsHoldingsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsHoldingsGetRequest](the_plaid_api/models/investments_holdings_get_request.py) \| [InvestmentsHoldingsGetRequestDict](the_plaid_api/models/investments_holdings_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvestmentsHoldingsGetResponse](the_plaid_api/models/investments_holdings_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investments_transactions_get(body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InvestmentsTransactionsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/investments/transactions/get` endpoint allows developers to retrieve user-authorized transaction data for investment accounts.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.investments.investments_transactions_get(
        InvestmentsTransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type InvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.investments.investments_transactions_get(
        InvestmentsTransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type InvestmentsTransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InvestmentsTransactionsGetRequest](the_plaid_api/models/investments_transactions_get_request.py) \| [InvestmentsTransactionsGetRequestDict](the_plaid_api/models/investments_transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvestmentsTransactionsGetResponse](the_plaid_api/models/investments_transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ItemApi

> Source: [ItemApi](the_plaid_api/apis/item_api.py)

<details>
<summary><code>def item_access_token_invalidate(body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemAccessTokenInvalidateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_access_token_invalidate(
        ItemAccessTokenInvalidateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemAccessTokenInvalidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_access_token_invalidate(
        ItemAccessTokenInvalidateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemAccessTokenInvalidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemAccessTokenInvalidateRequest](the_plaid_api/models/item_access_token_invalidate_request.py) \| [ItemAccessTokenInvalidateRequestDict](the_plaid_api/models/item_access_token_invalidate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemAccessTokenInvalidateResponse](the_plaid_api/models/item_access_token_invalidate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_list(body: ItemApplicationListRequest | ItemApplicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemApplicationListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List a user’s connected applications

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_application_list(ItemApplicationListRequest())
    # TODO: Handle 'response' of type ItemApplicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_application_list(ItemApplicationListRequest())
    # TODO: Handle 'response' of type ItemApplicationListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemApplicationListRequest](the_plaid_api/models/item_application_list_request.py) \| [ItemApplicationListRequestDict](the_plaid_api/models/item_application_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemApplicationListResponse](the_plaid_api/models/item_application_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_application_scopes_update(body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemApplicationScopesUpdateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable consumers to update product access on selected accounts for an application.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_application_scopes_update(
        ItemApplicationScopesUpdateRequest(
            access_token="some example string",
            application_id="some example string",
            scopes=Scopes(),
            context=ScopesContext.ENROLLMENT,
        ),
    )
    # TODO: Handle 'response' of type ItemApplicationScopesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_application_scopes_update(
        ItemApplicationScopesUpdateRequest(
            access_token="some example string",
            application_id="some example string",
            scopes=Scopes(),
            context=ScopesContext.ENROLLMENT,
        ),
    )
    # TODO: Handle 'response' of type ItemApplicationScopesUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemApplicationScopesUpdateRequest](the_plaid_api/models/item_application_scopes_update_request.py) \| [ItemApplicationScopesUpdateRequestDict](the_plaid_api/models/item_application_scopes_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemApplicationScopesUpdateResponse](the_plaid_api/models/item_application_scopes_update_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_create_public_token(body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemPublicTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_create_public_token(
        ItemPublicTokenCreateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_create_public_token(
        ItemPublicTokenCreateRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemPublicTokenCreateRequest](the_plaid_api/models/item_public_token_create_request.py) \| [ItemPublicTokenCreateRequestDict](the_plaid_api/models/item_public_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemPublicTokenCreateResponse](the_plaid_api/models/item_public_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_get(body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about the status of an Item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_get(ItemGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_get(ItemGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemGetRequest](the_plaid_api/models/item_get_request.py) \| [ItemGetRequestDict](the_plaid_api/models/item_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemGetResponse](the_plaid_api/models/item_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_import(body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemImportResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (`target_account_id`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_import(
        ItemImportRequest(
            products=[Products.ASSETS],
            user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ItemImportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_import(
        ItemImportRequest(
            products=[Products.ASSETS],
            user_auth=ItemImportRequestUserAuth(user_id="some example string", auth_token="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ItemImportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemImportRequest](the_plaid_api/models/item_import_request.py) \| [ItemImportRequestDict](the_plaid_api/models/item_import_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemImportResponse](the_plaid_api/models/item_import_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_public_token_exchange(body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemPublicTokenExchangeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes.

The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_public_token_exchange(
        ItemPublicTokenExchangeRequest(public_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_public_token_exchange(
        ItemPublicTokenExchangeRequest(public_token="some example string")
    )
    # TODO: Handle 'response' of type ItemPublicTokenExchangeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemPublicTokenExchangeRequest](the_plaid_api/models/item_public_token_exchange_request.py) \| [ItemPublicTokenExchangeRequestDict](the_plaid_api/models/item_public_token_exchange_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemPublicTokenExchangeResponse](the_plaid_api/models/item_public_token_exchange_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_remove(body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemRemoveResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/item/remove`  endpoint allows you to remove an Item. Once removed, the `access_token`  associated with the Item is no longer valid and cannot be used to access any data that was associated with the Item.

Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.

Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_remove(ItemRemoveRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_remove(ItemRemoveRequest(access_token="some example string"))
    # TODO: Handle 'response' of type ItemRemoveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemRemoveRequest](the_plaid_api/models/item_remove_request.py) \| [ItemRemoveRequestDict](the_plaid_api/models/item_remove_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemRemoveResponse](the_plaid_api/models/item_remove_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def item_webhook_update(body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ItemWebhookUpdateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a https://plaid.com/docs/api/webhooks/#item-webhook-url-updated webhook to the newly specified webhook URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.item_api.item_webhook_update(
        ItemWebhookUpdateRequest(access_token="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type ItemWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.item_api.item_webhook_update(
        ItemWebhookUpdateRequest(access_token="some example string", webhook="some example string")
    )
    # TODO: Handle 'response' of type ItemWebhookUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ItemWebhookUpdateRequest](the_plaid_api/models/item_webhook_update_request.py) \| [ItemWebhookUpdateRequestDict](the_plaid_api/models/item_webhook_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemWebhookUpdateResponse](the_plaid_api/models/item_webhook_update_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Liabilities

> Source: [Liabilities](the_plaid_api/apis/liabilities.py)

<details>
<summary><code>def liabilities_get(body: LiabilitiesGetRequest | LiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LiabilitiesGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.liabilities.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type LiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.liabilities.liabilities_get(LiabilitiesGetRequest(access_token="some example string"))
    # TODO: Handle 'response' of type LiabilitiesGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LiabilitiesGetRequest](the_plaid_api/models/liabilities_get_request.py) \| [LiabilitiesGetRequestDict](the_plaid_api/models/liabilities_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LiabilitiesGetResponse](the_plaid_api/models/liabilities_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Link

> Source: [Link](the_plaid_api/apis/link.py)

<details>
<summary><code>def link_token_create(body: LinkTokenCreateRequest | LinkTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.

A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.link.link_token_create(
        LinkTokenCreateRequest(
            client_name="some example string",
            language="some example string",
            country_codes=[CountryCode.US],
            user=LinkTokenCreateRequestUser(client_user_id="some example string"),
        ),
    )
    # TODO: Handle 'response' of type LinkTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link.link_token_create(
        LinkTokenCreateRequest(
            client_name="some example string",
            language="some example string",
            country_codes=[CountryCode.US],
            user=LinkTokenCreateRequestUser(client_user_id="some example string"),
        ),
    )
    # TODO: Handle 'response' of type LinkTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkTokenCreateRequest](the_plaid_api/models/link_token_create_request.py) \| [LinkTokenCreateRequestDict](the_plaid_api/models/link_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LinkTokenCreateResponse](the_plaid_api/models/link_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_token_get(body: LinkTokenGetRequest | LinkTokenGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> LinkTokenGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
`/link/token/create` endpoint. It can be useful for debugging purposes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.link.link_token_get(LinkTokenGetRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkTokenGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.link.link_token_get(LinkTokenGetRequest(link_token="some example string"))
    # TODO: Handle 'response' of type LinkTokenGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LinkTokenGetRequest](the_plaid_api/models/link_token_get_request.py) \| [LinkTokenGetRequestDict](the_plaid_api/models/link_token_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LinkTokenGetResponse](the_plaid_api/models/link_token_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## PaymentInitiation

> Source: [PaymentInitiation](the_plaid_api/apis/payment_initiation.py)

<details>
<summary><code>def create_payment_token(body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.create_payment_token(
        PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.create_payment_token(
        PaymentInitiationPaymentTokenCreateRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentTokenCreateRequest](the_plaid_api/models/payment_initiation_payment_token_create_request.py) \| [PaymentInitiationPaymentTokenCreateRequestDict](the_plaid_api/models/payment_initiation_payment_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationPaymentTokenCreateResponse](the_plaid_api/models/payment_initiation_payment_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_create(body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR or GBP.  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer and GBP-denominated payments will be sent via the Faster Payments network, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer will typically arrive in one business day.

Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

In the Development environment, payments must be below 5 GBP / EUR. For details on any payment limits in Production, contact your Plaid Account Manager.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_payment_create(
        PaymentInitiationPaymentCreateRequest(
            recipient_id="some example string",
            reference="some example string",
            amount=PaymentAmount(currency=Currency.GBP, value=1.5),
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_payment_create(
        PaymentInitiationPaymentCreateRequest(
            recipient_id="some example string",
            reference="some example string",
            amount=PaymentAmount(currency=Currency.GBP, value=1.5),
        ),
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentCreateRequest](the_plaid_api/models/payment_initiation_payment_create_request.py) \| [PaymentInitiationPaymentCreateRequestDict](the_plaid_api/models/payment_initiation_payment_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationPaymentCreateResponse](the_plaid_api/models/payment_initiation_payment_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_get(body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_payment_get(
        PaymentInitiationPaymentGetRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_payment_get(
        PaymentInitiationPaymentGetRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentGetRequest](the_plaid_api/models/payment_initiation_payment_get_request.py) \| [PaymentInitiationPaymentGetRequestDict](the_plaid_api/models/payment_initiation_payment_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationPaymentGetResponse](the_plaid_api/models/payment_initiation_payment_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_list(body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_payment_list(PaymentInitiationPaymentListRequest())
    # TODO: Handle 'response' of type PaymentInitiationPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_payment_list(
        PaymentInitiationPaymentListRequest()
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentListRequest](the_plaid_api/models/payment_initiation_payment_list_request.py) \| [PaymentInitiationPaymentListRequestDict](the_plaid_api/models/payment_initiation_payment_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationPaymentListResponse](the_plaid_api/models/payment_initiation_payment_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_payment_reverse(body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationPaymentReverseResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reverse a previously initiated payment.

A payment can only be reversed once and will be refunded to the original sender's account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_payment_reverse(
        PaymentInitiationPaymentReverseRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentReverseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_payment_reverse(
        PaymentInitiationPaymentReverseRequest(payment_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationPaymentReverseResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationPaymentReverseRequest](the_plaid_api/models/payment_initiation_payment_reverse_request.py) \| [PaymentInitiationPaymentReverseRequestDict](the_plaid_api/models/payment_initiation_payment_reverse_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationPaymentReverseResponse](the_plaid_api/models/payment_initiation_payment_reverse_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_create(body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA).  For a standing order (recurring) payment, the recipient must be in the UK.

The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_recipient_create(
        PaymentInitiationRecipientCreateRequest(name="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_recipient_create(
        PaymentInitiationRecipientCreateRequest(name="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientCreateRequest](the_plaid_api/models/payment_initiation_recipient_create_request.py) \| [PaymentInitiationRecipientCreateRequestDict](the_plaid_api/models/payment_initiation_recipient_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationRecipientCreateResponse](the_plaid_api/models/payment_initiation_recipient_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_get(body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get details about a payment recipient you have previously created.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_recipient_get(
        PaymentInitiationRecipientGetRequest(recipient_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_recipient_get(
        PaymentInitiationRecipientGetRequest(recipient_id="some example string")
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientGetRequest](the_plaid_api/models/payment_initiation_recipient_get_request.py) \| [PaymentInitiationRecipientGetRequestDict](the_plaid_api/models/payment_initiation_recipient_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationRecipientGetResponse](the_plaid_api/models/payment_initiation_recipient_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def payment_initiation_recipient_list(body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PaymentInitiationRecipientListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payment_initiation.payment_initiation_recipient_list(PaymentInitiationRecipientListRequest())
    # TODO: Handle 'response' of type PaymentInitiationRecipientListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.payment_initiation.payment_initiation_recipient_list(
        PaymentInitiationRecipientListRequest()
    )
    # TODO: Handle 'response' of type PaymentInitiationRecipientListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PaymentInitiationRecipientListRequest](the_plaid_api/models/payment_initiation_recipient_list_request.py) \| [PaymentInitiationRecipientListRequestDict](the_plaid_api/models/payment_initiation_recipient_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PaymentInitiationRecipientListResponse](the_plaid_api/models/payment_initiation_recipient_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ProcessorApi

> Source: [ProcessorApi](the_plaid_api/apis/processor_api.py)

<details>
<summary><code>def processor_apex_processor_token_create(body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_apex_processor_token_create(
        ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_apex_processor_token_create(
        ProcessorApexProcessorTokenCreateRequest(access_token="some example string", account_id="some example string")
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorApexProcessorTokenCreateRequest](the_plaid_api/models/processor_apex_processor_token_create_request.py) \| [ProcessorApexProcessorTokenCreateRequestDict](the_plaid_api/models/processor_apex_processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_auth_get(body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorAuthGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that's associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_auth_get(ProcessorAuthGetRequest(processor_token="some example string"))
    # TODO: Handle 'response' of type ProcessorAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_auth_get(
        ProcessorAuthGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorAuthGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorAuthGetRequest](the_plaid_api/models/processor_auth_get_request.py) \| [ProcessorAuthGetRequestDict](the_plaid_api/models/processor_auth_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorAuthGetResponse](the_plaid_api/models/processor_auth_get_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_balance_get(body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorBalanceGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_balance_get(
        ProcessorBalanceGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_balance_get(
        ProcessorBalanceGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorBalanceGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorBalanceGetRequest](the_plaid_api/models/processor_balance_get_request.py) \| [ProcessorBalanceGetRequestDict](the_plaid_api/models/processor_balance_get_request.py)</code> | The `/processor/balance/get` endpoint returns the real-time balance for the account associated with a given `processor_token`.<br><br>The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.<br><br>Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of `null`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorBalanceGetResponse](the_plaid_api/models/processor_balance_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_bank_transfer_create(body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorBankTransferCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_bank_transfer_create(
        ProcessorBankTransferCreateRequest(
            idempotency_key="some example string",
            processor_token="some example string",
            type_=BankTransferType.DEBIT,
            network=BankTransferNetwork.ACH,
            amount="some example string",
            iso_currency_code="some example string",
            description="some example string",
            user=BankTransferUser(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ProcessorBankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_bank_transfer_create(
        ProcessorBankTransferCreateRequest(
            idempotency_key="some example string",
            processor_token="some example string",
            type_=BankTransferType.DEBIT,
            network=BankTransferNetwork.ACH,
            amount="some example string",
            iso_currency_code="some example string",
            description="some example string",
            user=BankTransferUser(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type ProcessorBankTransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorBankTransferCreateRequest](the_plaid_api/models/processor_bank_transfer_create_request.py) \| [ProcessorBankTransferCreateRequestDict](the_plaid_api/models/processor_bank_transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorBankTransferCreateResponse](the_plaid_api/models/processor_bank_transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_identity_get(body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorIdentityGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_identity_get(
        ProcessorIdentityGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorIdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_identity_get(
        ProcessorIdentityGetRequest(processor_token="some example string")
    )
    # TODO: Handle 'response' of type ProcessorIdentityGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorIdentityGetRequest](the_plaid_api/models/processor_identity_get_request.py) \| [ProcessorIdentityGetRequestDict](the_plaid_api/models/processor_identity_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorIdentityGetResponse](the_plaid_api/models/processor_identity_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_stripe_bank_account_token_create(body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorStripeBankAccountTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_stripe_bank_account_token_create(
        ProcessorStripeBankAccountTokenCreateRequest(
            access_token="some example string", account_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ProcessorStripeBankAccountTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_stripe_bank_account_token_create(
        ProcessorStripeBankAccountTokenCreateRequest(
            access_token="some example string", account_id="some example string"
        ),
    )
    # TODO: Handle 'response' of type ProcessorStripeBankAccountTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorStripeBankAccountTokenCreateRequest](the_plaid_api/models/processor_stripe_bank_account_token_create_request.py) \| [ProcessorStripeBankAccountTokenCreateRequestDict](the_plaid_api/models/processor_stripe_bank_account_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorStripeBankAccountTokenCreateResponse](the_plaid_api/models/processor_stripe_bank_account_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def processor_token_create(body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ProcessorTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.processor_api.processor_token_create(
        ProcessorTokenCreateRequest(
            access_token="some example string", account_id="some example string", processor=Processor.ACHQ
        ),
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.processor_api.processor_token_create(
        ProcessorTokenCreateRequest(
            access_token="some example string", account_id="some example string", processor=Processor.ACHQ
        ),
    )
    # TODO: Handle 'response' of type ProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProcessorTokenCreateRequest](the_plaid_api/models/processor_token_create_request.py) \| [ProcessorTokenCreateRequestDict](the_plaid_api/models/processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProcessorTokenCreateResponse](the_plaid_api/models/processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Sandbox

> Source: [Sandbox](the_plaid_api/apis/sandbox.py)

<details>
<summary><code>def sandbox_bank_transfer_fire_webhook(body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxBankTransferFireWebhookResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_bank_transfer_fire_webhook(
        SandboxBankTransferFireWebhookRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_bank_transfer_fire_webhook(
        SandboxBankTransferFireWebhookRequest(webhook="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxBankTransferFireWebhookRequest](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py) \| [SandboxBankTransferFireWebhookRequestDict](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxBankTransferFireWebhookResponse](the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_bank_transfer_simulate(body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxBankTransferSimulateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_bank_transfer_simulate(
        SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_bank_transfer_simulate(
        SandboxBankTransferSimulateRequest(bank_transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxBankTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxBankTransferSimulateRequest](the_plaid_api/models/sandbox_bank_transfer_simulate_request.py) \| [SandboxBankTransferSimulateRequestDict](the_plaid_api/models/sandbox_bank_transfer_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxBankTransferSimulateResponse](the_plaid_api/models/sandbox_bank_transfer_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_income_fire_webhook(body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxIncomeFireWebhookResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger an Income webhook in the Sandbox environment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_income_fire_webhook(
        SandboxIncomeFireWebhookRequest(
            income_verification_id="some example string",
            webhook="some example string",
            verification_status=VerificationStatus3.VERIFICATION_STATUS_PROCESSING_COMPLETE,
        ),
    )
    # TODO: Handle 'response' of type SandboxIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_income_fire_webhook(
        SandboxIncomeFireWebhookRequest(
            income_verification_id="some example string",
            webhook="some example string",
            verification_status=VerificationStatus3.VERIFICATION_STATUS_PROCESSING_COMPLETE,
        ),
    )
    # TODO: Handle 'response' of type SandboxIncomeFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxIncomeFireWebhookRequest](the_plaid_api/models/sandbox_income_fire_webhook_request.py) \| [SandboxIncomeFireWebhookRequestDict](the_plaid_api/models/sandbox_income_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxIncomeFireWebhookResponse](the_plaid_api/models/sandbox_income_fire_webhook_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_fire_webhook(body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemFireWebhookResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. Calling this endpoint triggers a Transactions `DEFAULT_UPDATE` webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_item_fire_webhook(
        SandboxItemFireWebhookRequest(access_token="some example string", webhook_code="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_item_fire_webhook(
        SandboxItemFireWebhookRequest(access_token="some example string", webhook_code="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemFireWebhookResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemFireWebhookRequest](the_plaid_api/models/sandbox_item_fire_webhook_request.py) \| [SandboxItemFireWebhookRequestDict](the_plaid_api/models/sandbox_item_fire_webhook_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxItemFireWebhookResponse](the_plaid_api/models/sandbox_item_fire_webhook_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_reset_login(body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemResetLoginResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.

In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_item_reset_login(SandboxItemResetLoginRequest(access_token="some example string"))
    # TODO: Handle 'response' of type SandboxItemResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_item_reset_login(
        SandboxItemResetLoginRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type SandboxItemResetLoginResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemResetLoginRequest](the_plaid_api/models/sandbox_item_reset_login_request.py) \| [SandboxItemResetLoginRequestDict](the_plaid_api/models/sandbox_item_reset_login_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxItemResetLoginResponse](the_plaid_api/models/sandbox_item_reset_login_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_item_set_verification_status(body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxItemSetVerificationStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_item_set_verification_status(
        SandboxItemSetVerificationStatusRequest(
            access_token="some example string",
            account_id="some example string",
            verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
        ),
    )
    # TODO: Handle 'response' of type SandboxItemSetVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_item_set_verification_status(
        SandboxItemSetVerificationStatusRequest(
            access_token="some example string",
            account_id="some example string",
            verification_status=VerificationStatus1.AUTOMATICALLY_VERIFIED,
        ),
    )
    # TODO: Handle 'response' of type SandboxItemSetVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxItemSetVerificationStatusRequest](the_plaid_api/models/sandbox_item_set_verification_status_request.py) \| [SandboxItemSetVerificationStatusRequestDict](the_plaid_api/models/sandbox_item_set_verification_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxItemSetVerificationStatusResponse](the_plaid_api/models/sandbox_item_set_verification_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_oauth_select_accounts(body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Save the selected accounts when connecting to the Platypus Oauth institution

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_oauth_select_accounts(
        SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_oauth_select_accounts(
        SandboxOauthSelectAccountsRequest(oauth_state_id="some example string", accounts=["some example string"])
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxOauthSelectAccountsRequest](the_plaid_api/models/sandbox_oauth_select_accounts_request.py) \| [SandboxOauthSelectAccountsRequestDict](the_plaid_api/models/sandbox_oauth_select_accounts_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_processor_token_create(body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxProcessorTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_processor_token_create(
        SandboxProcessorTokenCreateRequest(institution_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_processor_token_create(
        SandboxProcessorTokenCreateRequest(institution_id="some example string")
    )
    # TODO: Handle 'response' of type SandboxProcessorTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxProcessorTokenCreateRequest](the_plaid_api/models/sandbox_processor_token_create_request.py) \| [SandboxProcessorTokenCreateRequestDict](the_plaid_api/models/sandbox_processor_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxProcessorTokenCreateResponse](the_plaid_api/models/sandbox_processor_token_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_public_token_create(body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxPublicTokenCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/public_token/create`  endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the https://plaid.com/docs/sandbox/user-custom to generate a test account with custom data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_public_token_create(
        SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type SandboxPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_public_token_create(
        SandboxPublicTokenCreateRequest(institution_id="some example string", initial_products=[Products.ASSETS])
    )
    # TODO: Handle 'response' of type SandboxPublicTokenCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxPublicTokenCreateRequest](the_plaid_api/models/sandbox_public_token_create_request.py) \| [SandboxPublicTokenCreateRequestDict](the_plaid_api/models/sandbox_public_token_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxPublicTokenCreateResponse](the_plaid_api/models/sandbox_public_token_create_response.py)</code> -- success

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sandbox_transfer_simulate(body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SandboxTransferSimulateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sandbox.sandbox_transfer_simulate(
        SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.sandbox.sandbox_transfer_simulate(
        SandboxTransferSimulateRequest(transfer_id="some example string", event_type="some example string")
    )
    # TODO: Handle 'response' of type SandboxTransferSimulateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SandboxTransferSimulateRequest](the_plaid_api/models/sandbox_transfer_simulate_request.py) \| [SandboxTransferSimulateRequestDict](the_plaid_api/models/sandbox_transfer_simulate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SandboxTransferSimulateResponse](the_plaid_api/models/sandbox_transfer_simulate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Signal

> Source: [Signal](the_plaid_api/apis/signal.py)

<details>
<summary><code>def signal_decision_report(body: SignalDecisionReportRequest | SignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalDecisionReportResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an `INVALID_REQUEST` error if called a second time with a different value for `initiated`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.signal.signal_decision_report(
        SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
    )
    # TODO: Handle 'response' of type SignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal.signal_decision_report(
        SignalDecisionReportRequest(client_transaction_id="some example string", initiated=True)
    )
    # TODO: Handle 'response' of type SignalDecisionReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalDecisionReportRequest](the_plaid_api/models/signal_decision_report_request.py) \| [SignalDecisionReportRequestDict](the_plaid_api/models/signal_decision_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SignalDecisionReportResponse](the_plaid_api/models/signal_decision_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_evaluate(body: SignalEvaluateRequest | SignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalEvaluateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.signal.signal_evaluate(
        SignalEvaluateRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal.signal_evaluate(
        SignalEvaluateRequest(
            access_token="some example string",
            account_id="some example string",
            client_transaction_id="some example string",
            amount=1.5,
        ),
    )
    # TODO: Handle 'response' of type SignalEvaluateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalEvaluateRequest](the_plaid_api/models/signal_evaluate_request.py) \| [SignalEvaluateRequestDict](the_plaid_api/models/signal_evaluate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SignalEvaluateResponse](the_plaid_api/models/signal_evaluate_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def signal_return_report(body: SignalReturnReportRequest | SignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SignalReturnReportResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.signal.signal_return_report(
        SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
    )
    # TODO: Handle 'response' of type SignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.signal.signal_return_report(
        SignalReturnReportRequest(client_transaction_id="some example string", return_code="some example string")
    )
    # TODO: Handle 'response' of type SignalReturnReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SignalReturnReportRequest](the_plaid_api/models/signal_return_report_request.py) \| [SignalReturnReportRequestDict](the_plaid_api/models/signal_return_report_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SignalReturnReportResponse](the_plaid_api/models/signal_return_report_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Transactions

> Source: [Transactions](the_plaid_api/apis/transactions.py)

<details>
<summary><code>def transactions_get(body: TransactionsGetRequest | TransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products#investments) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the https://plaid.com/docs/api/webhooks#transactions-initial_update and https://plaid.com/docs/api/webhooks#transactions-historical_update webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transactions.transactions_get(
        TransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type TransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions.transactions_get(
        TransactionsGetRequest(
            access_token="some example string", start_date=date(2024, 1, 15), end_date=date(2024, 1, 15)
        ),
    )
    # TODO: Handle 'response' of type TransactionsGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsGetRequest](the_plaid_api/models/transactions_get_request.py) \| [TransactionsGetRequestDict](the_plaid_api/models/transactions_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransactionsGetResponse](the_plaid_api/models/transactions_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transactions_refresh(body: TransactionsRefreshRequest | TransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransactionsRefreshResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: https://plaid.com/docs/api/webhooks#deleted-transactions-detected will be fired if any removed transactions are detected, and https://plaid.com/docs/api/webhooks#transactions-default_update will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get`.

Access to `/transactions/refresh` in Production is specific to certain pricing plans. If you cannot access `/transactions/refresh` in Production, [contact Sales](https://www.plaid.com/contact) for assistance.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transactions.transactions_refresh(TransactionsRefreshRequest(access_token="some example string"))
    # TODO: Handle 'response' of type TransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transactions.transactions_refresh(
        TransactionsRefreshRequest(access_token="some example string")
    )
    # TODO: Handle 'response' of type TransactionsRefreshResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransactionsRefreshRequest](the_plaid_api/models/transactions_refresh_request.py) \| [TransactionsRefreshRequestDict](the_plaid_api/models/transactions_refresh_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransactionsRefreshResponse](the_plaid_api/models/transactions_refresh_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## TransferApi

> Source: [TransferApi](the_plaid_api/apis/transfer_api.py)

<details>
<summary><code>def transfer_authorization_create(body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferAuthorizationCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

In Plaid's sandbox environment the decisions will be returned as follows:

  - To approve a transfer, make an authorization request with an `amount` less than the available balance in the account.

  - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

  - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

  - To permit a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

  - To permit a transfer with the rationale code `LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

All username/password combinations other than the ones listed above will result in a decision of permitted and rationale code `ERROR`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_authorization_create(
        TransferAuthorizationCreateRequest(
            access_token="some example string",
            account_id="some example string",
            type_=TransferType1.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            ach_class=Achclass.ARC,
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferAuthorizationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_authorization_create(
        TransferAuthorizationCreateRequest(
            access_token="some example string",
            account_id="some example string",
            type_=TransferType1.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            ach_class=Achclass.ARC,
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferAuthorizationCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferAuthorizationCreateRequest](the_plaid_api/models/transfer_authorization_create_request.py) \| [TransferAuthorizationCreateRequestDict](the_plaid_api/models/transfer_authorization_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferAuthorizationCreateResponse](the_plaid_api/models/transfer_authorization_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_cancel(body: TransferCancelRequest | TransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferCancelResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/transfer/get` is `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_cancel(TransferCancelRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferCancelRequest](the_plaid_api/models/transfer_cancel_request.py) \| [TransferCancelRequestDict](the_plaid_api/models/transfer_cancel_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferCancelResponse](the_plaid_api/models/transfer_cancel_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_create(body: TransferCreateRequest | TransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferCreateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/create` endpoint to initiate a new transfer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_create(
        TransferCreateRequest(
            idempotency_key="some example string",
            access_token="some example string",
            account_id="some example string",
            authorization_id="some example string",
            type_=TransferType1.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            description="some example string",
            ach_class=Achclass.ARC,
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_create(
        TransferCreateRequest(
            idempotency_key="some example string",
            access_token="some example string",
            account_id="some example string",
            authorization_id="some example string",
            type_=TransferType1.DEBIT,
            network=TransferNetwork.ACH,
            amount="some example string",
            description="some example string",
            ach_class=Achclass.ARC,
            user=TransferUserInRequest(legal_name="some example string"),
        ),
    )
    # TODO: Handle 'response' of type TransferCreateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferCreateRequest](the_plaid_api/models/transfer_create_request.py) \| [TransferCreateRequestDict](the_plaid_api/models/transfer_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferCreateResponse](the_plaid_api/models/transfer_create_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_list(body: TransferEventListRequest | TransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferEventListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_event_list(TransferEventListRequest())
    # TODO: Handle 'response' of type TransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_event_list(TransferEventListRequest())
    # TODO: Handle 'response' of type TransferEventListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferEventListRequest](the_plaid_api/models/transfer_event_list_request.py) \| [TransferEventListRequestDict](the_plaid_api/models/transfer_event_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferEventListResponse](the_plaid_api/models/transfer_event_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_event_sync(body: TransferEventSyncRequest | TransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferEventSyncResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

`/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_event_sync(TransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type TransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_event_sync(TransferEventSyncRequest(after_id=1))
    # TODO: Handle 'response' of type TransferEventSyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferEventSyncRequest](the_plaid_api/models/transfer_event_sync_request.py) \| [TransferEventSyncRequestDict](the_plaid_api/models/transfer_event_sync_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferEventSyncResponse](the_plaid_api/models/transfer_event_sync_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_get(body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The `/transfer/get` fetches information about the transfer corresponding to the given `transfer_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_get(TransferGetRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_get(TransferGetRequest(transfer_id="some example string"))
    # TODO: Handle 'response' of type TransferGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferGetRequest](the_plaid_api/models/transfer_get_request.py) \| [TransferGetRequestDict](the_plaid_api/models/transfer_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferGetResponse](the_plaid_api/models/transfer_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transfer_list(body: TransferListRequest | TransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TransferListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.transfer_api.transfer_list(TransferListRequest())
    # TODO: Handle 'response' of type TransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.transfer_api.transfer_list(TransferListRequest())
    # TODO: Handle 'response' of type TransferListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TransferListRequest](the_plaid_api/models/transfer_list_request.py) \| [TransferListRequestDict](the_plaid_api/models/transfer_list_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransferListResponse](the_plaid_api/models/transfer_list_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## WebhookVerificationKey

> Source: [WebhookVerificationKey](the_plaid_api/apis/webhook_verification_key.py)

<details>
<summary><code>def webhook_verification_key_get(body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WebhookVerificationKeyGetResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.webhook_verification_key.webhook_verification_key_get(
        WebhookVerificationKeyGetRequest(key_id="some example string")
    )
    # TODO: Handle 'response' of type WebhookVerificationKeyGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.webhook_verification_key.webhook_verification_key_get(
        WebhookVerificationKeyGetRequest(key_id="some example string")
    )
    # TODO: Handle 'response' of type WebhookVerificationKeyGetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[WebhookVerificationKeyGetRequest](the_plaid_api/models/webhook_verification_key_get_request.py) \| [WebhookVerificationKeyGetRequestDict](the_plaid_api/models/webhook_verification_key_get_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_plaid_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[WebhookVerificationKeyGetResponse](the_plaid_api/models/webhook_verification_key_get_response.py)</code> -- OK

**OnError**: <code>[ApiError](the_plaid_api/core/exceptions.py)&#91;[RawError](the_plaid_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

