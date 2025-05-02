# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["TaskIDList"]


class TaskIDList(BaseModel):
    tasks: List[str]
    """List of task IDs"""
