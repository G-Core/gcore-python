# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["APITokenList", "APITokenListItem", "APITokenListItemClientUser", "APITokenListItemClientUserRole"]


class APITokenListItemClientUserRole(BaseModel):
    id: Optional[int] = None
    """Group's ID: Possible values are:

    - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
      (API+Web)* 3022 - Purge and Prefetch only (API)
    """

    name: Optional[
        Literal[
            "Users", "Administrators", "Engineers", "Purge and Prefetch only (API)", "Purge and Prefetch only (API+Web)"
        ]
    ] = None
    """Group's name."""


class APITokenListItemClientUser(BaseModel):
    client_id: int
    """Account's ID."""

    deleted: bool
    """Deletion flag. If true, then the API token was deleted."""

    role: APITokenListItemClientUserRole

    user_email: str
    """User's email who issued the API token."""

    user_id: int
    """User's ID who issued the API token."""

    user_name: str
    """User's name who issued the API token."""


class APITokenListItem(BaseModel):
    id: int
    """API token ID."""

    client_user: APITokenListItemClientUser

    created: str
    """Date when the API token was issued (ISO 8086/RFC 3339 format), UTC."""

    deleted: bool
    """Deletion flag. If true, then the API token was deleted."""

    exp_date: Optional[str] = None
    """
    Date when the API token becomes expired (ISO 8086/RFC 3339 format), UTC. If
    null, then the API token will never expire.
    """

    expired: bool
    """Expiration flag.

    If true, then the API token has expired. When an API token expires it will be
    automatically deleted.
    """

    last_usage: str
    """Date when the API token was last used (ISO 8086/RFC 3339 format), UTC."""

    name: str
    """API token name."""

    description: Optional[str] = None
    """API token description."""


APITokenList: TypeAlias = List[APITokenListItem]
