# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UserUpdate", "ClientAndRole", "Group"]


class ClientAndRole(BaseModel):
    client_company_name: str

    client_id: int

    user_id: int
    """User's ID."""

    user_roles: List[str]
    """User role in this client."""


class Group(BaseModel):
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


class UserUpdate(BaseModel):
    id: int
    """User's ID."""

    activated: bool
    """Email confirmation:

    - `true` – user confirmed the email;
    - `false` – user did not confirm the email.
    """

    auth_types: List[Literal["password", "sso", "github", "google-oauth2"]]
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

    groups: List[Group]
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

    lang: Literal["de", "en", "ru", "zh", "az"]
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

    user_type: Literal["common", "reseller", "seller"]
    """User's type."""
