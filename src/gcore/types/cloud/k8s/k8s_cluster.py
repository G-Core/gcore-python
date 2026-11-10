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
    "Authentication",
    "AuthenticationOidc",
    "Cni",
    "CniCilium",
    "Csi",
    "CsiNfs",
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

    Null when the add-on is disabled.
    """

    ssh_key_ids: Optional[List[str]] = None
    """IDs of SSH keys authorized for SSH connection to Slurm login nodes.

    Null when the add-on is disabled.
    """

    worker_count: Optional[int] = None
    """Size of the worker pool, i.e. number of worker nodes.

    Each Slurm worker node is backed by a Pod scheduled on one of cluster's GPU
    nodes.

    Note: Downscaling (reducing worker count) is not supported.

    Null when the add-on is disabled.
    """


class AddOns(BaseModel):
    """Cluster add-ons configuration"""

    slurm: AddOnsSlurm
    """Slurm add-on configuration"""


class AuthenticationOidc(BaseModel):
    """OIDC authentication settings. Null when OIDC authentication is not configured"""

    client_id: Optional[str] = None
    """Client ID. Null when not set"""

    groups_claim: Optional[str] = None
    """JWT claim to use as the user's group. Null when not set"""

    groups_prefix: Optional[str] = None
    """Prefix prepended to group claims. Null when not set"""

    issuer_url: Optional[str] = None
    """Issuer URL. Null when not set"""

    required_claims: Optional[Dict[str, str]] = None
    """Key-value pairs that describe required claims in the token. Null when not set"""

    signing_algs: Optional[
        List[Literal["ES256", "ES384", "ES512", "PS256", "PS384", "PS512", "RS256", "RS384", "RS512"]]
    ] = None
    """Accepted signing algorithms. Null when not set"""

    username_claim: Optional[str] = None
    """JWT claim to use as the user name. Null when not set"""

    username_prefix: Optional[str] = None
    """Prefix prepended to username claims to prevent clashes. Null when not set"""


class Authentication(BaseModel):
    """Cluster authentication settings.

    Null when the cluster has no authentication settings
    """

    kubeconfig_created_at: Optional[datetime] = None
    """Kubeconfig creation date. Null until the cluster creates its kubeconfig"""

    kubeconfig_expires_at: Optional[datetime] = None
    """Kubeconfig expiration date. Null until the cluster creates its kubeconfig"""

    oidc: Optional[AuthenticationOidc] = None
    """OIDC authentication settings. Null when OIDC authentication is not configured"""


class CniCilium(BaseModel):
    """Cilium settings. Null when the CNI provider is not Cilium"""

    cni_exclusive: bool
    """Whether Cilium manages networking exclusively.

    Set to `false` to allow other CNI components to coexist with Cilium.
    """

    encryption: bool
    """Wireguard encryption"""

    hubble_relay: bool
    """Hubble Relay"""

    hubble_ui: bool
    """Hubble UI"""

    lb_acceleration: bool
    """LoadBalancer acceleration"""

    lb_mode: Literal["dsr", "hybrid", "snat"]
    """LoadBalancer mode"""

    mask_size: int
    """Mask size for IPv4"""

    mask_size_v6: int
    """Mask size for IPv6"""

    routing_mode: Literal["native", "tunnel"]
    """Routing mode"""

    tunnel: Literal["", "geneve", "vxlan"]
    """CNI provider"""


class Cni(BaseModel):
    """Cluster CNI settings. Null when the cluster does not report its CNI settings"""

    cilium: Optional[CniCilium] = None
    """Cilium settings. Null when the CNI provider is not Cilium"""

    provider: Literal["calico", "cilium"]
    """CNI provider"""


class CsiNfs(BaseModel):
    """NFS settings"""

    ddn_enabled: bool
    """Whether DDN (Lustre) integration is enabled.

    When `true`, the DDN EXAScaler CSI driver is deployed in the cluster and each
    DDN file share defined in the cloud is exposed as a dedicated StorageClass.
    """

    vast_enabled: bool
    """Indicates the status of VAST NFS integration"""


class Csi(BaseModel):
    """Cluster CSI settings"""

    nfs: CsiNfs
    """NFS settings"""


class DDOSProfileField(BaseModel):
    base_field: int

    field_value: object
    """Complex value for the DDoS profile field. Null when the field has a basic value"""


class DDOSProfile(BaseModel):
    """Advanced DDoS Protection profile. Null when the cluster has no DDoS profile"""

    enabled: bool
    """Enable advanced DDoS protection"""

    fields: Optional[List[DDOSProfileField]] = None
    """DDoS profile parameters. Null when the profile has no parameters"""

    profile_template: Optional[int] = None
    """DDoS profile template ID. Null when not set"""

    profile_template_name: Optional[str] = None
    """DDoS profile template name. Null when not set"""


class K8SCluster(BaseModel):
    id: str
    """Cluster pool uuid"""

    add_ons: AddOns
    """Cluster add-ons configuration"""

    authentication: Optional[Authentication] = None
    """Cluster authentication settings.

    Null when the cluster has no authentication settings
    """

    autoscaler_config: Dict[str, str]
    """Cluster autoscaler configuration.

    It contains overrides to the default cluster-autoscaler parameters provided by
    the platform.
    """

    cni: Optional[Cni] = None
    """Cluster CNI settings. Null when the cluster does not report its CNI settings"""

    created_at: str
    """Function creation date"""

    creator_task_id: Optional[str] = None
    """Task that created this entity. Null when no record of that task exists"""

    csi: Csi
    """Cluster CSI settings"""

    ddos_profile: Optional[DDOSProfile] = None
    """Advanced DDoS Protection profile. Null when the cluster has no DDoS profile"""

    fixed_network: str
    """Fixed network id. An empty string when not set"""

    fixed_subnet: str
    """Fixed subnet id. An empty string when not set"""

    is_ipv6: bool
    """Enable public v6 address"""

    is_public: bool
    """Cluster is public"""

    keypair: str
    """Keypair"""

    logging: Optional[Logging] = None
    """Logging configuration"""

    name: str
    """Name"""

    pods_ip_pool: str
    """The IP pool for the pods"""

    pods_ipv6_pool: Optional[str] = None
    """The IPv6 pool for the pods. Null when `is_ipv6` is false"""

    pools: List[K8SClusterPool]
    """pools"""

    services_ip_pool: str
    """The IP pool for the services"""

    services_ipv6_pool: Optional[str] = None
    """The IPv6 pool for the services. Null when `is_ipv6` is false"""

    status: Literal["Deleting", "Failed", "Pending", "Provisioned", "Provisioning", "Unknown"]
    """Status"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    version: str
    """K8s version"""
