# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserUpdateParams", "Group"]


class UserUpdateParams(TypedDict, total=False):
    auth_types: List[Literal["password", "sso", "github", "google-oauth2"]]
    """System field. List of auth types available for the account."""

    company: str
    """User's company."""

    email: str
    """User's email address."""

    groups: Iterable[Group]
    """User's group in the current account. IAM supports 5 groups:

    - Users
    - Administrators
    - Engineers
    - Purge and Prefetch only (API)
    - Purge and Prefetch only (API+Web)
    """

    lang: Literal["de", "en", "ru", "zh", "az"]
    """User's language. Defines language of the control panel and email messages."""

    name: Optional[str]
    """User's name."""

    phone: Optional[str]
    """User's phone."""


class Group(TypedDict, total=False):
    id: int
    """Group's ID: Possible values are:

    - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
      (API+Web)* 3022 - Purge and Prefetch only (API)
    """

    name: Literal[
        "Users", "Administrators", "Engineers", "Purge and Prefetch only (API)", "Purge and Prefetch only (API+Web)"
    ]
    """Group's name."""
