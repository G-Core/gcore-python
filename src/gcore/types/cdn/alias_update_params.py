# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AliasUpdateParams"]


class AliasUpdateParams(TypedDict, total=False):
    active: bool
    """Whether the alias is enabled.

    Possible values:

    - `true` – The alias is enabled.
    - `false` – The alias is paused and is not served. Certificate issuance stops,
      though an attempt already being processed completes.
    """

    automated: bool
    """How the alias certificate is managed.

    Change it to switch the alias between a Let's Encrypt certificate and your own.
    Cannot be changed while the alias is paused.

    Possible values:

    - `true` – Switch to a Let's Encrypt certificate. `ssl_id` must be omitted. The
      current certificate keeps being served until the new one is issued.
    - `false` – Switch to your own certificate. `ssl_id` is required and is served
      immediately.
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

    ssl_id: int
    """ID of your own SSL certificate to serve for the alias instead of the current
    one.

    The certificate must cover the alias hostname; a Let's Encrypt certificate
    issued for one of your CDN resources cannot be used. Available for an alias with
    `automated` set to `false`, and together with `automated` set to `false` to
    switch to your own certificate.
    """
