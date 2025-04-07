# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["V1DeleteResponse"]


class V1DeleteResponse(BaseModel):
    tasks: Optional[List[str]] = None
    """Task list"""
