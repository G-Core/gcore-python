# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["UsageSeries", "Clients", "ClientsLocations", "ClientsLocationsStorages"]


class ClientsLocationsStorages(BaseModel):
    buckets_series: Optional[Dict[str, List[List[object]]]] = None
    """
    a BucketsSeries is max bucket files count for grouped period
    {name:[[timestamp, count]]}
    """

    file_quantity_sum_max: Optional[int] = None
    """a FileQuantitySumMax is max sum of files quantity for grouped period"""

    name: Optional[str] = None
    """a Name of storage"""

    requests_in_series: Optional[List[List[object]]] = None
    """
    a RequestsInSeries is sum of incoming requests for grouped period
    [[timestamp, count]]
    """

    requests_in_sum: Optional[int] = None
    """a RequestsInSum is sum of incoming requests for grouped period"""

    requests_out_edges_series: Optional[List[List[object]]] = None
    """
    a RequestsOutWoEdgesSeries is sum of out requests (only edges) for grouped
    period [[timestamp, count]]
    """

    requests_out_edges_sum: Optional[int] = None
    """a RequestsOutEdgesSum is sum of out edges requests for grouped period"""

    requests_out_wo_edges_series: Optional[List[List[object]]] = None
    """
    a RequestsOutWoEdgesSeries is sum of out requests (without edges) for grouped
    period [[timestamp, count]]
    """

    requests_out_wo_edges_sum: Optional[int] = None
    """a RequestsOutWoEdgesSum is sum of out no edges requests for grouped period"""

    requests_series: Optional[List[List[object]]] = None
    """a RequestsSeries is sum of out requests for grouped period [[timestamp, count]]"""

    requests_sum: Optional[int] = None
    """a RequestsSum is sum of all requests for grouped period"""

    size_bytes_hour_series: Optional[List[List[object]]] = None
    """
    a SizeBytesHourSeries is value that displays how many bytes were stored per hour
    [[timestamp, count]]
    """

    size_max_series: Optional[List[List[object]]] = None
    """a SizeMaxSeries is max of files size for grouped period [[timestamp, count]]"""

    size_mean_series: Optional[List[List[object]]] = None
    """a SizeMeanSeries is mean of files size for grouped period [[timestamp, count]]"""

    size_sum_bytes_hour: Optional[int] = None
    """a SizeSumBytesHour is sum of bytes hour for grouped period"""

    size_sum_max: Optional[int] = None
    """a SizeSumMax is max sum of all files sizes for grouped period"""

    size_sum_mean: Optional[int] = None
    """a SizeSumMean is mean sum of all files sizes for grouped period"""

    traffic_in_series: Optional[List[List[object]]] = None
    """
    a TrafficInSeries is sum of incoming traffic bytes for grouped period
    [[timestamp, count]]
    """

    traffic_in_sum: Optional[int] = None
    """a TrafficInSum is sum of incoming traffic for grouped period"""

    traffic_out_edges_series: Optional[List[List[object]]] = None
    """
    a TrafficOutWoEdgesSeries is sum of out traffic bytes (only edges) for grouped
    period [[timestamp, count]]
    """

    traffic_out_edges_sum: Optional[int] = None
    """a TrafficOutEdgesSum is sum of out edges traffic for grouped period"""

    traffic_out_wo_edges_series: Optional[List[List[object]]] = None
    """
    a TrafficOutWoEdgesSeries is sum of out traffic bytes (without edges) for
    grouped period [[timestamp, count]]
    """

    traffic_out_wo_edges_sum: Optional[int] = None
    """a TrafficOutWoEdgesSum is sum of out no edges traffic for grouped period"""

    traffic_series: Optional[List[List[object]]] = None
    """a TrafficSeries is sum of traffic bytes for grouped period [[timestamp, count]]"""

    traffic_sum: Optional[int] = None
    """a TrafficSum is sum of all traffic for grouped period"""


class ClientsLocations(BaseModel):
    file_quantity_sum_max: Optional[int] = None
    """a FileQuantitySumMax is max sum of files quantity for grouped period"""

    name: Optional[str] = None
    """a Name of location"""

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

    storages: Optional[Dict[str, ClientsLocationsStorages]] = None
    """a Storages grouped data"""

    traffic_in_sum: Optional[int] = None
    """a TrafficInSum is sum of incoming traffic for grouped period"""

    traffic_out_edges_sum: Optional[int] = None
    """a TrafficOutEdgesSum is sum of out edges traffic for grouped period"""

    traffic_out_wo_edges_sum: Optional[int] = None
    """a TrafficOutWoEdgesSum is sum of out no edges traffic for grouped period"""

    traffic_sum: Optional[int] = None
    """a TrafficSum is sum of all traffic for grouped period"""


class Clients(BaseModel):
    id: Optional[int] = None
    """an ID of client"""

    file_quantity_sum_max: Optional[int] = None
    """a FileQuantitySumMax is max sum of files quantity for grouped period"""

    locations: Optional[Dict[str, ClientsLocations]] = None
    """a Locations grouped data"""

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


class UsageSeries(BaseModel):
    clients: Optional[Dict[str, Clients]] = None
    """a Clients grouped data"""
