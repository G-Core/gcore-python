# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClusterUpgradeParams"]


class ClusterUpgradeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    version: Required[str]
    """Target k8s cluster version"""
