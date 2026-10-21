# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AliasCreateParams"]


class AliasCreateParams(TypedDict, total=False):
    cname: Required[str]
    """Alias hostname. Wildcard hostnames are not supported."""

    resource_id: Required[int]
    """ID of the CDN resource whose settings the alias is served with."""

    active: bool
    """Whether the alias is enabled. Defaults to `true`."""

    automated: bool
    """How the alias certificate is managed.

    Defaults to `true` when `ssl_id` is omitted and to `false` when `ssl_id` is
    passed.

    Possible values:

    - `true` – A Let's Encrypt certificate is issued and renewed automatically.
      `ssl_id` must be omitted.
    - `false` – Your own certificate referenced by `ssl_id`, if any, is served.
    """

    challenge_type: Literal["dns_01", "http_01"]
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

    ssl_id: Optional[int]
    """ID of your own SSL certificate to serve for the alias.

    The certificate must cover the alias hostname. A Let's Encrypt certificate
    issued for one of your CDN resources cannot be used.

    Omit it to have a Let's Encrypt certificate issued automatically.
    """
