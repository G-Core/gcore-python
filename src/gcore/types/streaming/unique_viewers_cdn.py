# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UniqueViewersCDN", "Data"]


class Data(BaseModel):
    type: str

    uniqs: int


class UniqueViewersCDN(BaseModel):
    data: Optional[List[Data]] = None
