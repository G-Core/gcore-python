# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["DurationStats"]


class DurationStats(BaseModel):
    avg: int
    """Average duration in usec"""

    max: int
    """Max duration in usec"""

    median: int
    """Median (50% percentile) duration in usec"""

    min: int
    """Min duration in usec"""

    perc75: int
    """75% percentile duration in usec"""

    perc90: int
    """90% percentile duration in usec"""

    time: datetime
    """Beginning ot reporting slot"""
