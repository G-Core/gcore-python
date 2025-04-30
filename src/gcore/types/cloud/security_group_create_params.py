# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecurityGroupCreateParams", "SecurityGroup", "SecurityGroupSecurityGroupRule"]


class SecurityGroupCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/securitygroups/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsecuritygroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/securitygroups/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    security_group: Required[SecurityGroup]
    """
    '#/components/schemas/CreateSecurityGroupSerializer/properties/security_group'
    "$.components.schemas.CreateSecurityGroupSerializer.properties.security_group"
    """

    instances: List[str]
    """
    '#/components/schemas/CreateSecurityGroupSerializer/properties/instances'
    "$.components.schemas.CreateSecurityGroupSerializer.properties.instances"
    """


class SecurityGroupSecurityGroupRule(TypedDict, total=False):
    description: str
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/description'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.description"
    """

    direction: Literal["egress", "ingress"]
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/direction'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.direction"
    """

    ethertype: Literal["IPv4", "IPv6"]
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/ethertype'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.ethertype"
    """

    port_range_max: Optional[int]
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/port_range_max/anyOf/0'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.port_range_max.anyOf[0]"
    """

    port_range_min: Optional[int]
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/port_range_min/anyOf/0'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.port_range_min.anyOf[0]"
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
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/protocol'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.protocol"
    """

    remote_group_id: str
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/remote_group_id'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.remote_group_id"
    """

    remote_ip_prefix: Optional[str]
    """
    '#/components/schemas/CreateSecurityGroupRuleSerializer/properties/remote_ip_prefix/anyOf/0'
    "$.components.schemas.CreateSecurityGroupRuleSerializer.properties.remote_ip_prefix.anyOf[0]"
    """


class SecurityGroup(TypedDict, total=False):
    name: Required[str]
    """
    '#/components/schemas/SingleCreateSecurityGroupSerializer/properties/name'
    "$.components.schemas.SingleCreateSecurityGroupSerializer.properties.name"
    """

    description: Optional[str]
    """
    '#/components/schemas/SingleCreateSecurityGroupSerializer/properties/description/anyOf/0'
    "$.components.schemas.SingleCreateSecurityGroupSerializer.properties.description.anyOf[0]"
    """

    security_group_rules: Iterable[SecurityGroupSecurityGroupRule]
    """
    '#/components/schemas/SingleCreateSecurityGroupSerializer/properties/security_group_rules'
    "$.components.schemas.SingleCreateSecurityGroupSerializer.properties.security_group_rules"
    """

    tags: Dict[str, object]
    """
    '#/components/schemas/SingleCreateSecurityGroupSerializer/properties/tags'
    "$.components.schemas.SingleCreateSecurityGroupSerializer.properties.tags"
    """
