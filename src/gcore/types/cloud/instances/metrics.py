# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Metrics", "Disk"]


class Disk(BaseModel):
    disk_bps_read: Optional[float] = FieldInfo(alias="disk_Bps_read", default=None)
    """Disk read, Bytes per second"""

    disk_bps_write: Optional[float] = FieldInfo(alias="disk_Bps_write", default=None)
    """Disk write, Bytes per second"""

    disk_iops_read: Optional[float] = None
    """Disk read, iops"""

    disk_iops_write: Optional[float] = None
    """Disk write, iops"""

    disk_name: Optional[str] = None
    """Disk attached slot name"""


class Metrics(BaseModel):
    time: str
    """Timestamp"""

    cpu_util: Optional[float] = None
    """CPU utilization, % (max 100% for multi-core)"""

    disks: Optional[List[Disk]] = None
    """Disks metrics for each of the disks attached"""

    memory_util: Optional[float] = None
    """RAM utilization, %"""

    network_bps_egress: Optional[float] = FieldInfo(alias="network_Bps_egress", default=None)
    """Network out, bytes per second"""

    network_bps_ingress: Optional[float] = FieldInfo(alias="network_Bps_ingress", default=None)
    """Network in, bytes per second"""

    network_pps_egress: Optional[float] = None
    """Network out, packets per second"""

    network_pps_ingress: Optional[float] = None
    """Network in, packets per second"""
