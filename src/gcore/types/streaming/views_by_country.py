# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ViewsByCountry", "Data"]


class Data(BaseModel):
    country: str

    country_name: str

    views: int


class ViewsByCountry(BaseModel):
    data: Optional[List[Data]] = None
