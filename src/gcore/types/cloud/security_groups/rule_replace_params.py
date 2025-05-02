# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleReplaceParams"]


class RuleReplaceParams(TypedDict, total=False):
    project_id: int

    region_id: int

    direction: Required[Literal["egress", "ingress"]]
    """
    Ingress or egress, which is the direction in which the security group rule is
    applied
    """

    security_group_id: Required[str]
    """Parent security group of this rule"""

    description: str
    """Rule description"""

    ethertype: Optional[Literal["IPv4", "IPv6"]]
    """
    Must be IPv4 or IPv6, and addresses represented in CIDR must match the ingress
    or egress rules.
    """

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

    remote_group_id: Optional[str]
    """The remote group UUID to associate with this security group rule"""

    remote_ip_prefix: Optional[str]
    """The remote IP prefix that is matched by this security group rule"""
