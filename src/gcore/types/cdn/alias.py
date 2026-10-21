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

    Possible values:

    - `true` – The alias is enabled.
    - `false` – The alias is paused and is not served.
    """

    automated: Optional[bool] = None
    """How the alias certificate is managed. Can be changed while the alias is served.

    Possible values:

    - `true` – A Let's Encrypt certificate is issued and renewed automatically.
    - `false` – The certificate referenced by `ssl_id`, if any, was added by you.
    """

    challenge_type: Optional[Literal["dns_01", "http_01"]] = None
    """
    Domain validation method used to issue the Let's Encrypt certificate for the
    alias.

    Possible values:

    - `dns_01` – Validation via a CNAME record for
      `_acme-challenge.<alias hostname>`, shown in
      `ssl_provisioning.acme_delegation`.
    - `http_01` – Validation via an HTTP request to the alias hostname. The alias
      hostname must point to your CDN CNAME, shown in
      `ssl_provisioning.http_validation`. The request is served with the settings of
      the alias's CDN resource, so they must not block or redirect
      `/.well-known/acme-challenge/`.
    """

    cname: Optional[str] = None
    """Alias hostname. Cannot be changed after creation."""

    created: Optional[str] = None
    """Date and time when the alias was created (ISO 8601/RFC 3339 format, UTC)."""

    enabled: Optional[bool] = None
    """Whether the alias is enabled by the system.

    Follows the state of the CDN resource.

    Possible values:

    - `true` – The alias can be served.
    - `false` – The alias is not served because its CDN resource is not active.
    """

    resource_id: Optional[int] = None
    """ID of the CDN resource whose settings the alias is served with.

    Cannot be changed after creation.
    """

    ssl_id: Optional[int] = None
    """ID of the SSL certificate served for the alias."""

    ssl_status: Optional[Literal["pending", "issued", "failed"]] = None
    """Outcome of the certificate we manage for the alias.

    Possible values:

    - `pending` – A certificate attempt is in progress, or was stopped by pausing
      the alias and starts again after it is resumed.
    - `issued` – The latest attempt succeeded.
    - `failed` – The latest attempt ended without a certificate.
    - `null` – No certificate is managed for the alias: the alias uses a certificate
      you provided, or is automated and has never opened an attempt.
    """

    ssl_validity_not_after: Optional[str] = None
    """
    Date and time when the served certificate expires (ISO 8601/RFC 3339 format,
    UTC). `null` while no certificate is served.
    """

    status: Optional[Literal["inactive", "pending", "http_only", "active"]] = None
    """Alias status.

    Possible values:

    - `inactive` – The alias or its CDN resource is disabled; the alias is not
      served.
    - `pending` – The alias configuration has not reached the CDN yet.
    - `http_only` – The alias is served over HTTP only.
    - `active` – The alias is served over HTTP and HTTPS.
    """

    updated: Optional[str] = None
    """Date and time when the alias was last changed (ISO 8601/RFC 3339 format, UTC)."""
