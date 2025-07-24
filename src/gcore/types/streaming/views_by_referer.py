# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByReferer", "Data"]


class Data(BaseModel):
    embed_url: str

    views: int


class ViewsByReferer(BaseModel):
    data: Optional[List[Data]] = None
