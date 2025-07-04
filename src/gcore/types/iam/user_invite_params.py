# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserInviteParams", "UserRole"]


class UserInviteParams(TypedDict, total=False):
    client_id: Required[int]
    """ID of account."""

    email: Required[str]
    """User email."""

    user_role: Required[UserRole]

    lang: Literal["de", "en", "ru", "zh", "az"]
    """User's language. Defines language of the control panel and email messages."""

    name: str
    """User name."""


class UserRole(TypedDict, total=False):
    id: int
    """Group's ID: Possible values are:

    - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
      (API+Web)* 3022 - Purge and Prefetch only (API)
    """

    name: Literal[
        "Users", "Administrators", "Engineers", "Purge and Prefetch only (API)", "Purge and Prefetch only (API+Web)"
    ]
    """Group's name."""
