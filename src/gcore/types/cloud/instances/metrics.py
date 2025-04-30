# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Metrics", "Disk"]


class Disk(BaseModel):
    disk_bps_read: Optional[float] = FieldInfo(alias="disk_Bps_read", default=None)
    """
    '#/components/schemas/DisksMetrics/properties/disk_Bps_read/anyOf/0'
    "$.components.schemas.DisksMetrics.properties.disk_Bps_read.anyOf[0]"
    """

    disk_bps_write: Optional[float] = FieldInfo(alias="disk_Bps_write", default=None)
    """
    '#/components/schemas/DisksMetrics/properties/disk_Bps_write/anyOf/0'
    "$.components.schemas.DisksMetrics.properties.disk_Bps_write.anyOf[0]"
    """

    disk_iops_read: Optional[float] = None
    """
    '#/components/schemas/DisksMetrics/properties/disk_iops_read/anyOf/0'
    "$.components.schemas.DisksMetrics.properties.disk_iops_read.anyOf[0]"
    """

    disk_iops_write: Optional[float] = None
    """
    '#/components/schemas/DisksMetrics/properties/disk_iops_write/anyOf/0'
    "$.components.schemas.DisksMetrics.properties.disk_iops_write.anyOf[0]"
    """

    disk_name: Optional[str] = None
    """
    '#/components/schemas/DisksMetrics/properties/disk_name/anyOf/0'
    "$.components.schemas.DisksMetrics.properties.disk_name.anyOf[0]"
    """


class Metrics(BaseModel):
    time: str
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/time'
    "$.components.schemas.InstanceMetricsSerializer.properties.time"
    """

    cpu_util: Optional[float] = None
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/cpu_util/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.cpu_util.anyOf[0]"
    """

    disks: Optional[List[Disk]] = None
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/disks/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.disks.anyOf[0]"
    """

    memory_util: Optional[float] = None
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/memory_util/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.memory_util.anyOf[0]"
    """

    network_bps_egress: Optional[float] = FieldInfo(alias="network_Bps_egress", default=None)
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/network_Bps_egress/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.network_Bps_egress.anyOf[0]"
    """

    network_bps_ingress: Optional[float] = FieldInfo(alias="network_Bps_ingress", default=None)
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/network_Bps_ingress/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.network_Bps_ingress.anyOf[0]"
    """

    network_pps_egress: Optional[float] = None
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/network_pps_egress/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.network_pps_egress.anyOf[0]"
    """

    network_pps_ingress: Optional[float] = None
    """
    '#/components/schemas/InstanceMetricsSerializer/properties/network_pps_ingress/anyOf/0'
    "$.components.schemas.InstanceMetricsSerializer.properties.network_pps_ingress.anyOf[0]"
    """
