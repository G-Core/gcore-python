# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[0].schema"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/1'
    "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[1]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/2'
    "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[2]"
    """
