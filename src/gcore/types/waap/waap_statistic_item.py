# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["WaapStatisticItem"]


class WaapStatisticItem(BaseModel):
    date_time: datetime
    """The date and time for the statistic in ISO 8601 format"""

    value: int
    """The value for the statistic.

    If there is no data for the given time, the value will be 0.
    """
