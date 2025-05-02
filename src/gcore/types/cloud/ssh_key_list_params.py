# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SSHKeyListParams"]


class SSHKeyListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    limit: int
    """Maximum number of SSH keys to return"""

    offset: int
    """Offset for pagination"""

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]
    """Sort order for the SSH keys"""
