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
    """Time after which the resource will be deleted"""

    days: Optional[int] = None
    """Number of days to wait"""

    hours: Optional[int] = None
    """Number of hours to wait"""

    minutes: Optional[int] = None
    """Number of minutes to wait"""

    weeks: Optional[int] = None
    """Number of weeks to wait"""


class ScheduleGetCronScheduleSerializer(BaseModel):
    id: str
    """Schedule ID"""

    max_quantity: int
    """Number of stored resources."""

    owner: str
    """Schedule owner"""

    owner_id: int
    """Owner ID"""

    retention_time: Optional[ScheduleGetCronScheduleSerializerRetentionTime] = None
    """Time after which the resource will be deleted"""

    type: Literal["cron"]
    """Schedule type"""

    user_id: int
    """User ID"""

    day: Optional[str] = None
    """Day of the month (1-31, '\\**') or a comma-separated list of days"""

    day_of_week: Optional[str] = None
    """Weekday or a comma-separated list of weekdays (mon,tue,wed,thu,fri,sat,sun,\\**)"""

    hour: Optional[str] = None
    """Hour (0-23, '\\**') or a comma-separated list of hours"""

    minute: Optional[str] = None
    """Minute (0-59, '\\**') or a comma-separated list of minutes"""

    month: Optional[str] = None
    """Month (1-12, '\\**') or a comma-separated list of months"""

    resource_name_template: Optional[str] = None
    """Template for resource names"""

    timezone: Optional[str] = None
    """A pytz timezone. Defaults to UTC."""

    week: Optional[str] = None
    """ISO week (1-53, '\\**') or a comma-separated list of weeks"""


class ScheduleGetIntervalScheduleSerializerRetentionTime(BaseModel):
    """Time after which the resource will be deleted"""

    days: Optional[int] = None
    """Number of days to wait"""

    hours: Optional[int] = None
    """Number of hours to wait"""

    minutes: Optional[int] = None
    """Number of minutes to wait"""

    weeks: Optional[int] = None
    """Number of weeks to wait"""


class ScheduleGetIntervalScheduleSerializer(BaseModel):
    id: str
    """Schedule ID"""

    max_quantity: int
    """Number of stored resources."""

    owner: str
    """Schedule owner"""

    owner_id: int
    """Owner ID"""

    retention_time: Optional[ScheduleGetIntervalScheduleSerializerRetentionTime] = None
    """Time after which the resource will be deleted"""

    type: Literal["interval"]
    """Schedule type"""

    user_id: int
    """User ID"""

    days: Optional[int] = None
    """Number of days to wait"""

    hours: Optional[int] = None
    """Number of hours to wait"""

    minutes: Optional[int] = None
    """Number of minutes to wait"""

    resource_name_template: Optional[str] = None
    """Template for resource names"""

    weeks: Optional[int] = None
    """Number of weeks to wait"""


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
