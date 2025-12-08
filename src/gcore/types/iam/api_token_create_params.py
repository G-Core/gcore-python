# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["APITokenCreateParams", "ClientUser", "ClientUserRole"]


class APITokenCreateParams(TypedDict, total=False):
    client_user: Required[ClientUser]
    """API token role."""

    exp_date: Required[Optional[str]]
    """
    Date when the API token becomes expired (ISO 8086/RFC 3339 format), UTC. If
    null, then the API token will never expire.
    """

    name: Required[str]
    """API token name."""

    description: str
    """API token description."""


class ClientUserRole(TypedDict, total=False):
    id: int
    """Group's ID: Possible values are:

    - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
      (API+Web)* 3022 - Purge and Prefetch only (API)
    """

    name: Literal[
        "Users", "Administrators", "Engineers", "Purge and Prefetch only (API)", "Purge and Prefetch only (API+Web)"
    ]
    """Group's name."""


class ClientUser(TypedDict, total=False):
    """API token role."""

    role: ClientUserRole
