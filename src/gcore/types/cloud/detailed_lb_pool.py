# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .lb_algorithm import LbAlgorithm
from .lb_pool_protocol import LbPoolProtocol
from .lb_health_monitor import LbHealthMonitor
from .provisioning_status import ProvisioningStatus
from .lb_session_persistence import LbSessionPersistence
from .detailed_lb_pool_member import DetailedLbPoolMember
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["DetailedLbPool", "Listener", "Loadbalancer"]


class Listener(BaseModel):
    id: str
    """Resource ID"""


class Loadbalancer(BaseModel):
    id: str
    """Resource ID"""


class DetailedLbPool(BaseModel):
    id: str
    """Pool ID"""

    ca_secret_id: Optional[str] = None
    """Secret ID of CA certificate bundle"""

    crl_secret_id: Optional[str] = None
    """Secret ID of CA revocation list file"""

    lb_algorithm: LbAlgorithm
    """Load balancer algorithm"""

    listeners: List[Listener]
    """Listeners IDs"""

    loadbalancers: List[Loadbalancer]
    """Load balancers IDs"""

    members: List[DetailedLbPoolMember]
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

    session_persistence: Optional[LbSessionPersistence] = None
    """Session persistence parameters"""

    timeout_client_data: Optional[int] = None
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int] = None
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int] = None
    """Backend member inactivity timeout in milliseconds"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    healthmonitor: Optional[LbHealthMonitor] = None
    """Health monitor parameters"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
