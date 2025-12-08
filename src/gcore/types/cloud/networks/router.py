# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..route import Route
from ...._models import BaseModel
from ..ip_assignment import IPAssignment

__all__ = ["Router", "Interface", "ExternalGatewayInfo"]


class Interface(BaseModel):
    ip_assignments: List[IPAssignment]
    """IP addresses assigned to this port"""

    network_id: str
    """ID of the network the port is attached to"""

    port_id: str
    """ID of virtual ethernet port object"""

    mac_address: Optional[str] = None
    """MAC address of the virtual port"""


class ExternalGatewayInfo(BaseModel):
    """State of this router's external gateway."""

    enable_snat: bool
    """Is SNAT enabled."""

    external_fixed_ips: List[IPAssignment]
    """List of external IPs that emit SNAT-ed traffic."""

    network_id: str
    """Id of the external network."""


class Router(BaseModel):
    id: str
    """Router ID"""

    created_at: datetime
    """Datetime when the router was created"""

    distributed: bool
    """Whether the router is distributed or centralized."""

    interfaces: List[Interface]
    """List of router interfaces."""

    name: str
    """Router name"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    routes: List[Route]
    """List of custom routes."""

    status: str
    """Status of the router."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: datetime
    """Datetime when the router was last updated"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    external_gateway_info: Optional[ExternalGatewayInfo] = None
    """State of this router's external gateway."""
