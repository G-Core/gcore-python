# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Metrics", "Disk"]


class Disk(BaseModel):
    """Disk metrics item"""

    disk_bps_read: Optional[float] = FieldInfo(alias="disk_Bps_read", default=None)
    """Disk read, Bytes per second.

    The value is null if there is no data for this disk.
    """

    disk_bps_write: Optional[float] = FieldInfo(alias="disk_Bps_write", default=None)
    """Disk write, Bytes per second.

    The value is null if there is no data for this disk.
    """

    disk_iops_read: Optional[float] = None
    """Disk read, iops. The value is null if there is no data for this disk."""

    disk_iops_write: Optional[float] = None
    """Disk write, iops. The value is null if there is no data for this disk."""

    disk_name: Optional[str] = None
    """Disk attached slot name. The value is null if the name is unknown."""


class Metrics(BaseModel):
    """Instance metrics item"""

    cpu_util: Optional[float] = None
    """CPU utilization, % (max 100% for multi-core).

    The value is null if there is no data for this time.
    """

    disks: Optional[List[Disk]] = None
    """Disks metrics for each of the disks attached.

    The value is null if there is no disk data for this time.
    """

    memory_util: Optional[float] = None
    """RAM utilization, %. The value is null if there is no data for this time."""

    network_bps_egress: Optional[float] = FieldInfo(alias="network_Bps_egress", default=None)
    """
    Network out, bits per second (the 'Bps' in the field name is historical; the
    value is bits, not bytes). The value is null if there is no data for this time.
    """

    network_bps_ingress: Optional[float] = FieldInfo(alias="network_Bps_ingress", default=None)
    """
    Network in, bits per second (the 'Bps' in the field name is historical; the
    value is bits, not bytes). The value is null if there is no data for this time.
    """

    network_pps_egress: Optional[float] = None
    """Network out, packets per second.

    The value is null if there is no data for this time.
    """

    network_pps_ingress: Optional[float] = None
    """Network in, packets per second.

    The value is null if there is no data for this time.
    """

    time: str
    """Timestamp"""
