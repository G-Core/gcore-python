# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByOperatingSystem", "Data"]


class Data(BaseModel):
    os: str

    views: int


class ViewsByOperatingSystem(BaseModel):
    data: Optional[List[Data]] = None
