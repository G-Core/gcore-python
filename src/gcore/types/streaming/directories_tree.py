# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .directory_base import DirectoryBase

__all__ = ["DirectoriesTree", "Tree"]


class Tree(DirectoryBase):
    descendants: Optional[List["DirectoriesTree"]] = None
    """Array of subdirectories, if any."""


class DirectoriesTree(BaseModel):
    tree: Optional[List[Tree]] = None
