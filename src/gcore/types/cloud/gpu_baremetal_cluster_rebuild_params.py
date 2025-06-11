# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GPUBaremetalClusterRebuildParams"]


class GPUBaremetalClusterRebuildParams(TypedDict, total=False):
    project_id: int

    region_id: int

    nodes: Required[List[str]]
    """List of nodes uuids to be rebuild"""

    image_id: Optional[str]
    """AI GPU image ID"""

    user_data: Optional[str]
    """
    String in base64 format.Examples of the `user_data`:
    https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """
