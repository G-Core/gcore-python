# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["GPUBaremetalClusterRebuildParams"]


class GPUBaremetalClusterRebuildParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/0/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Frebuild/post/parameters/1/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/rebuild'].post.parameters[1].schema"
    """

    nodes: Required[List[str]]
    """
    '#/components/schemas/RebuildClusterSerializer/properties/nodes'
    "$.components.schemas.RebuildClusterSerializer.properties.nodes"
    """

    image_id: Optional[str]
    """
    '#/components/schemas/RebuildClusterSerializer/properties/image_id/anyOf/0'
    "$.components.schemas.RebuildClusterSerializer.properties.image_id.anyOf[0]"
    """

    user_data: Optional[str]
    """
    '#/components/schemas/RebuildClusterSerializer/properties/user_data/anyOf/0'
    "$.components.schemas.RebuildClusterSerializer.properties.user_data.anyOf[0]"
    """
