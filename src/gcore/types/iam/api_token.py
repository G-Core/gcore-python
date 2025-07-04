# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIToken", "ClientUser", "ClientUserRole"]


class ClientUserRole(BaseModel):
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


class ClientUser(BaseModel):
    client_id: Optional[int] = None
    """Account's ID."""

    deleted: Optional[bool] = None
    """Deletion flag. If true, then the API token was deleted."""

    role: Optional[ClientUserRole] = None

    user_email: Optional[str] = None
    """User's email who issued the API token."""

    user_id: Optional[int] = None
    """User's ID who issued the API token."""

    user_name: Optional[str] = None
    """User's name who issued the API token."""


class APIToken(BaseModel):
    client_user: ClientUser

    exp_date: str
    """
    Date when the API token becomes expired (ISO 8086/RFC 3339 format), UTC. If
    null, then the API token will never expire.
    """

    name: str
    """API token name."""

    id: Optional[int] = None
    """API token ID."""

    created: Optional[str] = None
    """Date when the API token was issued (ISO 8086/RFC 3339 format), UTC."""

    deleted: Optional[bool] = None
    """Deletion flag. If true, then the API token was deleted."""

    description: Optional[str] = None
    """API token description."""

    expired: Optional[bool] = None
    """Expiration flag.

    If true, then the API token has expired. When an API token expires it will be
    automatically deleted.
    """

    last_usage: Optional[str] = None
    """Date when the API token was last used (ISO 8086/RFC 3339 format), UTC."""
