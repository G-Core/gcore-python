# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecurityGroupUpdateParams", "ChangedRule"]


class SecurityGroupUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bgroup_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bgroup_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}'].patch.parameters[1].schema"
    """

    changed_rules: Iterable[ChangedRule]
    """
    '#/components/schemas/UpdateSecurityGroupSerializer/properties/changed_rules'
    "$.components.schemas.UpdateSecurityGroupSerializer.properties.changed_rules"
    """

    name: str
    """
    '#/components/schemas/UpdateSecurityGroupSerializer/properties/name'
    "$.components.schemas.UpdateSecurityGroupSerializer.properties.name"
    """


class ChangedRule(TypedDict, total=False):
    action: Required[Literal["create", "delete"]]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/action'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.action"
    """

    description: str
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/description'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.description"
    """

    direction: Literal["egress", "ingress"]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/direction'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.direction"
    """

    ethertype: Optional[Literal["IPv4", "IPv6"]]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/ethertype/anyOf/0'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.ethertype.anyOf[0]"
    """

    port_range_max: int
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/port_range_max'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.port_range_max"
    """

    port_range_min: int
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/port_range_min'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.port_range_min"
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
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/protocol'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.protocol"
    """

    remote_group_id: Optional[str]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/remote_group_id/anyOf/0'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.remote_group_id.anyOf[0]"
    """

    remote_ip_prefix: Optional[str]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/remote_ip_prefix/anyOf/0'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.remote_ip_prefix.anyOf[0]"
    """

    security_group_rule_id: Optional[str]
    """
    '#/components/schemas/UpdateSecurityGroupRuleSerializer/properties/security_group_rule_id/anyOf/0'
    "$.components.schemas.UpdateSecurityGroupRuleSerializer.properties.security_group_rule_id.anyOf[0]"
    """
