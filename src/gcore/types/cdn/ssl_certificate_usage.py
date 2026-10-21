# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SslCertificateUsage", "Alias", "Resource"]


class Alias(BaseModel):
    id: int
    """Alias ID."""

    cname: str
    """Alias hostname."""

    status: Literal["inactive", "pending", "http_only", "active"]
    """Alias status.

    Possible values:

    - `inactive` – The alias or its CDN resource is disabled; the alias is not
      served.
    - `pending` – The alias configuration has not reached the CDN yet.
    - `http_only` – The alias is served over HTTP only.
    - `active` – The alias is served over HTTP and HTTPS.
    """


class Resource(BaseModel):
    id: int
    """CDN resource ID."""

    cname: str
    """CDN resource CNAME (primary hostname)."""

    status: Literal["active", "suspended", "processed", "deleted"]
    """CDN resource status.

    Possible values:

    - **active** - CDN resource is active. Content is available to users.
    - **suspended** - CDN resource is suspended. Content is not available to users.
    - **processed** - CDN resource has recently been created and is currently being
      processed. It will take about fifteen minutes to propagate it to all
      locations.
    - **deleted** - CDN resource is deleted.
    """


class SslCertificateUsage(BaseModel):
    """List of CDN resources and aliases using this SSL certificate."""

    aliases: List[Alias]
    """
    Aliases that have this certificate attached, including one in the process of
    issuance.
    """

    resources: List[Resource]
    """CDN resources that have this certificate attached."""
