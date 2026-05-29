
# Mfa

Specifies the multi-factor authentication settings to use with this test account

*This model accepts additional fields of type Any.*

## Structure

`Mfa`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Possible values are `device`, `selections`, or `questions`.<br><br>If value is `device`, the MFA answer is `1234`.<br><br>If value is `selections`, the MFA answer is always the first option.<br><br>If value is `questions`, the MFA answer is  `answer_<i>_<j>` for the j-th question in the i-th round, starting from 0. For example, the answer to the first question in the second round is `answer_1_0`. |
| `question_rounds` | `float` | Required | Number of rounds of questions. Required if value of `type` is `questions`. |
| `questions_per_round` | `float` | Required | Number of questions per round. Required if value of `type` is `questions`. If value of type is `selections`, default value is 2. |
| `selection_rounds` | `float` | Required | Number of rounds of selections, used if `type` is `selections`. Defaults to 1. |
| `selections_per_question` | `float` | Required | Number of available answers per question, used if `type` is `selection`. Defaults to 2. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "type0",
  "question_rounds": 169.62,
  "questions_per_round": 161.58,
  "selection_rounds": 198.1,
  "selections_per_question": 232.84,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

