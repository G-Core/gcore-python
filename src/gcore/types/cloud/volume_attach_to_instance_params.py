# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VolumeAttachToInstanceParams"]


class VolumeAttachToInstanceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/0/schema'
    "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/1/schema'
    "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[1].schema"
    """

    instance_id: Required[str]
    """
    '#/components/schemas/AttachVolumeToInstanceSerializer/properties/instance_id'
    "$.components.schemas.AttachVolumeToInstanceSerializer.properties.instance_id"
    """

    attachment_tag: str
    """
    '#/components/schemas/AttachVolumeToInstanceSerializer/properties/attachment_tag'
    "$.components.schemas.AttachVolumeToInstanceSerializer.properties.attachment_tag"
    """
