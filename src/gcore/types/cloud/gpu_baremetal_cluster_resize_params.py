# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GPUBaremetalClusterResizeParams"]


class GPUBaremetalClusterResizeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/0/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fresize/post/parameters/1/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/resize'].post.parameters[1].schema"
    """

    instances_count: Required[int]
    """
    '#/components/schemas/ResizeAIClusterGPUSerializerV1/properties/instances_count'
    "$.components.schemas.ResizeAIClusterGPUSerializerV1.properties.instances_count"
    """
