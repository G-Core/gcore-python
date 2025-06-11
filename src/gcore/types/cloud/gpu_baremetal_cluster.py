# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel
from .gpu_baremetal_cluster_server import GPUBaremetalClusterServer

__all__ = ["GPUBaremetalCluster", "Interface"]


class Interface(BaseModel):
    network_id: str
    """Network ID"""

    port_id: str
    """Network ID the subnet belongs to. Port will be plugged in this network"""

    subnet_id: str
    """Port is assigned to IP address from the subnet"""

    type: str
    """Network type"""


class GPUBaremetalCluster(BaseModel):
    cluster_id: str
    """GPU Cluster ID"""

    cluster_name: str
    """GPU Cluster Name"""

    cluster_status: Literal["ACTIVE", "ERROR", "PENDING", "SUSPENDED"]
    """GPU Cluster status"""

    created_at: Optional[str] = None
    """Datetime when the cluster was created"""

    creator_task_id: str
    """Task that created this entity"""

    flavor: str
    """Flavor ID is the same as the name"""

    image_id: str
    """Image ID"""

    image_name: str
    """Image name"""

    interfaces: Optional[List[Interface]] = None
    """Networks managed by user and associated with the cluster"""

    password: Optional[str] = None
    """A password for a bare metal server.

    This parameter is used to set a password for the "Admin" user on a Windows
    instance, a default user or a new user on a Linux instance
    """

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    servers: List[GPUBaremetalClusterServer]
    """GPU cluster servers"""

    ssh_key_name: Optional[str] = None
    """Keypair name to inject into new cluster(s)"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """Task ID associated with the cluster"""

    task_status: Literal[
        "CLUSTER_CLEAN_UP",
        "CLUSTER_RESIZE",
        "CLUSTER_RESUME",
        "CLUSTER_SUSPEND",
        "ERROR",
        "FINISHED",
        "IPU_SERVERS",
        "NETWORK",
        "POPLAR_SERVERS",
        "POST_DEPLOY_SETUP",
        "VIPU_CONTROLLER",
    ]
    """Task status"""

    user_data: Optional[str] = None
    """String in base64 format.

    Must not be passed together with 'username' or 'password'. Examples of the
    `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """

    username: Optional[str] = None
    """A name of a new user in the Linux instance.

    It may be passed with a 'password' parameter
    """
