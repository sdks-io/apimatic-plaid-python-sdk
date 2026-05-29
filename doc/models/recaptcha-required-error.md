
# Recaptcha Required Error

The request was flagged by Plaid's fraud system, and requires additional verification to ensure they are not a bot.

*This model accepts additional fields of type Any.*

## Structure

`RecaptchaRequiredError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_type` | `str` | Required | RECAPTCHA_ERROR |
| `error_code` | `str` | Required | RECAPTCHA_REQUIRED |
| `display_message` | `str` | Required | - |
| `http_code` | `str` | Required | 400 |
| `link_user_experience` | `str` | Required | Your user will be prompted to solve a Google reCAPTCHA challenge in the Link Recaptcha pane. If they solve the challenge successfully, the user's request is resubmitted and they are directed to the next Item creation step. |
| `common_causes` | `str` | Required | Plaid's fraud system detects abusive traffic and considers a variety of parameters throughout Item creation requests. When a request is considered risky or possibly fraudulent, Link presents a reCAPTCHA for the user to solve. |
| `troubleshooting_steps` | `str` | Required | Link will automatically guide your user through reCAPTCHA verification. As a general rule, we recommend instrumenting basic fraud monitoring to detect and protect your website from spam and abuse.<br><br>If your user cannot verify their session, please submit a Support ticket with the following identifiers: `link_session_id` or `request_id` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "error_type": "error_type2",
  "error_code": "error_code6",
  "display_message": "display_message2",
  "http_code": "http_code0",
  "link_user_experience": "link_user_experience2",
  "common_causes": "common_causes8",
  "troubleshooting_steps": "troubleshooting_steps0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

