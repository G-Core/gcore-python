# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UsageTotal", "Data", "DataMetrics"]


class DataMetrics(BaseModel):
    file_quantity_sum_max: Optional[int] = None
    """a FileQuantitySumMax is max sum of files quantity for grouped period"""

    requests_in_sum: Optional[int] = None
    """a RequestsInSum is sum of incoming requests for grouped period"""

    requests_out_edges_sum: Optional[int] = None
    """a RequestsOutEdgesSum is sum of out edges requests for grouped period"""

    requests_out_wo_edges_sum: Optional[int] = None
    """a RequestsOutWoEdgesSum is sum of out no edges requests for grouped period"""

    requests_sum: Optional[int] = None
    """a RequestsSum is sum of all requests for grouped period"""

    size_sum_bytes_hour: Optional[int] = None
    """a SizeSumBytesHour is sum of bytes hour for grouped period"""

    size_sum_max: Optional[int] = None
    """a SizeSumMax is max sum of all files sizes for grouped period"""

    size_sum_mean: Optional[int] = None
    """a SizeSumMean is mean sum of all files sizes for grouped period"""

    traffic_in_sum: Optional[int] = None
    """a TrafficInSum is sum of incoming traffic for grouped period"""

    traffic_out_edges_sum: Optional[int] = None
    """a TrafficOutEdgesSum is sum of out edges traffic for grouped period"""

    traffic_out_wo_edges_sum: Optional[int] = None
    """a TrafficOutWoEdgesSum is sum of out no edges traffic for grouped period"""

    traffic_sum: Optional[int] = None
    """a TrafficSum is sum of all traffic for grouped period"""


class Data(BaseModel):
    """StorageStatsTotalElement for response"""

    metrics: Optional[DataMetrics] = None


class UsageTotal(BaseModel):
    data: Optional[List[Data]] = None
    """StorageUsageTotalRes for response"""
