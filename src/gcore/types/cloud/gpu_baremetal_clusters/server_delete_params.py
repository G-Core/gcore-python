# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: int

    region_id: int

    cluster_id: Required[str]

    delete_floatings: bool
    """Set False if you do not want to delete assigned floating IPs.

    By default, it's True.
    """
