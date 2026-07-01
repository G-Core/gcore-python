# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerReplaceParams"]


class ServerReplaceParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_id: Required[str]
    """Cluster unique identifier"""

    keep_ip_addresses: bool
    """Retain the original Public/Private IPs on the replacement node (ethernet only).

    When false, new IPs are assigned. No effect on InfiniBand interfaces.
    """
