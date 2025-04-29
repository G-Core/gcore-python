# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..instance_metrics_time_unit import InstanceMetricsTimeUnit

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fmetrics/post/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/metrics'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fmetrics/post/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/metrics'].post.parameters[1].schema"
    """

    time_interval: Required[int]
    """
    '#/components/schemas/LoadbalancerMetricsRequestSerializer/properties/time_interval'
    "$.components.schemas.LoadbalancerMetricsRequestSerializer.properties.time_interval"
    """

    time_unit: Required[InstanceMetricsTimeUnit]
    """
    '#/components/schemas/LoadbalancerMetricsRequestSerializer/properties/time_unit'
    "$.components.schemas.LoadbalancerMetricsRequestSerializer.properties.time_unit"
    """
