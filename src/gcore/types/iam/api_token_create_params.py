# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .user_group_param import UserGroupParam

__all__ = ["APITokenCreateParams", "ClientUser"]


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

    assign_default_policy: bool
    """
    Whether the new API token gets the default access policy of its role. Set to
    `false` if you will bind policies or permission sets to the token yourself: the
    token then has no permissions until you do.
    """

    description: str
    """API token description."""


class ClientUser(TypedDict, total=False):
    """API token role."""

    role: UserGroupParam
