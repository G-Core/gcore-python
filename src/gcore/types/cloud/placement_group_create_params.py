# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlacementGroupCreateParams"]


class PlacementGroupCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    name: Required[str]
    """Placement group name.

    A name starting with `k8s-` is rejected with 400 `validation-error`. The prefix
    is reserved for the groups that managed Kubernetes creates.
    """

    policy: Required[Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]]
    """
    Placement policy: affinity, anti-affinity, soft-affinity, or soft-anti-affinity.
    """

    region_id: Required[int]
    """Region to create the placement group in."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """
