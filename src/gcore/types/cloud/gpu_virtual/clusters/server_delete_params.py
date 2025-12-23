# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_id: Required[str]
    """Cluster unique identifier"""

    all_floating_ips: bool
    """
    Flag indicating whether the floating ips associated with server / cluster are
    deleted
    """

    all_reserved_fixed_ips: bool
    """
    Flag indicating whether the reserved fixed ips associated with server / cluster
    are deleted
    """

    all_volumes: bool
    """Flag indicating whether all attached volumes are deleted"""

    floating_ip_ids: SequenceNotStr[str]
    """Optional list of floating ips to be deleted"""

    reserved_fixed_ip_ids: SequenceNotStr[str]
    """Optional list of reserved fixed ips to be deleted"""

    volume_ids: SequenceNotStr[str]
    """Optional list of volumes to be deleted"""
