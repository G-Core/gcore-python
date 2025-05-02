# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlacementGroupCreateParams"]


class PlacementGroupCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: Required[str]
    """The name of the server group."""

    policy: Required[Literal["affinity", "anti-affinity", "soft-anti-affinity"]]
    """The server group policy."""
