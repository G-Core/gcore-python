# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .cdn_metrics_values import CDNMetricsValues

__all__ = ["CDNMetricsGroups"]


class CDNMetricsGroups(BaseModel):
    group: Optional[CDNMetricsValues] = None
    """List of requested metrics sorted by timestamp in ascending order."""
