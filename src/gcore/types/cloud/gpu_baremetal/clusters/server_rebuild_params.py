# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerRebuildParams"]


class ServerRebuildParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_id: Required[str]
    """Cluster unique identifier"""

    image_id: str
    """New or existing image to rebuild the node with.

    Omit to keep the cluster's current image.
    """

    ssh_key_name: str
    """New or existing SSH keypair name. Omit to keep the cluster's current SSH key."""

    user_data: str
    """New or existing user data (Base64-encoded).

    Omit to keep the cluster's current user data.
    """
