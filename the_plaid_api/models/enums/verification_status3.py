from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VerificationStatus3(str, Enum):
    """``VERIFICATION_STATUS_PROCESSING_COMPLETE``: The income verification status processing has completed.

    ``VERIFICATION_STATUS_DOCUMENT_REJECTED``: The documentation uploaded by the end user was recognized as a supported
    file format, but not recognized as a valid paystub.

    ``VERIFICATION_STATUS_PROCESSING_FAILED``: A failure occurred when attempting to process the verification
    documentation."""

    VERIFICATION_STATUS_PROCESSING_COMPLETE = "VERIFICATION_STATUS_PROCESSING_COMPLETE"
    VERIFICATION_STATUS_DOCUMENT_REJECTED = "VERIFICATION_STATUS_DOCUMENT_REJECTED"
    VERIFICATION_STATUS_PROCESSING_FAILED = "VERIFICATION_STATUS_PROCESSING_FAILED"

    __str__ = str.__str__


VerificationStatus3OrStr: TypeAlias = Annotated[VerificationStatus3 | str, open_enum_validator(VerificationStatus3)]
