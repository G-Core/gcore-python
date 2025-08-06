# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["IPInfoGetTopURLsResponse", "IPInfoGetTopURLsResponseItem"]


class IPInfoGetTopURLsResponseItem(BaseModel):
    count: int
    """The number of attacks to the URL"""

    url: str
    """The URL that was attacked"""


IPInfoGetTopURLsResponse: TypeAlias = List[IPInfoGetTopURLsResponseItem]
