# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .user_lang import UserLang
from .user_group_v2 import UserGroupV2

__all__ = ["User"]


class User(BaseModel):
    """Fixed field set for /v2/users."""

    id: int

    activated: bool
    """Whether the user's membership in this client is activated."""

    auth_types: List[str]
    """List of authentication methods available to the user (e.g., 'password', 'sso')."""

    client: Optional[int] = None

    created_at: Optional[datetime] = None

    email: str
    """User's email address used for login and notifications."""

    groups: List[UserGroupV2]

    name: str
    """Full name of the user."""

    two_fa: bool
    """Indicates whether two-factor authentication (TOTP) is enabled for the user."""

    user_type: str

    lang: Optional[UserLang] = None

    phone: Optional[str] = None
    """User phone"""
