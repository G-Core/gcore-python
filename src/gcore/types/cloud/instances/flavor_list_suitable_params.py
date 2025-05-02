# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FlavorListSuitableParams", "Volume"]


class FlavorListSuitableParams(TypedDict, total=False):
    project_id: int

    region_id: int

    volumes: Required[Iterable[Volume]]
    """Volumes details. Non-important info such as names may be omitted."""

    include_prices: bool
    """Set to true if flavor listing should include flavor prices"""


class Volume(TypedDict, total=False):
    source: Required[Literal["apptemplate", "existing-volume", "image", "new-volume", "snapshot"]]
    """Volume source"""

    apptemplate_id: str
    """App template ID. Mandatory if volume is created from marketplace template"""

    boot_index: int
    """
    0 should be set for primary boot device Unique positive values for other
    bootable devices.Negative - boot prohibited
    """

    image_id: str
    """Image ID. Mandatory if volume is created from image"""

    name: Optional[str]

    size: int
    """Volume size.

    Must be specified when source is 'new-volume' or 'image'. If specified for
    source 'snapshot' or 'existing-volume', value must be equal to respective
    snapshot or volume size
    """

    snapshot_id: str
    """Volume snapshot ID. Mandatory if volume is created from a snapshot"""

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """One of 'standard', 'ssd_hiiops', 'ssd_local', 'ssd_lowlatency', 'cold', 'ultra'"""

    volume_id: str
    """Volume ID. Mandatory if volume is pre-existing volume"""
