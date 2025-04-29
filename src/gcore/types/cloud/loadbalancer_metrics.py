# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoadbalancerMetrics"]


class LoadbalancerMetrics(BaseModel):
    cpu_util: Optional[float] = None
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/cpu_util/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.cpu_util.anyOf[0]"
    """

    memory_util: Optional[float] = None
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/memory_util/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.memory_util.anyOf[0]"
    """

    network_bps_egress: Optional[float] = FieldInfo(alias="network_Bps_egress", default=None)
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/network_Bps_egress/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.network_Bps_egress.anyOf[0]"
    """

    network_bps_ingress: Optional[float] = FieldInfo(alias="network_Bps_ingress", default=None)
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/network_Bps_ingress/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.network_Bps_ingress.anyOf[0]"
    """

    network_pps_egress: Optional[float] = None
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/network_pps_egress/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.network_pps_egress.anyOf[0]"
    """

    network_pps_ingress: Optional[float] = None
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/network_pps_ingress/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.network_pps_ingress.anyOf[0]"
    """

    time: Optional[str] = None
    """
    '#/components/schemas/LoadbalancerMetricsSerializer/properties/time/anyOf/0'
    "$.components.schemas.LoadbalancerMetricsSerializer.properties.time.anyOf[0]"
    """
