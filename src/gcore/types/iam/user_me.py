# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .user_lang import UserLang
from .user_group_v2 import UserGroupV2

__all__ = ["UserMe", "ClientsAndRole"]


class ClientsAndRole(BaseModel):
    auth_types: List[str]

    client_company_name: str

    client_id: int

    user_id: int

    user_roles: List[str]


class UserMe(BaseModel):
    """The client-tier caller's own profile, including the clients they belong to."""

    id: int

    activated: bool
    """Whether the user's membership in this client is activated."""

    auth_types: List[str]
    """List of authentication methods available to the user (e.g., 'password', 'sso')."""

    can_disable_2fa: bool
    """
    False when the user cannot disable their own 2FA because they are an active
    member of an account that enforces 2FA. Use it to disable the Disable-2FA
    control.
    """

    client: Optional[int] = None

    clients_and_roles: List[ClientsAndRole]

    created_at: Optional[datetime] = None

    email: str
    """User's email address used for login and notifications."""

    groups: List[UserGroupV2]

    name: str
    """Full name of the user."""

    show_chat: bool
    """Whether the support chat widget should be shown."""

    two_fa: bool
    """Indicates whether two-factor authentication (TOTP) is enabled for the user."""

    user_type: str

    lang: Optional[UserLang] = None

    phone: Optional[str] = None
    """User phone"""
