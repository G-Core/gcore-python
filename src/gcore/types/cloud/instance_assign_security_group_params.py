# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["InstanceAssignSecurityGroupParams", "PortsSecurityGroupName"]


class InstanceAssignSecurityGroupParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faddsecuritygroup/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/addsecuritygroup'].post.parameters[1].schema"
    """

    name: str
    """
    '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/name'
    "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.name"
    """

    ports_security_group_names: Iterable[PortsSecurityGroupName]
    """
    '#/components/schemas/InstancePortsSecurityGroupsSchema/properties/ports_security_group_names'
    "$.components.schemas.InstancePortsSecurityGroupsSchema.properties.ports_security_group_names"
    """


class PortsSecurityGroupName(TypedDict, total=False):
    port_id: Required[Optional[str]]
    """
    '#/components/schemas/PortSecurityGroupNamesSchema/properties/port_id'
    "$.components.schemas.PortSecurityGroupNamesSchema.properties.port_id"
    """

    security_group_names: Required[List[str]]
    """
    '#/components/schemas/PortSecurityGroupNamesSchema/properties/security_group_names'
    "$.components.schemas.PortSecurityGroupNamesSchema.properties.security_group_names"
    """
