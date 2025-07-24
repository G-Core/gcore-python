# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UniqueViewersCdn", "Data"]


class Data(BaseModel):
    type: str

    uniqs: int


class UniqueViewersCdn(BaseModel):
    data: Optional[List[Data]] = None
