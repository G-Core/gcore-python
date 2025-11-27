# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .lb_listener_protocol import LbListenerProtocol
from .load_balancer_statistics import LoadBalancerStatistics
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["LoadBalancerListenerDetail", "UserList"]


class UserList(BaseModel):
    encrypted_password: str
    """Encrypted password to auth via Basic Authentication"""

    username: str
    """Username to auth via Basic Authentication"""


class LoadBalancerListenerDetail(BaseModel):
    id: str
    """Load balancer listener ID"""

    allowed_cidrs: Optional[List[str]] = None
    """Network CIDRs from which service will be accessible"""

    connection_limit: int
    """Limit of simultaneous connections"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    insert_headers: Dict[str, object]
    """Dictionary of additional header insertion into HTTP headers.

    Only used with HTTP and `TERMINATED_HTTPS` protocols.
    """

    load_balancer_id: Optional[str] = None
    """Load balancer ID"""

    name: str
    """Load balancer listener name"""

    operating_status: LoadBalancerOperatingStatus
    """Listener operating status"""

    pool_count: Optional[int] = None
    """Number of pools (for UI)"""

    protocol: LbListenerProtocol
    """Load balancer protocol"""

    protocol_port: int
    """Protocol port"""

    provisioning_status: ProvisioningStatus
    """Listener lifecycle status"""

    secret_id: Optional[str] = None
    """
    ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
    PROMETHEUS load balancer
    """

    sni_secret_id: Optional[List[str]] = None
    """
    List of secret's ID containing PKCS12 format certificate/key bundles for
    `TERMINATED_HTTPS` or PROMETHEUS listeners
    """

    stats: Optional[LoadBalancerStatistics] = None
    """Statistics of the load balancer.

    It is available only in get functions by a flag.
    """

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

    user_list: List[UserList]
    """Load balancer listener users list"""
