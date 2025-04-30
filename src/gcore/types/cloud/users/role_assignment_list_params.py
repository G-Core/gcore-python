# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RoleAssignmentListParams"]


class RoleAssignmentListParams(TypedDict, total=False):
    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fusers%2Fassignments/get/parameters/0'
    "$.paths['/cloud/v1/users/assignments'].get.parameters[0]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fusers%2Fassignments/get/parameters/1'
    "$.paths['/cloud/v1/users/assignments'].get.parameters[1]"
    """

    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fusers%2Fassignments/get/parameters/2'
    "$.paths['/cloud/v1/users/assignments'].get.parameters[2]"
    """

    user_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fusers%2Fassignments/get/parameters/3'
    "$.paths['/cloud/v1/users/assignments'].get.parameters[3]"
    """
