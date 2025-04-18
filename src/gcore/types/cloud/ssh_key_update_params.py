# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHKeyUpdateParams"]


class SSHKeyUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fssh_keys%2F%7Bproject_id%7D%2F%7Bssh_key_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/ssh_keys/{project_id}/{ssh_key_id}'].patch.parameters[0].schema"
    """

    shared_in_project: Required[bool]
    """
    '#/components/schemas/ShareSSHKeySerializer/properties/shared_in_project'
    "$.components.schemas.ShareSSHKeySerializer.properties.shared_in_project"
    """
