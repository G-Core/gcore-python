# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LoadBalancerListParams"]


class LoadBalancerListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    assigned_floating: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[2]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[3]"
    """

    logging_enabled: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[4]"
    """

    metadata_k: str
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[5]"
    """

    metadata_kv: str
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[6]"
    """

    name: str
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[7]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[8]"
    """

    order_by: str
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[9]"
    """

    show_stats: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[10]"
    """

    with_ddos: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].get.parameters[11]"
    """
