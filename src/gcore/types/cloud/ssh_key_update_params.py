# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHKeyUpdateParams"]


class SSHKeyUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    shared_in_project: Required[bool]
    """Share your ssh key with all users in the project"""
