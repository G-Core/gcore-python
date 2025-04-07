# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .project import Project
from ..._models import BaseModel

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[Project]
    """Objects"""
