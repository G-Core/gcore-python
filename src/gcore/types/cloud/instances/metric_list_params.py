# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..instance_metrics_time_unit import InstanceMetricsTimeUnit

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    time_interval: Required[int]
    """Length of the time range, in the `time_unit`.

    The range is 1, 6 or 24 hours, or 1, 7 or 14 days.
    """

    time_unit: Required[InstanceMetricsTimeUnit]
    """Unit of the `time_interval`."""

    limit: int
    """Max items to return."""

    offset: int
    """Items to skip."""
