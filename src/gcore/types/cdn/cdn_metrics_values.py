# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CdnMetricsValues", "CdnMetricsValueItem"]


class CdnMetricsValueItem(BaseModel):
    metric: Optional[float] = None
    """Metrics value."""

    timestamp: Optional[int] = None
    """Start timestamp of interval."""


CdnMetricsValues: TypeAlias = List[CdnMetricsValueItem]
