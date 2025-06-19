# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ServerListParams"]


class ServerListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    changes_before: Annotated[Union[str, datetime], PropertyInfo(alias="changes-before", format="iso8601")]
    """Filters the instances by a date and time stamp when the instances last changed."""

    changes_since: Annotated[Union[str, datetime], PropertyInfo(alias="changes-since", format="iso8601")]
    """
    Filters the instances by a date and time stamp when the instances last changed
    status.
    """

    flavor_id: str
    """Filter out instances by `flavor_id`. Flavor id must match exactly."""

    flavor_prefix: str
    """Filter out instances by `flavor_prefix`."""

    include_k8s: bool
    """Include managed k8s worker nodes"""

    ip: str
    """An IPv4 address to filter results by.

    Note: partial matches are allowed. For example, searching for 192.168.0.1 will
    return 192.168.0.1, 192.168.0.10, 192.168.0.110, and so on.
    """

    limit: int
    """Optional. Limit the number of returned items"""

    name: str
    """Filter instances by name.

    You can provide a full or partial name, instances with matching names will be
    returned. For example, entering 'test' will return all instances that contain
    'test' in their name.
    """

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    only_isolated: bool
    """Include only isolated instances"""

    only_with_fixed_external_ip: bool
    """Return bare metals only with external fixed IP addresses."""

    order_by: Literal["created.asc", "created.desc", "name.asc", "name.desc", "status.asc", "status.desc"]
    """Order by field and direction."""

    profile_name: str
    """Filter result by ddos protection profile name.

    Effective only with `with_ddos` set to true.
    """

    protection_status: Literal["Active", "Queued", "Error"]
    """Filter result by DDoS `protection_status`.

    Effective only with `with_ddos` set to true. (Active, Queued or Error)
    """

    status: Literal["ACTIVE", "BUILD", "ERROR", "HARD_REBOOT", "REBOOT", "REBUILD", "RESCUE", "SHUTOFF", "SUSPENDED"]
    """Filters instances by a server status, as a string."""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""

    tag_value: List[str]
    """Optional. Filter by tag values. ?`tag_value`=value1&`tag_value`=value2"""

    type_ddos_profile: Literal["basic", "advanced"]
    """Return bare metals either only with advanced or only basic DDoS protection.

    Effective only with `with_ddos` set to true. (advanced or basic)
    """

    uuid: str
    """Filter the server list result by the UUID of the server. Allowed UUID part"""

    with_ddos: bool
    """
    Include DDoS profile information for bare-metal servers in the response when set
    to `true`. Otherwise, the `ddos_profile` field in the response is `null` by
    default.
    """

    with_interfaces_name: bool
    """Include `interface_name` in the addresses"""
