# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel
from .gpu_cluster_server import GPUClusterServer

__all__ = ["GPUBaremetalCluster", "Interface"]


class Interface(BaseModel):
    network_id: str
    """
    '#/components/schemas/AIClusterNetworkSerializer/properties/network_id'
    "$.components.schemas.AIClusterNetworkSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/AIClusterNetworkSerializer/properties/port_id'
    "$.components.schemas.AIClusterNetworkSerializer.properties.port_id"
    """

    subnet_id: str
    """
    '#/components/schemas/AIClusterNetworkSerializer/properties/subnet_id'
    "$.components.schemas.AIClusterNetworkSerializer.properties.subnet_id"
    """

    type: str
    """
    '#/components/schemas/AIClusterNetworkSerializer/properties/type'
    "$.components.schemas.AIClusterNetworkSerializer.properties.type"
    """


class GPUBaremetalCluster(BaseModel):
    cluster_id: str
    """
    '#/components/schemas/AIClusterSerializer/properties/cluster_id'
    "$.components.schemas.AIClusterSerializer.properties.cluster_id"
    """

    cluster_name: str
    """
    '#/components/schemas/AIClusterSerializer/properties/cluster_name'
    "$.components.schemas.AIClusterSerializer.properties.cluster_name"
    """

    cluster_status: Literal["ACTIVE", "ERROR", "PENDING", "SUSPENDED"]
    """
    '#/components/schemas/AIClusterSerializer/properties/cluster_status'
    "$.components.schemas.AIClusterSerializer.properties.cluster_status"
    """

    created_at: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/created_at/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.created_at.anyOf[0]"
    """

    creator_task_id: str
    """
    '#/components/schemas/AIClusterSerializer/properties/creator_task_id'
    "$.components.schemas.AIClusterSerializer.properties.creator_task_id"
    """

    flavor: str
    """
    '#/components/schemas/AIClusterSerializer/properties/flavor'
    "$.components.schemas.AIClusterSerializer.properties.flavor"
    """

    image_id: str
    """
    '#/components/schemas/AIClusterSerializer/properties/image_id'
    "$.components.schemas.AIClusterSerializer.properties.image_id"
    """

    image_name: str
    """
    '#/components/schemas/AIClusterSerializer/properties/image_name'
    "$.components.schemas.AIClusterSerializer.properties.image_name"
    """

    interfaces: Optional[List[Interface]] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/interfaces/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.interfaces.anyOf[0]"
    """

    password: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/password/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.password.anyOf[0]"
    """

    project_id: int
    """
    '#/components/schemas/AIClusterSerializer/properties/project_id'
    "$.components.schemas.AIClusterSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/AIClusterSerializer/properties/region'
    "$.components.schemas.AIClusterSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/AIClusterSerializer/properties/region_id'
    "$.components.schemas.AIClusterSerializer.properties.region_id"
    """

    servers: List[GPUClusterServer]
    """
    '#/components/schemas/AIClusterSerializer/properties/servers'
    "$.components.schemas.AIClusterSerializer.properties.servers"
    """

    ssh_key_name: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.ssh_key_name.anyOf[0]"
    """

    tags: List[Tag]
    """
    '#/components/schemas/AIClusterSerializer/properties/tags'
    "$.components.schemas.AIClusterSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.task_id.anyOf[0]"
    """

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
    """
    '#/components/schemas/AIClusterSerializer/properties/task_status'
    "$.components.schemas.AIClusterSerializer.properties.task_status"
    """

    user_data: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/user_data/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.user_data.anyOf[0]"
    """

    username: Optional[str] = None
    """
    '#/components/schemas/AIClusterSerializer/properties/username/anyOf/0'
    "$.components.schemas.AIClusterSerializer.properties.username.anyOf[0]"
    """
