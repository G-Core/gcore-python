# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    client_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/0'
    "$.paths['/cloud/v1/projects'].get.parameters[0]"
    """

    include_deleted: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/1'
    "$.paths['/cloud/v1/projects'].get.parameters[1]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/2'
    "$.paths['/cloud/v1/projects'].get.parameters[2]"
    """

    name: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/3'
    "$.paths['/cloud/v1/projects'].get.parameters[3]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/4'
    "$.paths['/cloud/v1/projects'].get.parameters[4]"
    """

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects/get/parameters/5'
    "$.paths['/cloud/v1/projects'].get.parameters[5]"
    """
