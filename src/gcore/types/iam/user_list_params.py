# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    auth_type: Literal["password", "sso", "google-oauth2", "github"]
    """Filter by login method - a specific social provider, 'sso', or 'password'."""

    created_at: Dict[str, object]
    """Filter by creation time.

    Bracket operator required: `created_at[gte]`, `created_at[gt]`, `created_at[lt]`
    or `created_at[lte]` (ISO 8601), e.g.
    `created_at[gte]=2026-01-01T00:00:00Z&created_at[lt]=2026-02-01T00:00:00Z`.
    """

    email: Dict[str, object]
    """Filter by email, case-insensitive.

    Bracket operator required: `email[exact]`, `email[prefix]`, `email[contains]` or
    `email[suffix]`, e.g. `email[contains]=example.com`.
    """

    ids: Iterable[int]
    """Filter by user id.

    Repeat the parameter for several values (OR), e.g. `ids=1&ids=2`.
    """

    langs: List[Literal["az", "de", "en", "ru", "zh"]]
    """Filter by interface language.

    Repeat the parameter for several values (OR), e.g. `langs=en&langs=ru`.
    """

    limit: int
    """The maximum number of items."""

    name: Dict[str, object]
    """Filter by name, case-insensitive.

    Bracket operator required: `name[exact]`, `name[prefix]`, `name[contains]` or
    `name[suffix]`, e.g. `name[prefix]=Jo`.
    """

    offset: int
    """Offset relative to the beginning of list."""

    order_by: str
    """Sort order as `field.direction`, e.g.

    `order_by=created_at.desc`. Allowed fields: `created_at`, `email`, `name`.
    Defaults to `created_at.desc`.
    """
