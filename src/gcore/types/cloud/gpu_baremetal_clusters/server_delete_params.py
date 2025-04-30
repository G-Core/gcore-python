# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/0/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[0].schema"
    """

    region_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/1/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[1].schema"
    """

    cluster_id: Required[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/2/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[2].schema"
    """

    delete_floatings: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D%2Fnode%2F%7Binstance_id%7D/delete/parameters/4'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}/{cluster_id}/node/{instance_id}']['delete'].parameters[4]"
    """
