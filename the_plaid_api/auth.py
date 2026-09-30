from __future__ import annotations

from dataclasses import dataclass

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    plaid_client_id: AuthScheme
    plaid_secret: AuthScheme
    plaid_version: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    plaid_client_id: AsyncAuthScheme
    plaid_secret: AsyncAuthScheme
    plaid_version: AsyncAuthScheme
