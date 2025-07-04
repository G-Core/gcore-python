# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccountOverview",
    "FreeFeatures",
    "FreeFeaturesCdn",
    "FreeFeaturesCloud",
    "FreeFeaturesDDOS",
    "FreeFeaturesDNS",
    "FreeFeaturesStorage",
    "FreeFeaturesStreaming",
    "PaidFeatures",
    "PaidFeaturesCdn",
    "PaidFeaturesCloud",
    "PaidFeaturesDDOS",
    "PaidFeaturesDNS",
    "PaidFeaturesStorage",
    "PaidFeaturesStreaming",
    "ServiceStatuses",
    "ServiceStatusesCdn",
    "ServiceStatusesCloud",
    "ServiceStatusesDDOS",
    "ServiceStatusesDNS",
    "ServiceStatusesStorage",
    "ServiceStatusesStreaming",
    "User",
    "UserGroup",
]


class FreeFeaturesCdn(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeaturesCloud(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeaturesDDOS(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeaturesDNS(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeaturesStorage(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeaturesStreaming(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    free_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    name: Optional[str] = None
    """Name of the feature."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class FreeFeatures(BaseModel):
    cdn: Optional[List[FreeFeaturesCdn]] = FieldInfo(alias="CDN", default=None)

    cloud: Optional[List[FreeFeaturesCloud]] = FieldInfo(alias="CLOUD", default=None)

    ddos: Optional[List[FreeFeaturesDDOS]] = FieldInfo(alias="DDOS", default=None)

    dns: Optional[List[FreeFeaturesDNS]] = FieldInfo(alias="DNS", default=None)

    storage: Optional[List[FreeFeaturesStorage]] = FieldInfo(alias="STORAGE", default=None)

    streaming: Optional[List[FreeFeaturesStreaming]] = FieldInfo(alias="STREAMING", default=None)


class PaidFeaturesCdn(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeaturesCloud(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeaturesDDOS(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeaturesDNS(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeaturesStorage(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeaturesStreaming(BaseModel):
    create_date: Optional[str] = None
    """Date and time when the feature was activated (ISO 8086/RFC 3339 format)."""

    feature_id: Optional[int] = None
    """Feature ID."""

    name: Optional[str] = None
    """Name of the feature."""

    paid_feature_id: Optional[int] = None
    """Internal feature activation ID."""

    service: Optional[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]] = None
    """Service's name."""


class PaidFeatures(BaseModel):
    cdn: Optional[List[PaidFeaturesCdn]] = FieldInfo(alias="CDN", default=None)

    cloud: Optional[List[PaidFeaturesCloud]] = FieldInfo(alias="CLOUD", default=None)

    ddos: Optional[List[PaidFeaturesDDOS]] = FieldInfo(alias="DDOS", default=None)

    dns: Optional[List[PaidFeaturesDNS]] = FieldInfo(alias="DNS", default=None)

    storage: Optional[List[PaidFeaturesStorage]] = FieldInfo(alias="STORAGE", default=None)

    streaming: Optional[List[PaidFeaturesStreaming]] = FieldInfo(alias="STREAMING", default=None)


class ServiceStatusesCdn(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatusesCloud(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatusesDDOS(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatusesDNS(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatusesStorage(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatusesStreaming(BaseModel):
    enabled: Optional[bool] = None
    """`true` - service is available in the Control Panel."""

    status: Optional[Literal["new", "trial", "trialend", "active", "paused", "activating", "deleted"]] = None
    """Status of the service."""


class ServiceStatuses(BaseModel):
    cdn: Optional[ServiceStatusesCdn] = FieldInfo(alias="CDN", default=None)

    cloud: Optional[ServiceStatusesCloud] = FieldInfo(alias="CLOUD", default=None)

    ddos: Optional[ServiceStatusesDDOS] = FieldInfo(alias="DDOS", default=None)

    dns: Optional[ServiceStatusesDNS] = FieldInfo(alias="DNS", default=None)

    storage: Optional[ServiceStatusesStorage] = FieldInfo(alias="STORAGE", default=None)

    streaming: Optional[ServiceStatusesStreaming] = FieldInfo(alias="STREAMING", default=None)


class UserGroup(BaseModel):
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

    groups: Optional[List[UserGroup]] = None
    """User's group in the current account. IAM supports 5 groups:

    - Users
    - Administrators
    - Engineers
    - Purge and Prefetch only (API)
    - Purge and Prefetch only (API+Web)
    """

    lang: Optional[Literal["de", "en", "ru", "zh", "az"]] = None
    """User's language. Defines language of the control panel and email messages."""

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


class AccountOverview(BaseModel):
    id: Optional[int] = None
    """The account ID."""

    bill_type: Optional[str] = None
    """System field. Billing type of the account."""

    capabilities: Optional[List[Literal["CDN", "STORAGE", "STREAMING", "DNS", "DDOS", "CLOUD"]]] = None
    """System field. List of services available for the account."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The company name."""

    country_code: Optional[str] = None
    """System field. The company country (ISO 3166-1 alpha-2 format)."""

    current_user: Optional[int] = FieldInfo(alias="currentUser", default=None)
    """ID of the current user."""

    custom_id: Optional[str] = None
    """The account custom ID."""

    deleted: Optional[bool] = None
    """The field shows the status of the account:

    - `true` – the account has been deleted
    - `false` – the account is not deleted
    """

    email: Optional[str] = None
    """The account email."""

    entry_base_domain: Optional[str] = FieldInfo(alias="entryBaseDomain", default=None)
    """System field. Control panel domain."""

    free_features: Optional[FreeFeatures] = FieldInfo(alias="freeFeatures", default=None)
    """
    An object of arrays which contains information about free features available for
    the requested account.
    """

    has_active_admin: Optional[bool] = None
    """System field."""

    is_test: Optional[bool] = None
    """System field:

    - `true` — a test account;
    - `false` — a production account.
    """

    name: Optional[str] = None
    """Name of a user who registered the requested account."""

    paid_features: Optional[PaidFeatures] = FieldInfo(alias="paidFeatures", default=None)
    """
    An object of arrays which contains information about paid features available for
    the requested account.
    """

    phone: Optional[str] = None
    """Phone of a user who registered the requested account."""

    service_statuses: Optional[ServiceStatuses] = FieldInfo(alias="serviceStatuses", default=None)
    """
    An object of arrays which contains information about all services available for
    the requested account.
    """

    signup_process: Optional[Literal["sign_up_full", "sign_up_simple"]] = None
    """System field. Type of the account registration process."""

    status: Optional[Literal["new", "trial", "trialend", "active", "integration", "paused", "preparation", "ready"]] = (
        None
    )
    """Status of the account."""

    users: Optional[List[User]] = None
    """List of account users."""

    website: Optional[str] = None
    """The company website."""
