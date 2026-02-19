# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .auth_type import AuthType
from .user_language import UserLanguage

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    auth_types: Required[List[AuthType]]
    """System field. List of auth types available for the account."""

    email: Required[str]
    """User's email address."""

    lang: Required[UserLanguage]
    """User's language.

    Defines language of the control panel and email messages.
    """

    name: Required[Optional[str]]
    """User's name."""

    phone: Required[Optional[str]]
    """User's phone."""
