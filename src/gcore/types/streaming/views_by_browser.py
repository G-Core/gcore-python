# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByBrowser", "Data"]


class Data(BaseModel):
    browser: str

    views: int


class ViewsByBrowser(BaseModel):
    data: Optional[List[Data]] = None
