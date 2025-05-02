# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VolumeAttachToInstanceParams"]


class VolumeAttachToInstanceParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    instance_id: Required[str]
    """Instance ID."""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)."""
