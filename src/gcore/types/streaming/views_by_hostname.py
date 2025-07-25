# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByHostname", "Data"]


class Data(BaseModel):
    host: str

    views: int


class ViewsByHostname(BaseModel):
    data: Optional[List[Data]] = None
