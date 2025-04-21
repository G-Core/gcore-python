# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReservedFixedIPListParams"]


class ReservedFixedIPListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    available_only: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[2]"
    """

    device_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[3]"
    """

    external_only: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[4]"
    """

    internal_only: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[5]"
    """

    ip_address: str
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[6]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[7]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[8]"
    """

    order_by: str
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[9]"
    """

    vip_only: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].get.parameters[10]"
    """
