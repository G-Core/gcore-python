# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .auth_type import AuthType
from .user_type import UserType
from .user_group import UserGroup
from .user_language import UserLanguage

__all__ = ["User", "ClientAndRole"]


class ClientAndRole(BaseModel):
    client_company_name: str

    client_id: int

    user_id: int
    """User's ID."""

    user_roles: List[str]
    """User role in this client."""


class User(BaseModel):
    id: int
    """User's ID."""

    activated: bool
    """Email confirmation:

    - `true` – user confirmed the email;
    - `false` – user did not confirm the email.
    """

    auth_types: List[AuthType]
    """System field. List of auth types available for the account."""

    client: float
    """User's account ID."""

    client_and_roles: List[ClientAndRole]
    """List of user's clients. User can access to one or more clients."""

    company: str
    """User's company."""

    deleted: bool
    """Deletion flag. If `true` then user was deleted."""

    email: str
    """User's email address."""

    groups: List[UserGroup]
    """User's group in the current account.

    IAM supports 5 groups:

    - Users
    - Administrators
    - Engineers
    - Purge and Prefetch only (API)
    - Purge and Prefetch only (API+Web)
    """

    is_active: bool
    """User activity flag."""

    lang: UserLanguage
    """User's language.

    Defines language of the control panel and email messages.
    """

    name: Optional[str] = None
    """User's name."""

    phone: Optional[str] = None
    """User's phone."""

    reseller: int
    """Services provider ID."""

    sso_auth: bool
    """SSO authentication flag. If `true` then user can login via SAML SSO."""

    two_fa: bool
    """Two-step verification:

    - `true` – user enabled two-step verification;
    - `false` – user disabled two-step verification.
    """

    user_type: UserType
    """User's type."""
