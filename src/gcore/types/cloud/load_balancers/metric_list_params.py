# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..instance_metrics_time_unit import InstanceMetricsTimeUnit

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    time_interval: Required[int]
    """Time interval"""

    time_unit: Required[InstanceMetricsTimeUnit]
    """Time interval unit"""
