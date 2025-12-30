# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ClusterRebuildParams"]


class ClusterRebuildParams(TypedDict, total=False):
    project_id: int

    region_id: int

    nodes: Required[SequenceNotStr[str]]
    """List of nodes uuids to be rebuild"""

    image_id: Optional[str]
    """AI GPU image ID"""

    user_data: Optional[str]
    """
    String in base64 format.Examples of the `user_data`:
    https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """
