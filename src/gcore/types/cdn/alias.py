# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Alias"]


class Alias(BaseModel):
    id: Optional[int] = None
    """Alias ID."""

    active: Optional[bool] = None
    """Whether you have enabled the alias.

    Enabling it does not by itself make it live: the alias is served only while
    `status` is **active**, **`ssl_issuing`** or **`ssl_error`**.

    Possible values:

    - **true** – The alias is enabled and is served once its certificate is ready.
    - **false** – The alias is paused and is not served.
    """

    automated: Optional[bool] = None
    """How the alias certificate is managed. Can be changed while the alias is served.

    Possible values:

    - **true** – A Let's Encrypt certificate is issued and renewed automatically.
    - **false** – The certificate referenced by `ssl_id` was added by you.
    """

    cname: Optional[str] = None
    """Alias hostname. Cannot be changed after creation."""

    created: Optional[str] = None
    """Date and time when the alias was created (ISO 8601/RFC 3339 format, UTC.)"""

    enabled: Optional[bool] = None
    """Whether the alias is enabled by the system.

    Follows the state of the CDN resource.

    Possible values:

    - **true** – The alias can be served.
    - **false** – The alias is not served because its CDN resource is not active.
    """

    resource_id: Optional[int] = None
    """ID of the CDN resource whose settings the alias is served with.

    Cannot be changed after creation.
    """

    ssl_id: Optional[int] = None
    """ID of the SSL certificate served for the alias.

    Null until a certificate is issued.
    """

    ssl_status: Optional[Literal["pending", "issued", "failed"]] = None
    """Outcome of the certificate we manage for the alias.

    Possible values:

    - **pending** – A certificate attempt is in progress.
    - **issued** – The latest attempt succeeded.
    - **failed** – The latest attempt ended without a certificate.
    - **null** – No certificate is managed for the alias: the alias uses a
      certificate you provided, or is automated and has never opened an attempt.
    """

    ssl_validity_not_after: Optional[str] = None
    """
    Date and time when the served certificate expires (ISO 8601/RFC 3339 format,
    UTC). Null while no certificate is served yet.
    """

    status: Optional[Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"]] = None
    """Alias status.

    Possible values:

    - **pending** – The certificate has not been issued yet; the alias is not
      served.
    - **active** – The alias is served with its certificate.
    - **`ssl_issuing`** – A new certificate is being issued; the current one keeps
      being served.
    - **`ssl_error`** – Certificate issuance failed; a previously issued certificate
      keeps being served.
    - **inactive** – The alias or its CDN resource is disabled; the alias is not
      served.
    """

    updated: Optional[str] = None
    """Date and time when the alias was last changed (ISO 8601/RFC 3339 format, UTC.)"""
