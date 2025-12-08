# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..logging import Logging
from ...._models import BaseModel
from .clusters.k8s_cluster_pool import K8SClusterPool

__all__ = [
    "K8SCluster",
    "AddOns",
    "AddOnsSlurm",
    "Csi",
    "CsiNfs",
    "Authentication",
    "AuthenticationOidc",
    "Cni",
    "CniCilium",
    "DDOSProfile",
    "DDOSProfileField",
]


class AddOnsSlurm(BaseModel):
    """Slurm add-on configuration"""

    enabled: bool
    """Indicates whether Slurm add-on is deployed in the cluster.

    This add-on is only supported in clusters running Kubernetes v1.31 and v1.32
    with at least 1 GPU cluster pool.
    """

    file_share_id: Optional[str] = None
    """ID of a VAST file share used as Slurm storage.

    The Slurm add-on creates separate Persistent Volume Claims for different
    purposes (controller spool, worker spool, jail) on that file share.
    """

    ssh_key_ids: Optional[List[str]] = None
    """IDs of SSH keys authorized for SSH connection to Slurm login nodes."""

    worker_count: Optional[int] = None
    """Size of the worker pool, i.e. number of worker nodes.

    Each Slurm worker node is backed by a Pod scheduled on one of cluster's GPU
    nodes.
    """


class AddOns(BaseModel):
    """Cluster add-ons configuration"""

    slurm: AddOnsSlurm
    """Slurm add-on configuration"""


class CsiNfs(BaseModel):
    """NFS settings"""

    vast_enabled: bool
    """Indicates the status of VAST NFS integration"""


class Csi(BaseModel):
    """Cluster CSI settings"""

    nfs: CsiNfs
    """NFS settings"""


class AuthenticationOidc(BaseModel):
    """OIDC authentication settings"""

    client_id: Optional[str] = None
    """Client ID"""

    groups_claim: Optional[str] = None
    """JWT claim to use as the user's group"""

    groups_prefix: Optional[str] = None
    """Prefix prepended to group claims"""

    issuer_url: Optional[str] = None
    """Issuer URL"""

    required_claims: Optional[Dict[str, str]] = None
    """Key-value pairs that describe required claims in the token"""

    signing_algs: Optional[
        List[Literal["ES256", "ES384", "ES512", "PS256", "PS384", "PS512", "RS256", "RS384", "RS512"]]
    ] = None
    """Accepted signing algorithms"""

    username_claim: Optional[str] = None
    """JWT claim to use as the user name"""

    username_prefix: Optional[str] = None
    """Prefix prepended to username claims to prevent clashes"""


class Authentication(BaseModel):
    """Cluster authentication settings"""

    kubeconfig_created_at: Optional[datetime] = None
    """Kubeconfig creation date"""

    kubeconfig_expires_at: Optional[datetime] = None
    """Kubeconfig expiration date"""

    oidc: Optional[AuthenticationOidc] = None
    """OIDC authentication settings"""


class CniCilium(BaseModel):
    """Cilium settings"""

    encryption: Optional[bool] = None
    """Wireguard encryption"""

    hubble_relay: Optional[bool] = None
    """Hubble Relay"""

    hubble_ui: Optional[bool] = None
    """Hubble UI"""

    lb_acceleration: Optional[bool] = None
    """LoadBalancer acceleration"""

    lb_mode: Optional[Literal["dsr", "hybrid", "snat"]] = None
    """LoadBalancer mode"""

    mask_size: Optional[int] = None
    """Mask size for IPv4"""

    mask_size_v6: Optional[int] = None
    """Mask size for IPv6"""

    routing_mode: Optional[Literal["native", "tunnel"]] = None
    """Routing mode"""

    tunnel: Optional[Literal["", "geneve", "vxlan"]] = None
    """CNI provider"""


class Cni(BaseModel):
    """Cluster CNI settings"""

    cilium: Optional[CniCilium] = None
    """Cilium settings"""

    provider: Optional[Literal["calico", "cilium"]] = None
    """CNI provider"""


class DDOSProfileField(BaseModel):
    base_field: int

    field_value: Optional[object] = None
    """Complex value. Only one of 'value' or '`field_value`' must be specified"""

    value: Optional[str] = None
    """Basic value. Only one of 'value' or '`field_value`' must be specified"""


class DDOSProfile(BaseModel):
    """Advanced DDoS Protection profile"""

    enabled: bool
    """Enable advanced DDoS protection"""

    fields: Optional[List[DDOSProfileField]] = None
    """DDoS profile parameters"""

    profile_template: Optional[int] = None
    """DDoS profile template ID"""

    profile_template_name: Optional[str] = None
    """DDoS profile template name"""


class K8SCluster(BaseModel):
    id: str
    """Cluster pool uuid"""

    add_ons: AddOns
    """Cluster add-ons configuration"""

    created_at: str
    """Function creation date"""

    csi: Csi
    """Cluster CSI settings"""

    is_public: bool
    """Cluster is public"""

    keypair: str
    """Keypair"""

    logging: Optional[Logging] = None
    """Logging configuration"""

    name: str
    """Name"""

    pools: List[K8SClusterPool]
    """pools"""

    status: Literal["Deleting", "Provisioned", "Provisioning"]
    """Status"""

    version: str
    """K8s version"""

    authentication: Optional[Authentication] = None
    """Cluster authentication settings"""

    autoscaler_config: Optional[Dict[str, str]] = None
    """Cluster autoscaler configuration.

    It contains overrides to the default cluster-autoscaler parameters provided by
    the platform.
    """

    cni: Optional[Cni] = None
    """Cluster CNI settings"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    ddos_profile: Optional[DDOSProfile] = None
    """Advanced DDoS Protection profile"""

    fixed_network: Optional[str] = None
    """Fixed network id"""

    fixed_subnet: Optional[str] = None
    """Fixed subnet id"""

    is_ipv6: Optional[bool] = None
    """Enable public v6 address"""

    pods_ip_pool: Optional[str] = None
    """The IP pool for the pods"""

    pods_ipv6_pool: Optional[str] = None
    """The IPv6 pool for the pods"""

    services_ip_pool: Optional[str] = None
    """The IP pool for the services"""

    services_ipv6_pool: Optional[str] = None
    """The IPv6 pool for the services"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
