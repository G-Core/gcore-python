# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .cdn_metrics_groups import CDNMetricsGroups
from .cdn_metrics_values import CDNMetricsValues

__all__ = ["CDNMetrics", "Data"]

Data: TypeAlias = Union[CDNMetricsValues, CDNMetricsGroups]


class CDNMetrics(BaseModel):
    data: Optional[Data] = None
    """
    If no grouping was requested then "data" holds an array of metric values. If at
    least one field is specified in "group_by" then "data" is an object whose
    properties are groups, which may include other groups; the last group will hold
    array of metrics values.
    """
