# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsHeatmap", "Data"]


class Data(BaseModel):
    viewers: int

    seconds: Optional[int] = None

    time: Optional[str] = None


class ViewsHeatmap(BaseModel):
    data: Optional[List[Data]] = None
