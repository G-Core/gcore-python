# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .cdn_metrics_groups import CdnMetricsGroups
from .cdn_metrics_values import CdnMetricsValues

__all__ = ["CdnMetrics", "Data"]

Data: TypeAlias = Union[CdnMetricsValues, CdnMetricsGroups]


class CdnMetrics(BaseModel):
    data: Optional[Data] = None
    """
    If no grouping was requested then "data" holds an array of metric values. If at
    least one field is specified in "`group_by`" then "data" is an object whose
    properties are groups, which may include other groups; the last group will hold
    array of metrics values.
    """
