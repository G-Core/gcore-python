# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_status import LoadBalancerStatus

__all__ = ["LoadBalancerStatusList"]


class LoadBalancerStatusList(BaseModel):
    count: int
    """
    '#/components/schemas/LoadBalancerStatusSerializerList/properties/count'
    "$.components.schemas.LoadBalancerStatusSerializerList.properties.count"
    """

    results: List[LoadBalancerStatus]
    """
    '#/components/schemas/LoadBalancerStatusSerializerList/properties/results'
    "$.components.schemas.LoadBalancerStatusSerializerList.properties.results"
    """
