# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["User", "Group"]


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


class User(BaseModel):
    id: Optional[int] = None
    """User's ID."""

    activated: Optional[bool] = None
    """Email confirmation:

    - `true` – user confirmed the email;
    - `false` – user did not confirm the email.
    """

    auth_types: Optional[List[Literal["password", "sso", "github", "google-oauth2"]]] = None
    """System field. List of auth types available for the account."""

    client: Optional[float] = None
    """User's account ID."""

    company: Optional[str] = None
    """User's company."""

    deleted: Optional[bool] = None
    """Deletion flag. If `true` then user was deleted."""

    email: Optional[str] = None
    """User's email address."""

    groups: Optional[List[Group]] = None
    """User's group in the current account.

    IAM supports 5 groups:

    - Users
    - Administrators
    - Engineers
    - Purge and Prefetch only (API)
    - Purge and Prefetch only (API+Web)
    """

    lang: Optional[Literal["de", "en", "ru", "zh", "az"]] = None
    """User's language.

    Defines language of the control panel and email messages.
    """

    name: Optional[str] = None
    """User's name."""

    phone: Optional[str] = None
    """User's phone."""

    reseller: Optional[int] = None
    """Services provider ID."""

    sso_auth: Optional[bool] = None
    """SSO authentication flag. If `true` then user can login via SAML SSO."""

    two_fa: Optional[bool] = None
    """Two-step verification:

    - `true` – user enabled two-step verification;
    - `false` – user disabled two-step verification.
    """

    user_type: Optional[Literal["common"]] = None
    """User's type."""
