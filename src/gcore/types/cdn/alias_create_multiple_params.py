# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AliasCreateMultipleParams", "Item"]


class AliasCreateMultipleParams(TypedDict, total=False):
    items: Required[Iterable[Item]]
    """Aliases to create."""

    resource_id: Required[int]
    """ID of the CDN resource whose settings the aliases are served with."""


class Item(TypedDict, total=False):
    cname: Required[str]
    """Alias hostname."""

    automated: bool
    """How the alias certificate is managed.

    Defaults to **true** when `ssl_id` is omitted and to **false** when `ssl_id` is
    passed.
    """

    ssl_id: Optional[int]
    """ID of your own SSL certificate to serve for the alias.

    A Let's Encrypt certificate issued for one of your CDN resources cannot be used.
    Omit it to have a Let's Encrypt certificate issued automatically.
    """
