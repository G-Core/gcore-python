# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SecurityGroupRule"]


class SecurityGroupRule(BaseModel):
    id: str
    """The ID of the security group rule"""

    created_at: datetime
    """Datetime when the rule was created"""

    direction: Literal["egress", "ingress"]
    """
    Ingress or egress, which is the direction in which the security group rule is
    applied
    """

    revision_number: int
    """The revision number of the resource"""

    security_group_id: str
    """The security group ID to associate with this security group rule"""

    updated_at: datetime
    """Datetime when the rule was last updated"""

    description: Optional[str] = None
    """Rule description"""

    ethertype: Optional[Literal["IPv4", "IPv6"]] = None
    """
    Must be IPv4 or IPv6, and addresses represented in CIDR must match the ingress
    or egress rules.
    """

    port_range_max: Optional[int] = None
    """The maximum port number in the range that is matched by the security group rule"""

    port_range_min: Optional[int] = None
    """The minimum port number in the range that is matched by the security group rule"""

    protocol: Optional[
        Literal[
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
    ] = None
    """Protocol"""

    remote_group_id: Optional[str] = None
    """The remote group UUID to associate with this security group rule"""

    remote_ip_prefix: Optional[str] = None
    """The remote IP prefix that is matched by this security group rule"""
