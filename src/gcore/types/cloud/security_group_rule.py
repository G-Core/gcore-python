# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SecurityGroupRule"]


class SecurityGroupRule(BaseModel):
    id: str
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/id'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/created_at'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.created_at"
    """

    direction: Literal["egress", "ingress"]
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/direction'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.direction"
    """

    revision_number: int
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/revision_number'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.revision_number"
    """

    security_group_id: str
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/security_group_id'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.security_group_id"
    """

    updated_at: datetime
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/updated_at'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.updated_at"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/description/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.description.anyOf[0]"
    """

    ethertype: Optional[Literal["IPv4", "IPv6"]] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/ethertype/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.ethertype.anyOf[0]"
    """

    port_range_max: Optional[int] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/port_range_max/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.port_range_max.anyOf[0]"
    """

    port_range_min: Optional[int] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/port_range_min/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.port_range_min.anyOf[0]"
    """

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
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/protocol/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.protocol.anyOf[0]"
    """

    remote_group_id: Optional[str] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/remote_group_id/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.remote_group_id.anyOf[0]"
    """

    remote_ip_prefix: Optional[str] = None
    """
    '#/components/schemas/SecurityGroupRuleSerializer/properties/remote_ip_prefix/anyOf/0'
    "$.components.schemas.SecurityGroupRuleSerializer.properties.remote_ip_prefix.anyOf[0]"
    """
