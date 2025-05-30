# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .member import Member
from ..._models import BaseModel
from .lb_algorithm import LbAlgorithm
from .health_monitor import HealthMonitor
from .lb_pool_protocol import LbPoolProtocol
from .provisioning_status import ProvisioningStatus
from .session_persistence import SessionPersistence
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["LoadBalancerPool", "Listener", "Loadbalancer"]


class Listener(BaseModel):
    id: str
    """Resource ID"""


class Loadbalancer(BaseModel):
    id: str
    """Resource ID"""


class LoadBalancerPool(BaseModel):
    id: str
    """Pool ID"""

    ca_secret_id: Optional[str] = None
    """Secret ID of CA certificate bundle"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    crl_secret_id: Optional[str] = None
    """Secret ID of CA revocation list file"""

    healthmonitor: Optional[HealthMonitor] = None
    """Health monitor parameters"""

    lb_algorithm: LbAlgorithm
    """Load balancer algorithm"""

    listeners: List[Listener]
    """Listeners IDs"""

    loadbalancers: List[Loadbalancer]
    """Load balancers IDs"""

    members: List[Member]
    """Pool members"""

    name: str
    """Pool name"""

    operating_status: LoadBalancerOperatingStatus
    """Pool operating status"""

    protocol: LbPoolProtocol
    """Protocol"""

    provisioning_status: ProvisioningStatus
    """Pool lifecycle status"""

    secret_id: Optional[str] = None
    """Secret ID for TLS client authentication to the member servers"""

    session_persistence: Optional[SessionPersistence] = None
    """Session persistence parameters"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    timeout_client_data: Optional[int] = None
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int] = None
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int] = None
    """Backend member inactivity timeout in milliseconds"""
