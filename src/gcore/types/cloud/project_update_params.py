# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    description: str
    """Description of the project."""

    name: str
    """Name of the entity, following a specific format."""
