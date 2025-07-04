# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["VolumeListParams"]


class VolumeListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    bootable: bool
    """Filter by bootable field"""

    cluster_id: str
    """Filter volumes by k8s cluster ID"""

    has_attachments: bool
    """Filter by the presence of attachments"""

    id_part: str
    """Filter the volume list result by the ID part of the volume"""

    instance_id: str
    """Filter volumes by instance ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    name_part: str
    """
    Filter volumes by `name_part` inclusion in volume name.Any substring can be used
    and volumes will be returned with names containing the substring.
    """

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    tag_key: List[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""
