# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["SubnetListParams"]


class SubnetListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[2]"
    """

    metadata_k: List[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[3]"
    """

    metadata_kv: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[4]"
    """

    network_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[5]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[6]"
    """

    order_by: Literal[
        "available_ips.asc",
        "available_ips.desc",
        "cidr.asc",
        "cidr.desc",
        "created_at.asc",
        "created_at.desc",
        "name.asc",
        "name.desc",
        "total_ips.asc",
        "total_ips.desc",
        "updated_at.asc",
        "updated_at.desc",
    ]
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].get.parameters[7]"
    """
