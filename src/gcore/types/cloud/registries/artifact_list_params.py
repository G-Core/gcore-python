# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ArtifactListParams"]


class ArtifactListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    registry_id: Required[int]

    limit: int
    """Limit the number of returned items"""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""
