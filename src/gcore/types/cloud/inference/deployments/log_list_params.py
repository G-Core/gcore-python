# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[0].schema"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/2'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[2]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/3'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[3]"
    """

    order_by: Literal["time.asc", "time.desc"]
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/4'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[4]"
    """

    region_id: Optional[int]
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/5/schema/anyOf/0'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[5].schema.anyOf[0]"
    """
