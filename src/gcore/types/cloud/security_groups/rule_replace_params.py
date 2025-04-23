# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleReplaceParams"]


class RuleReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygrouprules%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brule_id%7D/put/parameters/0/schema'
    "$.paths['/cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}'].put.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygrouprules%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brule_id%7D/put/parameters/1/schema'
    "$.paths['/cloud/v1/securitygrouprules/{project_id}/{region_id}/{rule_id}'].put.parameters[1].schema"
    """

    direction: Required[Literal["egress", "ingress"]]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/direction'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.direction"
    """

    security_group_id: Required[str]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/security_group_id'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.security_group_id"
    """

    description: str
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/description'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.description"
    """

    ethertype: Optional[Literal["IPv4", "IPv6"]]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/ethertype/anyOf/0'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.ethertype.anyOf[0]"
    """

    port_range_max: Optional[int]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/port_range_max/anyOf/0'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.port_range_max.anyOf[0]"
    """

    port_range_min: Optional[int]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/port_range_min/anyOf/0'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.port_range_min.anyOf[0]"
    """

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
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/protocol'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.protocol"
    """

    remote_group_id: Optional[str]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/remote_group_id/anyOf/0'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.remote_group_id.anyOf[0]"
    """

    remote_ip_prefix: Optional[str]
    """
    '#/components/schemas/ChangeSecurityGroupRuleSerializer/properties/remote_ip_prefix/anyOf/0'
    "$.components.schemas.ChangeSecurityGroupRuleSerializer.properties.remote_ip_prefix.anyOf[0]"
    """
