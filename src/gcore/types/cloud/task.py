# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Task", "CreatedResources"]


class CreatedResources(BaseModel):
    ai_clusters: Optional[List[str]] = None
    """IDs of created AI clusters"""

    api_keys: Optional[List[str]] = None
    """IDs of created API keys"""

    caas_containers: Optional[List[str]] = None
    """IDs of created CaaS containers"""

    ddos_profiles: Optional[List[int]] = None
    """IDs of created ddos protection profiles"""

    faas_functions: Optional[List[str]] = None
    """IDs of created FaaS functions"""

    faas_namespaces: Optional[List[str]] = None
    """IDs of created FaaS namespaces"""

    file_shares: Optional[List[str]] = None
    """IDs of created file shares"""

    floatingips: Optional[List[str]] = None
    """IDs of created floating IPs"""

    healthmonitors: Optional[List[str]] = None
    """IDs of created health monitors"""

    images: Optional[List[str]] = None
    """IDs of created images"""

    inference_instances: Optional[List[str]] = None
    """IDs of created inference instances"""

    instances: Optional[List[str]] = None
    """IDs of created instances"""

    k8s_clusters: Optional[List[str]] = None
    """IDs of created Kubernetes clusters"""

    k8s_pools: Optional[List[str]] = None
    """IDs of created Kubernetes pools"""

    l7polices: Optional[List[str]] = None
    """IDs of created L7 policies"""

    l7rules: Optional[List[str]] = None
    """IDs of created L7 rules"""

    laas_topic: Optional[List[str]] = None
    """IDs of created LaaS topics"""

    listeners: Optional[List[str]] = None
    """IDs of created load balancer listeners"""

    loadbalancers: Optional[List[str]] = None
    """IDs of created load balancers"""

    members: Optional[List[str]] = None
    """IDs of created pool members"""

    networks: Optional[List[str]] = None
    """IDs of created networks"""

    pools: Optional[List[str]] = None
    """IDs of created load balancer pools"""

    ports: Optional[List[str]] = None
    """IDs of created ports"""

    postgresql_clusters: Optional[List[str]] = None
    """IDs of created postgres clusters"""

    projects: Optional[List[int]] = None
    """IDs of created projects"""

    registry_registries: Optional[List[str]] = None
    """IDs of created registry registries"""

    registry_users: Optional[List[str]] = None
    """IDs of created registry users"""

    routers: Optional[List[str]] = None
    """IDs of created routers"""

    secrets: Optional[List[str]] = None
    """IDs of created secrets"""

    servergroups: Optional[List[str]] = None
    """IDs of created server groups"""

    snapshots: Optional[List[str]] = None
    """IDs of created volume snapshots"""

    subnets: Optional[List[str]] = None
    """IDs of created subnets"""

    volumes: Optional[List[str]] = None
    """IDs of created volumes"""


class Task(BaseModel):
    id: str
    """The task ID"""

    created_on: Optional[str] = None
    """Created timestamp"""

    state: Literal["ERROR", "FINISHED", "NEW", "RUNNING"]
    """The task state"""

    task_type: str
    """The task type"""

    user_id: int
    """The user ID that initiated the task"""

    acknowledged_at: Optional[str] = None
    """If task was acknowledged, this field stores acknowledge timestamp"""

    acknowledged_by: Optional[int] = None
    """If task was acknowledged, this field stores `user_id` of the person"""

    client_id: Optional[int] = None
    """The client ID"""

    created_resources: Optional[CreatedResources] = None
    """If the task creates resources, this field will contain their IDs"""

    data: Optional[object] = None
    """Task parameters"""

    detailed_state: Optional[
        Literal[
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
    ] = None
    """Task detailed state that is more specific to task type"""

    error: Optional[str] = None
    """The error value"""

    finished_on: Optional[str] = None
    """Finished timestamp"""

    job_id: Optional[str] = None
    """Job ID"""

    lifecycle_policy_id: Optional[int] = None
    """Lifecycle policy ID"""

    project_id: Optional[int] = None
    """The project ID"""

    region_id: Optional[int] = None
    """The region ID"""

    request_id: Optional[str] = None
    """The request ID"""

    schedule_id: Optional[str] = None
    """Schedule ID"""

    updated_on: Optional[str] = None
    """Last updated timestamp"""

    user_client_id: Optional[int] = None
    """Client, specified in user's JWT"""
