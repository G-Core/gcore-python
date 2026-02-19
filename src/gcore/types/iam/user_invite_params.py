# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .user_language import UserLanguage
from .user_group_param import UserGroupParam

__all__ = ["UserInviteParams"]


class UserInviteParams(TypedDict, total=False):
    client_id: Required[int]
    """ID of account."""

    email: Required[str]
    """User email."""

    user_role: Required[UserGroupParam]

    lang: UserLanguage
    """User's language.

    Defines language of the control panel and email messages.
    """

    name: str
    """User name."""
