# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["VolumeSnapshotCreateParams"]


class VolumeSnapshotCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: Required[str]
    """Snapshot name"""

    volume_id: Required[str]
    """Volume ID to make snapshot of"""

    description: str
    """Snapshot description"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """
