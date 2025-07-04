# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MemberAddParams"]


class MemberAddParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    address: Required[str]
    """Member IP address"""

    protocol_port: Required[int]
    """Member IP port"""

    admin_state_up: Optional[bool]
    """Administrative state of the resource.

    When set to true, the resource is enabled and operational. When set to false,
    the resource is disabled and will not process traffic. When null is passed, the
    value is skipped and defaults to true.
    """

    instance_id: Optional[str]
    """Either `subnet_id` or `instance_id` should be provided"""

    monitor_address: Optional[str]
    """An alternate IP address used for health monitoring of a backend member.

    Default is null which monitors the member address.
    """

    monitor_port: Optional[int]
    """An alternate protocol port used for health monitoring of a backend member.

    Default is null which monitors the member `protocol_port`.
    """

    subnet_id: Optional[str]
    """Either `subnet_id` or `instance_id` should be provided"""

    weight: Optional[int]
    """Member weight. Valid values: 0 to 256, defaults to 1"""
