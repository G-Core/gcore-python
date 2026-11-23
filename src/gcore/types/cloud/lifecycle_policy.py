# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "LifecyclePolicy",
    "Schedule",
    "ScheduleGetCronScheduleSerializer",
    "ScheduleGetCronScheduleSerializerRetentionTime",
    "ScheduleGetIntervalScheduleSerializer",
    "ScheduleGetIntervalScheduleSerializerRetentionTime",
    "Volume",
]


class ScheduleGetCronScheduleSerializerRetentionTime(BaseModel):
    """Time after which the resource will be deleted.

    The value is null if no retention is set.
    """

    days: Optional[int] = None
    """Number of days to wait.

    The value is null if the retention time does not set days.
    """

    hours: Optional[int] = None
    """Number of hours to wait.

    The value is null if the retention time does not set hours.
    """

    minutes: Optional[int] = None
    """Number of minutes to wait.

    The value is null if the retention time does not set minutes.
    """

    weeks: Optional[int] = None
    """Number of weeks to wait.

    The value is null if the retention time does not set weeks.
    """


class ScheduleGetCronScheduleSerializer(BaseModel):
    id: str
    """Schedule ID"""

    day: Optional[str] = None
    """Day of the month (1-31, '\\**') or a comma-separated list of days.

    The value is null if the schedule does not set a day.
    """

    day_of_week: Optional[str] = None
    """Weekday or a comma-separated list of weekdays (mon,tue,wed,thu,fri,sat,sun,\\**).

    The value is null if the schedule does not set a weekday.
    """

    hour: Optional[str] = None
    """Hour (0-23, '\\**') or a comma-separated list of hours.

    The value is null if the schedule does not set an hour.
    """

    max_quantity: int
    """Number of stored resources."""

    minute: Optional[str] = None
    """Minute (0-59, '\\**') or a comma-separated list of minutes.

    The value is null if the schedule does not set a minute.
    """

    month: Optional[str] = None
    """Month (1-12, '\\**') or a comma-separated list of months.

    The value is null if the schedule does not set a month.
    """

    owner: str
    """Schedule owner"""

    owner_id: int
    """Owner ID"""

    resource_name_template: Optional[str] = None
    """Template for resource names. The value is null if the schedule has no template."""

    retention_time: Optional[ScheduleGetCronScheduleSerializerRetentionTime] = None
    """Time after which the resource will be deleted.

    The value is null if no retention is set.
    """

    timezone: Optional[str] = None
    """A timezone name, for example Europe/Berlin.

    The value is null if the schedule does not set a timezone, and it then uses UTC.
    """

    type: Literal["cron"]
    """Schedule type"""

    user_id: int
    """User ID"""

    week: Optional[str] = None
    """ISO week (1-53, '\\**') or a comma-separated list of weeks.

    The value is null if the schedule does not set a week.
    """


class ScheduleGetIntervalScheduleSerializerRetentionTime(BaseModel):
    """Time after which the resource will be deleted.

    The value is null if no retention is set.
    """

    days: Optional[int] = None
    """Number of days to wait.

    The value is null if the retention time does not set days.
    """

    hours: Optional[int] = None
    """Number of hours to wait.

    The value is null if the retention time does not set hours.
    """

    minutes: Optional[int] = None
    """Number of minutes to wait.

    The value is null if the retention time does not set minutes.
    """

    weeks: Optional[int] = None
    """Number of weeks to wait.

    The value is null if the retention time does not set weeks.
    """


class ScheduleGetIntervalScheduleSerializer(BaseModel):
    id: str
    """Schedule ID"""

    days: Optional[int] = None
    """Number of days to wait. The value is null if the schedule does not set days."""

    hours: Optional[int] = None
    """Number of hours to wait. The value is null if the schedule does not set hours."""

    max_quantity: int
    """Number of stored resources."""

    minutes: Optional[int] = None
    """Number of minutes to wait.

    The value is null if the schedule does not set minutes.
    """

    owner: str
    """Schedule owner"""

    owner_id: int
    """Owner ID"""

    resource_name_template: Optional[str] = None
    """Template for resource names. The value is null if the schedule has no template."""

    retention_time: Optional[ScheduleGetIntervalScheduleSerializerRetentionTime] = None
    """Time after which the resource will be deleted.

    The value is null if no retention is set.
    """

    type: Literal["interval"]
    """Schedule type"""

    user_id: int
    """User ID"""

    weeks: Optional[int] = None
    """Number of weeks to wait. The value is null if the schedule does not set weeks."""


Schedule: TypeAlias = Annotated[
    Union[ScheduleGetCronScheduleSerializer, ScheduleGetIntervalScheduleSerializer], PropertyInfo(discriminator="type")
]


class Volume(BaseModel):
    volume_id: str
    """Unique identifier of the volume."""

    volume_name: str
    """Name of the volume."""


class LifecyclePolicy(BaseModel):
    id: int
    """Unique identifier for the policy."""

    action: str
    """Action associated with the lifecycle policy."""

    name: str
    """Name of the policy."""

    project_id: int
    """Project ID associated with the policy."""

    region_id: int
    """Region ID where the policy is applied."""

    schedules: List[Schedule]
    """List of schedules within the policy."""

    status: Literal["active", "paused"]
    """Status of the lifecycle policy."""

    user_id: int
    """User ID of the creator of the policy."""

    volumes: List[Volume]
    """Data of volumes that should be reserved.

    Displayed only when the query parameter is specified.
    """
