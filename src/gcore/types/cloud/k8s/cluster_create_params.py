# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr
from ..laas_index_retention_policy_param import LaasIndexRetentionPolicyParam

__all__ = [
    "ClusterCreateParams",
    "Pool",
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
    "Logging",
]


class ClusterCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    keypair: Required[str]
    """The keypair of the cluster"""

    name: Required[str]
    """The name of the cluster"""

    pools: Required[Iterable[Pool]]
    """The pools of the cluster"""

    version: Required[str]
    """The version of the k8s cluster"""

    add_ons: AddOns
    """Cluster add-ons configuration"""

    authentication: Optional[Authentication]
    """Authentication settings"""

    autoscaler_config: Optional[Dict[str, str]]
    """Cluster autoscaler configuration.

    It allows you to override the default cluster-autoscaler parameters provided by
    the platform with your preferred values.

    Supported parameters (in alphabetical order):

    - balance-similar-node-groups (boolean: true/false) - Detect similar node groups
      and balance the number of nodes between them.
    - expander (string: random, most-pods, least-waste, price, priority, grpc) -
      Type of node group expander to be used in scale up. Specifying multiple values
      separated by commas will call the expanders in succession until there is only
      one option remaining.
    - expendable-pods-priority-cutoff (float) - Pods with priority below cutoff will
      be expendable. They can be killed without any consideration during scale down
      and they don't cause scale up. Pods with null priority (PodPriority disabled)
      are non expendable.
    - ignore-daemonsets-utilization (boolean: true/false) - Should CA ignore
      DaemonSet pods when calculating resource utilization for scaling down.
    - max-empty-bulk-delete (integer) - Maximum number of empty nodes that can be
      deleted at the same time.
    - max-graceful-termination-sec (integer) - Maximum number of seconds CA waits
      for pod termination when trying to scale down a node.
    - max-node-provision-time (duration: e.g., '15m') - The default maximum time CA
      waits for node to be provisioned - the value can be overridden per node group.
    - max-total-unready-percentage (float) - Maximum percentage of unready nodes in
      the cluster. After this is exceeded, CA halts operations.
    - new-pod-scale-up-delay (duration: e.g., '10s') - Pods less than this old will
      not be considered for scale-up. Can be increased for individual pods through
      annotation.
    - ok-total-unready-count (integer) - Number of allowed unready nodes,
      irrespective of max-total-unready-percentage.
    - scale-down-delay-after-add (duration: e.g., '10m') - How long after scale up
      that scale down evaluation resumes.
    - scale-down-delay-after-delete (duration: e.g., '10s') - How long after node
      deletion that scale down evaluation resumes.
    - scale-down-delay-after-failure (duration: e.g., '3m') - How long after scale
      down failure that scale down evaluation resumes.
    - scale-down-enabled (boolean: true/false) - Should CA scale down the cluster.
    - scale-down-unneeded-time (duration: e.g., '10m') - How long a node should be
      unneeded before it is eligible for scale down.
    - scale-down-unready-time (duration: e.g., '20m') - How long an unready node
      should be unneeded before it is eligible for scale down.
    - scale-down-utilization-threshold (float) - The maximum value between the sum
      of cpu requests and sum of memory requests of all pods running on the node
      divided by node's corresponding allocatable resource, below which a node can
      be considered for scale down.
    - scan-interval (duration: e.g., '10s') - How often cluster is reevaluated for
      scale up or down.
    - skip-nodes-with-custom-controller-pods (boolean: true/false) - If true cluster
      autoscaler will never delete nodes with pods owned by custom controllers.
    - skip-nodes-with-local-storage (boolean: true/false) - If true cluster
      autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir
      or HostPath.
    - skip-nodes-with-system-pods (boolean: true/false) - If true cluster autoscaler
      will never delete nodes with pods from kube-system (except for DaemonSet or
      mirror pods).
    """

    cni: Optional[Cni]
    """Cluster CNI settings"""

    csi: Csi
    """Container Storage Interface (CSI) driver settings"""

    ddos_profile: Optional[DDOSProfile]
    """Advanced DDoS Protection profile"""

    fixed_network: Optional[str]
    """The network of the cluster"""

    fixed_subnet: Optional[str]
    """The subnet of the cluster"""

    is_ipv6: Optional[bool]
    """Enable public v6 address"""

    logging: Optional[Logging]
    """Logging configuration"""

    pods_ip_pool: Optional[str]
    """The IP pool for the pods"""

    pods_ipv6_pool: Optional[str]
    """The IPv6 pool for the pods"""

    services_ip_pool: Optional[str]
    """The IP pool for the services"""

    services_ipv6_pool: Optional[str]
    """The IPv6 pool for the services"""


