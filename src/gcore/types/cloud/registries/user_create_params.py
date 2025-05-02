# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    duration: Required[int]
    """User account operating time, days"""

    name: Required[str]
    """A name for the registry user.

    Should be in lowercase, consisting only of numbers and letters,

    with maximum length of 16 characters
    """

    read_only: bool
    """Read-only user"""

    secret: str
    """User secret"""
