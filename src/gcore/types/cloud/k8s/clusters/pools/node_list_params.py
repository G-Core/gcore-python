# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NodeListParams"]


class NodeListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    cluster_name: Required[str]

    with_ddos: bool
    """Include DDoS profile information if set to true. Default is false."""