class Pool(TypedDict, total=False):
    flavor_id: Required[str]
    """Flavor ID"""

    min_node_count: Required[int]
    """Minimum node count"""

    name: Required[str]
    """Pool's name"""

    auto_healing_enabled: Optional[bool]
    """Enable auto healing"""

    boot_volume_size: Optional[int]
    """Boot volume size"""

    boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Boot volume type"""

    crio_config: Optional[Dict[str, str]]
    """Cri-o configuration for pool nodes"""

    is_public_ipv4: Optional[bool]
    """Enable public v4 address"""

    kubelet_config: Optional[Dict[str, str]]
    """Kubelet configuration for pool nodes"""

    labels: Optional[Dict[str, str]]
    """Labels applied to the cluster pool"""

    max_node_count: Optional[int]
    """Maximum node count"""

    servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]]
    """Server group policy: anti-affinity, soft-anti-affinity or affinity"""

    taints: Optional[Dict[str, str]]
    """Taints applied to the cluster pool"""


class AddOnsSlurm(TypedDict, total=False):
    """Slurm add-on configuration"""

    enabled: Required[Literal[True]]
    """The Slurm add-on will be enabled in the cluster.

    This add-on is only supported in clusters running Kubernetes v1.31 and v1.32
    with at least 1 GPU cluster pool and VAST NFS support enabled.
    """

    file_share_id: Required[str]
    """ID of a VAST file share to be used as Slurm storage.

    The Slurm add-on will create separate Persistent Volume Claims for different
    purposes (controller spool, worker spool, jail) on that file share.

    The file share must have `root_squash` disabled, while `path_length` and
    `allowed_characters` settings must be set to `NPL`.
    """

    ssh_key_ids: Required[SequenceNotStr[str]]
    """IDs of SSH keys to authorize for SSH connection to Slurm login nodes."""

    worker_count: Required[int]
    """Size of the worker pool, i.e. the number of Slurm worker nodes.

    Each Slurm worker node will be backed by a Pod scheduled on one of cluster's GPU
    nodes.
    """


class AddOns(TypedDict, total=False):
    """Cluster add-ons configuration"""

    slurm: AddOnsSlurm
    """Slurm add-on configuration"""


class AuthenticationOidc(TypedDict, total=False):
    """OIDC authentication settings"""

    client_id: Optional[str]
    """Client ID"""

    groups_claim: Optional[str]
    """JWT claim to use as the user's group"""

    groups_prefix: Optional[str]
    """Prefix prepended to group claims"""

    issuer_url: Optional[str]
    """Issuer URL"""

    required_claims: Optional[Dict[str, str]]
    """Key-value pairs that describe required claims in the token"""

    signing_algs: Optional[
        List[Literal["ES256", "ES384", "ES512", "PS256", "PS384", "PS512", "RS256", "RS384", "RS512"]]
    ]
    """Accepted signing algorithms"""

    username_claim: Optional[str]
    """JWT claim to use as the user name"""

    username_prefix: Optional[str]
    """Prefix prepended to username claims to prevent clashes"""


class Authentication(TypedDict, total=False):
    """Authentication settings"""

    oidc: Optional[AuthenticationOidc]
    """OIDC authentication settings"""


class CniCilium(TypedDict, total=False):
    """Cilium settings"""

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


class Cni(TypedDict, total=False):
    """Cluster CNI settings"""

    cilium: Optional[CniCilium]
    """Cilium settings"""

    provider: Literal["calico", "cilium"]
    """CNI provider"""


class CsiNfs(TypedDict, total=False):
    """NFS CSI driver settings"""

    vast_enabled: bool
    """Enable or disable VAST NFS integration.

    The default value is `false`. When set to `true`, a dedicated StorageClass will
    be created in the cluster for each VAST NFS file share defined in the cloud. All
    file shares created prior to cluster creation will be available immediately,
    while those created afterward may take a few minutes for to appear.
    """


class Csi(TypedDict, total=False):
    """Container Storage Interface (CSI) driver settings"""

    nfs: CsiNfs
    """NFS CSI driver settings"""


class DDOSProfileField(TypedDict, total=False):
    base_field: Required[int]

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified"""

    value: Optional[str]
    """Basic value. Only one of 'value' or '`field_value`' must be specified"""


class DDOSProfile(TypedDict, total=False):
    """Advanced DDoS Protection profile"""

    enabled: Required[bool]
    """Enable advanced DDoS protection"""

    fields: Iterable[DDOSProfileField]
    """DDoS profile parameters"""

    profile_template: Optional[int]
    """DDoS profile template ID"""

    profile_template_name: Optional[str]
    """DDoS profile template name"""


class Logging(TypedDict, total=False):
    """Logging configuration"""

    destination_region_id: Optional[int]
    """Destination region id to which the logs will be written"""

    enabled: bool
    """Enable/disable forwarding logs to LaaS"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """The logs retention policy"""

    topic_name: Optional[str]
    """The topic name to which the logs will be written"""
