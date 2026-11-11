# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InstanceRebuildParams"]


class InstanceRebuildParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    image_id: str
    """Image ID. If you omit it, the instance keeps the current image."""

    ssh_key_name: Optional[str]
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    Use null to remove the SSH key from the instance. If you omit it, the instance
    keeps the current SSH key.
    """

    user_data: str
    """String in base64 format.

    Examples of the `user_data`:
    https://cloudinit.readthedocs.io/en/latest/topics/examples.html. If you omit it,
    the instance keeps the current user data.
    """
