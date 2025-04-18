# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHKeyCreateParams"]


class SSHKeyCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/ssh_keys/{project_id}'].post.parameters[0].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateSSHKeySerializer/properties/name'
    "$.components.schemas.CreateSSHKeySerializer.properties.name"
    """

    public_key: str
    """
    '#/components/schemas/CreateSSHKeySerializer/properties/public_key'
    "$.components.schemas.CreateSSHKeySerializer.properties.public_key"
    """

    shared_in_project: bool
    """
    '#/components/schemas/CreateSSHKeySerializer/properties/shared_in_project'
    "$.components.schemas.CreateSSHKeySerializer.properties.shared_in_project"
    """
