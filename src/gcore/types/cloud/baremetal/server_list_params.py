# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ServerListParams"]


class ServerListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[1].schema"
    """

    changes_before: Annotated[Union[str, datetime], PropertyInfo(alias="changes-before", format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[2]"
    """

    changes_since: Annotated[Union[str, datetime], PropertyInfo(alias="changes-since", format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[3]"
    """

    flavor_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[4]"
    """

    flavor_prefix: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[5]"
    """

    include_k8s: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[6]"
    """

    ip: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[7]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[8]"
    """

    name: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[9]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[10]"
    """

    only_isolated: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[11]"
    """

    only_with_fixed_external_ip: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/12'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[12]"
    """

    order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/13'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[13]"
    """

    profile_name: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/14'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[14]"
    """

    protection_status: Literal["Active", "Queued", "Error"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/15'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[15]"
    """

    status: Literal["ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/16'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[16]"
    """

    tag_key_value: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/17'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[17]"
    """

    tag_value: List[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/18'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[18]"
    """

    type_ddos_profile: Literal["basic", "advanced"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/19'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[19]"
    """

    uuid: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/20'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[20]"
    """

    with_ddos: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/21'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[21]"
    """

    with_interfaces_name: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/22'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].get.parameters[22]"
    """
