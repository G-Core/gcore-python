# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]
    """Unique project name for a client. Each client always has one "default" project."""

    client_id: Optional[int]
    """ID associated with the client."""

    description: Optional[str]
    """Description of the project."""

    state: Optional[str]
    """State of the project."""
