# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectReplaceParams"]


class ProjectReplaceParams(TypedDict, total=False):
    project_id: int

    name: Required[str]
    """Name of the entity, following a specific format."""

    description: Optional[str]
    """Description of the project."""
