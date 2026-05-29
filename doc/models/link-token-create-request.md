
# Link Token Create Request

LinkTokenCreateRequest defines the request schema for `/link/token/create`

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `client_name` | `str` | Required | The name of your application, as it should be displayed in Link. Maximum length of 30 characters. |
| `language` | `str` | Required | The language that Link should be displayed in.<br><br>Supported languages are:<br><br>- English (`'en'`)<br>- French (`'fr'`)<br>- Spanish (`'es'`)<br>- Dutch (`'nl'`)<br><br>When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied. |
| `country_codes` | [`List[CountryCode]`](../../doc/models/country-code.md) | Required | Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown.  Supported country codes are: `US`, `CA`, `ES`, `FR`, `GB`, `IE`, `NL`.<br><br>If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. To gain access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.<br><br>If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`. If both `country_codes` and a Link customization are used, the value in `country_codes` may override the value in the customization.<br><br>If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.<br><br>**Constraints**: *Minimum Items*: `1` |
| `user` | [`LinkTokenCreateRequestUser`](../../doc/models/link-token-create-request-user.md) | Required | An object specifying information about the end user who will be linking their account. |
| `products` | [`List[Products]`](../../doc/models/products.md) | Optional | List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted; required otherwise. Valid products are:<br><br>`transactions`, `auth`, `identity`, `assets`, `investments`, `liabilities`, `payment_initiation`, `deposit_switch`, `income_verification`, `transfer`<br><br>`balance` is *not* a valid value, the Balance product does not require explicit initalization and will automatically be initialized when any other product is initialized.<br><br>Only institutions that support *all* requested products will be shown in Link; to maximize the number of institutions listed, it is recommended to initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](https://plaid.com/docs/link/best-practices/#choosing-when-to-initialize-products).<br><br>Note that, unless you have opted to disable Instant Match support, institutions that support Instant Match will also be shown in Link if `auth` is specified as a product, even though these institutions do not contain `auth` in their product array.<br><br>In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`. |
| `webhook` | `str` | Optional | The destination URL to which any webhooks should be sent. |
| `access_token` | `str` | Optional | The `access_token` associated with the Item to update, used when updating or modifying an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link as part of the Payment Initiation (UK and Europe) flow. |
| `link_customization_name` | `str` | Optional | The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`. |
| `redirect_uri` | `str` | Optional | A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. When used in Production or Development, must be an https URI. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. If `android_package_name` is specified, this field should be left blank.  Note that any redirect URI must also be added to the Allowed redirect URIs list in the [developer dashboard](https://dashboard.plaid.com/team/api). |
| `android_package_name` | `str` | Optional | The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. When creating a `link_token` for initializing Link on other platforms, this field must be left blank. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). |
| `account_filters` | [`LinkTokenAccountFilters`](../../doc/models/link-token-account-filters.md) | Optional | By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `"all"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#accounts-schema).<br><br>For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window. |
| `eu_config` | [`LinkTokenEuConfig`](../../doc/models/link-token-eu-config.md) | Optional | Configuration parameters for EU flows |
| `institution_id` | `str` | Optional | Used for certain Europe-only configurations, as well as certain legacy use cases in other regions. |
| `payment_initiation` | [`LinkTokenCreateRequestPaymentInitiation`](../../doc/models/link-token-create-request-payment-initiation.md) | Optional | Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. |
| `deposit_switch` | [`LinkTokenCreateRequestDepositSwitch`](../../doc/models/link-token-create-request-deposit-switch.md) | Optional | Specifies options for initializing Link for use with the Deposit Switch (beta) product. This field is required if `deposit_switch` is included in the `products` array. |
| `income_verification` | [`LinkTokenCreateRequestIncomeVerification`](../../doc/models/link-token-create-request-income-verification.md) | Optional | Specifies options for initializing Link for use with the Income (beta) product. This field is required if `income_verification` is included in the `products` array. |
| `auth` | [`LinkTokenCreateRequestAuth`](../../doc/models/link-token-create-request-auth.md) | Optional | Specifies options for initializing Link for use with the Auth product. This field is currently only required if using the Flexible Auth product (currently in closed beta). |
| `update` | [`LinkTokenCreateRequestUpdate`](../../doc/models/link-token-create-request-update.md) | Optional | Specifies options for initializing Link for [update mode](https://plaid.com/docs/link/update-mode). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "client_name": "client_name2",
  "language": "language6",
  "country_codes": [
    "NL",
    "FR",
    "IE"
  ],
  "user": {
    "client_user_id": "client_user_id4",
    "legal_name": "legal_name8",
    "phone_number": "phone_number2",
    "phone_number_verified_time": "2016-03-13T12:52:32.123Z",
    "email_address": "email_address2",
    "email_address_verified_time": "2016-03-13T12:52:32.123Z",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "products": [
    "payment_initiation",
    "transactions",
    "credit_details"
  ],
  "webhook": "webhook2",
  "access_token": "access_token2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

