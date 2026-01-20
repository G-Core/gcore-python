# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .tag_update_map_param import TagUpdateMapParam

__all__ = ["SecurityGroupUpdateParams", "Rule"]


class SecurityGroupUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    description: str
    """Security group description"""

    name: str
    """Name"""

    rules: Iterable[Rule]
    """Security group rules"""

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
      adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
      preserving other existing tags.
    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class Rule(TypedDict, total=False):
    description: str
    """Security grpup rule description"""

    direction: Literal["egress", "ingress"]
    """
    Ingress or egress, which is the direction in which the security group rule is
    applied
    """

    ethertype: Literal["IPv4", "IPv6"]
    """
    Must be IPv4 or IPv6, and addresses represented in CIDR must match the ingress
    or egress rules.
    """

    port_range_max: int
    """The maximum port number in the range that is matched by the security group rule"""

    port_range_min: int
    """The minimum port number in the range that is matched by the security group rule"""

    protocol: Literal[
        "ah",
        "any",
        "dccp",
        "egp",
        "esp",
        "gre",
        "icmp",
        "igmp",
        "ipencap",
        "ipip",
        "ipv6-encap",
        "ipv6-frag",
        "ipv6-icmp",
        "ipv6-nonxt",
        "ipv6-opts",
        "ipv6-route",
        "ospf",
        "pgm",
        "rsvp",
        "sctp",
        "tcp",
        "udp",
        "udplite",
        "vrrp",
    ]
    """Protocol"""

    remote_group_id: str
    """The remote group UUID to associate with this security group rule"""

    remote_ip_prefix: str
    """The remote IP prefix that is matched by this security group rule"""
