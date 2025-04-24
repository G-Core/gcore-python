# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VolumeCreateParams",
    "CreateVolumeFromImageSerializer",
    "CreateVolumeFromSnapshotSerializer",
    "CreateNewVolumeSerializer",
]


class CreateVolumeFromImageSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    image_id: Required[str]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/image_id'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.image_id"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/name'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.name"
    """

    size: Required[int]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/size'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.size"
    """

    source: Required[Literal["image"]]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/source'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.source"
    """

    attachment_tag: str
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/attachment_tag'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.attachment_tag"
    """

    instance_id_to_attach_to: str
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/instance_id_to_attach_to'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.instance_id_to_attach_to"
    """

    lifecycle_policy_ids: Iterable[int]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/lifecycle_policy_ids'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.lifecycle_policy_ids"
    """

    metadata: Dict[str, str]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/metadata'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.metadata"
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """
    '#/components/schemas/CreateVolumeFromImageSerializer/properties/type_name'
    "$.components.schemas.CreateVolumeFromImageSerializer.properties.type_name"
    """


class CreateVolumeFromSnapshotSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/name'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.name"
    """

    snapshot_id: Required[str]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/snapshot_id'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.snapshot_id"
    """

    source: Required[Literal["snapshot"]]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/source'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.source"
    """

    attachment_tag: str
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/attachment_tag'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.attachment_tag"
    """

    instance_id_to_attach_to: str
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/instance_id_to_attach_to'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.instance_id_to_attach_to"
    """

    lifecycle_policy_ids: Iterable[int]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/lifecycle_policy_ids'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.lifecycle_policy_ids"
    """

    metadata: Dict[str, str]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/metadata'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.metadata"
    """

    size: int
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/size'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.size"
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """
    '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/type_name'
    "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.type_name"
    """


class CreateNewVolumeSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/name'
    "$.components.schemas.CreateNewVolumeSerializer.properties.name"
    """

    size: Required[int]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/size'
    "$.components.schemas.CreateNewVolumeSerializer.properties.size"
    """

    source: Required[Literal["new-volume"]]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/source'
    "$.components.schemas.CreateNewVolumeSerializer.properties.source"
    """

    attachment_tag: str
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/attachment_tag'
    "$.components.schemas.CreateNewVolumeSerializer.properties.attachment_tag"
    """

    instance_id_to_attach_to: str
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/instance_id_to_attach_to'
    "$.components.schemas.CreateNewVolumeSerializer.properties.instance_id_to_attach_to"
    """

    lifecycle_policy_ids: Iterable[int]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/lifecycle_policy_ids'
    "$.components.schemas.CreateNewVolumeSerializer.properties.lifecycle_policy_ids"
    """

    metadata: Dict[str, str]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/metadata'
    "$.components.schemas.CreateNewVolumeSerializer.properties.metadata"
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """
    '#/components/schemas/CreateNewVolumeSerializer/properties/type_name'
    "$.components.schemas.CreateNewVolumeSerializer.properties.type_name"
    """


VolumeCreateParams: TypeAlias = Union[
    CreateVolumeFromImageSerializer, CreateVolumeFromSnapshotSerializer, CreateNewVolumeSerializer
]
