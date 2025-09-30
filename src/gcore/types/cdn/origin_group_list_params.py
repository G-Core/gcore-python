# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OriginGroupListParams"]


class OriginGroupListParams(TypedDict, total=False):
    has_related_resources: bool
    """Defines whether the origin group has related CDN resources.

    Possible values:

    - **true** – Origin group has related CDN resources.
    - **false** – Origin group does not have related CDN resources.
    """

    name: str
    """Origin group name."""

    sources: str
    """Origin sources (IP addresses or domains) in the origin group."""
