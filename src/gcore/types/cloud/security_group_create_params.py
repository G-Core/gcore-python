# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecurityGroupCreateParams", "SecurityGroup", "SecurityGroupSecurityGroupRule"]


class SecurityGroupCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    security_group: Required[SecurityGroup]
    """Security group"""

    instances: List[str]
    """List of instances"""


class SecurityGroupSecurityGroupRule(TypedDict, total=False):
    description: str
    """Rule description"""

    direction: Literal["egress", "ingress"]
    """
    Ingress or egress, which is the direction in which the security group is applied
    """

    ethertype: Literal["IPv4", "IPv6"]
    """Ether type"""

    port_range_max: Optional[int]
    """The maximum port number in the range that is matched by the security group rule"""

    port_range_min: Optional[int]
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
    """The remote group UUID to associate with this security group"""

    remote_ip_prefix: Optional[str]
    """The remote IP prefix that is matched by this security group rule"""


class SecurityGroup(TypedDict, total=False):
    name: Required[str]
    """Security group name"""

    description: Optional[str]
    """Security group description"""

    security_group_rules: Iterable[SecurityGroupSecurityGroupRule]
    """Security group rules"""

    tags: Dict[str, object]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
