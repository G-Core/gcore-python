# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["VodTotalStreamDurationSeries", "VodTotalStreamDurationSeriesItem"]


class VodTotalStreamDurationSeriesItem(BaseModel):
    client: int

    duration: int
    """count of minutes"""

    client_user_id: Optional[int] = None

    stream_id: Optional[str] = None


VodTotalStreamDurationSeries: TypeAlias = List[VodTotalStreamDurationSeriesItem]
