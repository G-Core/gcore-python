# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["VolumeType", "Capabilities", "Qos"]


class Capabilities(BaseModel):
    """Operations that a volume of this type supports."""

    attachable_to_boot: bool
    """A volume of this type can be the boot volume of an instance.

    The instance flavor can add more limits.
    """

    resizable: bool
    """A volume of this type can increase in size.

    Without `region_id`, the value ignores region limits. A region can set it to
    false.
    """

    retypable: bool
    """
    A volume of this type can change to a different retypable type, and the reverse.
    """

    snapshottable: bool
    """A volume of this type can have snapshots."""


class Qos(BaseModel):
    """QoS profile of a volume type.

    The base limit of a volume is the integer part of its size in GiB multiplied by the per-GiB rate.
    The minimum and maximum values limit the result.
    The burst limit is the base limit multiplied by `burst_ratio`. The maximum value limits the result.
    """

    bandwidth_max_mb_per_sec: int
    """Highest base and burst bandwidth limit in megabytes per second."""

    bandwidth_mb_per_sec_per_gib: float
    """Base bandwidth in megabytes per second for each GiB of volume size."""

    bandwidth_min_mb_per_sec: int
    """Lowest base bandwidth limit in megabytes per second."""

    burst_ratio: float
    """Burst limit divided by base limit."""

    iops_max: int
    """Highest base and burst IOPS limit."""

    iops_min: int
    """Lowest base IOPS limit."""

    iops_per_gib: float
    """Base IOPS for each GiB of volume size."""


class VolumeType(BaseModel):
    capabilities: Capabilities
    """Operations that a volume of this type supports."""

    name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type name."""

    qos: Optional[Qos] = None
    """QoS profile of a volume type.

    The base limit of a volume is the integer part of its size in GiB multiplied by
    the per-GiB rate. The minimum and maximum values limit the result. The burst
    limit is the base limit multiplied by `burst_ratio`. The maximum value limits
    the result.
    """
