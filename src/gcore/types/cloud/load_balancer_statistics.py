# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["LoadBalancerStatistics"]


class LoadBalancerStatistics(BaseModel):
    active_connections: int
    """
    '#/components/schemas/LoadbalancerStatsSerializer/properties/active_connections'
    "$.components.schemas.LoadbalancerStatsSerializer.properties.active_connections"
    """

    bytes_in: int
    """
    '#/components/schemas/LoadbalancerStatsSerializer/properties/bytes_in'
    "$.components.schemas.LoadbalancerStatsSerializer.properties.bytes_in"
    """

    bytes_out: int
    """
    '#/components/schemas/LoadbalancerStatsSerializer/properties/bytes_out'
    "$.components.schemas.LoadbalancerStatsSerializer.properties.bytes_out"
    """

    request_errors: int
    """
    '#/components/schemas/LoadbalancerStatsSerializer/properties/request_errors'
    "$.components.schemas.LoadbalancerStatsSerializer.properties.request_errors"
    """

    total_connections: int
    """
    '#/components/schemas/LoadbalancerStatsSerializer/properties/total_connections'
    "$.components.schemas.LoadbalancerStatsSerializer.properties.total_connections"
    """
