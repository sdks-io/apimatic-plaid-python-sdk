from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SandboxProcessorTokenCreateRequestOptions(SdkBaseModel):
    """An optional set of options to be used when configuring the Item. If specified, must not be ``null``."""

    override_username: str | None = "user_good"
    """Test username to use for the creation of the Sandbox Item. Default value is ``user_good``."""

    override_password: str | None = "pass_good"
    """Test password to use for the creation of the Sandbox Item. Default value is ``pass_good``."""


class SandboxProcessorTokenCreateRequestOptionsDict(TypedDict):
    override_username: NotRequired[str | None]
    override_password: NotRequired[str | None]
