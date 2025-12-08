# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WaapTaskID"]


class WaapTaskID(BaseModel):
    """Response model for the task result ID"""

    id: str
    """The task ID"""
