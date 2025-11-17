# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from ..tag_update_map_param import TagUpdateMapParam

__all__ = ["SubnetUpdateParams", "HostRoute"]


class SubnetUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    dns_nameservers: Optional[SequenceNotStr[str]]
    """List IP addresses of DNS servers to advertise via DHCP."""

    enable_dhcp: Optional[bool]
    """True if DHCP should be enabled"""

    gateway_ip: Optional[str]
    """Default GW IPv4 address to advertise in DHCP routes in this subnet.

    Omit this field to let the cloud backend allocate it automatically. Set to null
    if no gateway must be advertised by this subnet's DHCP (useful when attaching
    instances to multiple subnets in order to prevent default route conflicts).
    """

    host_routes: Optional[Iterable[HostRoute]]
    """List of custom static routes to advertise via DHCP."""

    name: Optional[str]
    """Name"""

    tags: Optional[TagUpdateMapParam]
    """Update key-value tags using JSON Merge Patch semantics (RFC 7386).

    Provide key-value pairs to add or update tags. Set tag values to `null` to
    remove tags. Unspecified tags remain unchanged. Read-only tags are always
    preserved and cannot be modified.

    **Examples:**

    - **Add/update tags:**
      `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
      updates existing ones.

    - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.

    - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
      tags are preserved).

    - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
      specified tags.

    - **Mixed operations:**
      `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
      adds/updates 'environment' and '`cost_center`' while removing
      '`deprecated_tag`', preserving other existing tags.

    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class HostRoute(TypedDict, total=False):
    destination: Required[str]
    """CIDR of destination IPv4 subnet."""

    nexthop: Required[str]
    """
    IPv4 address to forward traffic to if it's destination IP matches 'destination'
    CIDR.
    """
