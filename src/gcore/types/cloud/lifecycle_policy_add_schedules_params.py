# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "LifecyclePolicyAddSchedulesParams",
    "Schedule",
    "ScheduleCreateCronScheduleSerializer",
    "ScheduleCreateCronScheduleSerializerRetentionTime",
    "ScheduleCreateIntervalScheduleSerializer",
    "ScheduleCreateIntervalScheduleSerializerRetentionTime",
]


class LifecyclePolicyAddSchedulesParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    schedules: Required[Iterable[Schedule]]
    """List of schedules associated with the policy."""


class ScheduleCreateCronScheduleSerializerRetentionTime(TypedDict, total=False):
    """Time after which the resource will be deleted"""

    days: int
    """Number of days to wait"""

    hours: int
    """Number of hours to wait"""

    minutes: int
    """Number of minutes to wait"""

    weeks: int
    """Number of weeks to wait"""


class ScheduleCreateCronScheduleSerializer(TypedDict, total=False):
    type: Required[Literal["cron"]]
    """Schedule type"""

    day: str
    """Day of the month (1-31, '\\**') or a comma-separated list of days"""

    day_of_week: str
    """Weekday or a comma-separated list of weekdays (mon,tue,wed,thu,fri,sat,sun,\\**)"""

    hour: str
    """Hour (0-23, '\\**') or a comma-separated list of hours"""

    max_quantity: int
    """Number of stored resources."""

    minute: str
    """Minute (0-59, '\\**') or a comma-separated list of minutes"""

    month: str
    """Month (1-12, '\\**') or a comma-separated list of months"""

    resource_name_template: str
    """Template for resource names."""

    retention_time: ScheduleCreateCronScheduleSerializerRetentionTime
    """Time after which the resource will be deleted"""

    timezone: str
    """A pytz timezone. Defaults to UTC."""

    week: str
    """ISO week (1-53, '\\**') or a comma-separated list of weeks"""


class ScheduleCreateIntervalScheduleSerializerRetentionTime(TypedDict, total=False):
    """Time after which the resource will be deleted"""

    days: int
    """Number of days to wait"""

    hours: int
    """Number of hours to wait"""

    minutes: int
    """Number of minutes to wait"""

    weeks: int
    """Number of weeks to wait"""


class ScheduleCreateIntervalScheduleSerializer(TypedDict, total=False):
    type: Required[Literal["interval"]]
    """Schedule type"""

    days: int
    """Number of days to wait"""

    hours: int
    """Number of hours to wait"""

    max_quantity: int
    """Number of stored resources."""

    minutes: int
    """Number of minutes to wait"""

    resource_name_template: str
    """Template for resource names."""

    retention_time: ScheduleCreateIntervalScheduleSerializerRetentionTime
    """Time after which the resource will be deleted"""

    weeks: int
    """Number of weeks to wait"""


Schedule: TypeAlias = Union[ScheduleCreateCronScheduleSerializer, ScheduleCreateIntervalScheduleSerializer]
