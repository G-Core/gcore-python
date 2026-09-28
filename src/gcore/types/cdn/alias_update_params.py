# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AliasUpdateParams"]


class AliasUpdateParams(TypedDict, total=False):
    active: bool
    """Whether the alias is enabled.

    Possible values:

    - **true** – The alias is enabled and is served once its certificate is ready.
    - **false** – The alias is paused and is not served.
    """

    automated: bool
    """How the alias certificate is managed.

    Change it to switch the alias between a Let's Encrypt certificate and your own.
    Cannot be changed while the alias is paused.

    Possible values:

    - **true** – Switch to a Let's Encrypt certificate. `ssl_id` must be omitted.
      The current certificate keeps being served until the new one is issued.
    - **false** – Switch to your own certificate. `ssl_id` is required and is served
      immediately.
    """

    ssl_id: int
    """ID of your own SSL certificate to serve for the alias instead of the current
    one.

    The certificate must cover the alias hostname; a Let's Encrypt certificate
    issued for one of your CDN resources cannot be used. Available for an alias with
    `automated` set to **false**, and together with `automated` set to **false** to
    switch to your own certificate.
    """
