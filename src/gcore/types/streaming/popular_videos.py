# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PopularVideos", "Data"]


class Data(BaseModel):
    id: str

    views: int


class PopularVideos(BaseModel):
    data: Optional[List[Data]] = None
