# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .loadbalancer_metrics import LoadbalancerMetrics

__all__ = ["LoadbalancerMetricsList"]


class LoadbalancerMetricsList(BaseModel):
    count: int
    """
    '#/components/schemas/LoadbalancerMetricsSerializerList/properties/count'
    "$.components.schemas.LoadbalancerMetricsSerializerList.properties.count"
    """

    results: List[LoadbalancerMetrics]
    """
    '#/components/schemas/LoadbalancerMetricsSerializerList/properties/results'
    "$.components.schemas.LoadbalancerMetricsSerializerList.properties.results"
    """
