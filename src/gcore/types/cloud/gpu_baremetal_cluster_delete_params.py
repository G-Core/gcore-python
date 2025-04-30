# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GPUBaremetalClusterDeleteParams"]


class GPUBaremetalClusterDeleteParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/0/schema'
    "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/1/schema'
    "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[1].schema"
    """

    delete_floatings: bool
    """
    '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/3'
    "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[3]"
    """

    floatings: str
    """
    '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/4'
    "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[4]"
    """

    reserved_fixed_ips: str
    """
    '#/paths/%2Fcloud%2Fv2%2Fai%2Fclusters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bcluster_id%7D/delete/parameters/5'
    "$.paths['/cloud/v2/ai/clusters/{project_id}/{region_id}/{cluster_id}']['delete'].parameters[5]"
    """
