# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["StatisticGetVodWatchTimeTotalCdnResponse", "StatisticGetVodWatchTimeTotalCdnResponseItem"]


class StatisticGetVodWatchTimeTotalCdnResponseItem(BaseModel):
    client: int

    duration: int
    """count of minutes"""

    client_user_id: Optional[int] = None

    slug: Optional[str] = None


StatisticGetVodWatchTimeTotalCdnResponse: TypeAlias = List[StatisticGetVodWatchTimeTotalCdnResponseItem]
