# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tag_update_map_param import TagUpdateMapParam

__all__ = [
    "VolumeCreateParams",
    "CreateVolumeFromImageSerializer",
    "CreateVolumeFromSnapshotSerializer",
    "CreateNewVolumeSerializer",
]


class CreateVolumeFromImageSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    image_id: Required[str]
    """Image ID"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["image"]]
    """Volume source type"""

    attachment_tag: str
    """Block device attachment tag (not exposed in the user tags).

    Only used in conjunction with `instance_id_to_attach_to`
    """

    instance_id_to_attach_to: str
    """`instance_id` to attach newly-created volume to"""

    lifecycle_policy_ids: Iterable[int]
    """
    List of lifecycle policy IDs (snapshot creation schedules) to associate with the
    volume
    """

    tags: TagUpdateMapParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type.

    Defaults to `standard`. If not specified for source `snapshot`, volume type will
    be derived from the snapshot volume.
    """


class CreateVolumeFromSnapshotSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """Volume name"""

    snapshot_id: Required[str]
    """Snapshot ID"""

    source: Required[Literal["snapshot"]]
    """Volume source type"""

    attachment_tag: str
    """Block device attachment tag (not exposed in the user tags).

    Only used in conjunction with `instance_id_to_attach_to`
    """

    instance_id_to_attach_to: str
    """`instance_id` to attach newly-created volume to"""

    lifecycle_policy_ids: Iterable[int]
    """
    List of lifecycle policy IDs (snapshot creation schedules) to associate with the
    volume
    """

    size: int
    """Volume size in GiB.

    If specified, value must be equal to respective snapshot size
    """

    tags: TagUpdateMapParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type.

    Defaults to `standard`. If not specified for source `snapshot`, volume type will
    be derived from the snapshot volume.
    """


class CreateNewVolumeSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["new-volume"]]
    """Volume source type"""

    attachment_tag: str
    """Block device attachment tag (not exposed in the user tags).

    Only used in conjunction with `instance_id_to_attach_to`
    """

    instance_id_to_attach_to: str
    """`instance_id` to attach newly-created volume to"""

    lifecycle_policy_ids: Iterable[int]
    """
    List of lifecycle policy IDs (snapshot creation schedules) to associate with the
    volume
    """

    tags: TagUpdateMapParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type.

    Defaults to `standard`. If not specified for source `snapshot`, volume type will
    be derived from the snapshot volume.
    """


VolumeCreateParams: TypeAlias = Union[
    CreateVolumeFromImageSerializer, CreateVolumeFromSnapshotSerializer, CreateNewVolumeSerializer
]
