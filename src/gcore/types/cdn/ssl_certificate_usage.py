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

    status: Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"]
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
