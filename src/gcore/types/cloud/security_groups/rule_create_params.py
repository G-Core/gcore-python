# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

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
