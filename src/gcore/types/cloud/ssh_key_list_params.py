# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SSHKeyListParams"]


class SSHKeyListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[0].schema"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/1'
    "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[1]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/2'
    "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[2]"
    """

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/ssh_keys/{project_id}'].get.parameters[3]"
    """
