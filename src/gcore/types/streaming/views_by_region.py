# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByRegion", "Data"]


class Data(BaseModel):
    region: str

    region_name: str

    views: int


class ViewsByRegion(BaseModel):
    data: Optional[List[Data]] = None
