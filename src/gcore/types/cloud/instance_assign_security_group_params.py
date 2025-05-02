# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["InstanceAssignSecurityGroupParams", "PortsSecurityGroupName"]


class InstanceAssignSecurityGroupParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: str
    """Security group name, applies to all ports"""

    ports_security_group_names: Iterable[PortsSecurityGroupName]
    """Port security groups mapping"""


class PortsSecurityGroupName(TypedDict, total=False):
    port_id: Required[Optional[str]]
    """Port ID. If None, security groups will be applied to all ports"""

    security_group_names: Required[List[str]]
    """List of security group names"""
