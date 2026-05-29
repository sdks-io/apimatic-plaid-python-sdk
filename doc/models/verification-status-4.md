
# Verification Status 4

The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.

`pending_automatic_verification`: The Item is pending automatic verification

`pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.

`automatically_verified`: The Item has successfully been automatically verified

`manually_verified`: The Item has successfully been manually verified

`verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.

`verification_failed`: The Item failed manual micro-deposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.

*This model accepts additional fields of type Any.*

## Enumeration

`VerificationStatus4`

## Fields

| Name |
|  --- |
| `AUTOMATICALLY_VERIFIED` |
| `PENDING_AUTOMATIC_VERIFICATION` |
| `PENDING_MANUAL_VERIFICATION` |
| `MANUALLY_VERIFIED` |
| `VERIFICATION_EXPIRED` |
| `VERIFICATION_FAILED` |

