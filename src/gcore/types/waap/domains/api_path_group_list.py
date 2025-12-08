# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["APIPathGroupList"]


class APIPathGroupList(BaseModel):
    """Response model for the API path groups"""

    api_path_groups: List[str]
    """An array of api groups associated with the API path"""
