# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PriceVolumeSpecParam", "Source"]


class Source(TypedDict, total=False):
    """Image, snapshot or volume to create the volume from.

    Omit it for a blank volume.
    """

    id: Required[str]
    """ID of the image, the snapshot or the volume to clone.

    Only a source volume of type `standard` or `ssd_hiiops` can be cloned.
    """

    type: Required[Literal["image", "snapshot", "volume"]]
    """What the volume is created from."""


class PriceVolumeSpecParam(TypedDict, total=False):
    size: int
    """Size in GiB.

    Required for a blank or image volume. A volume from a snapshot or a volume has
    the size of its source, and a larger size grows it.
    """

    source: Source
    """Image, snapshot or volume to create the volume from.

    Omit it for a blank volume.
    """

    type: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type.

    A volume from a snapshot or a volume has the type of its source. Any other
    volume is `standard` by default.
    """
