# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapClearLocalTagsResponse"]


class WaapClearLocalTagsResponse(BaseModel):
    num_cleared: Optional[int] = None
    """The number of items affected by the action"""
