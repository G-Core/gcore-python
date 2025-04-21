# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Task", "CreatedResources"]


class CreatedResources(BaseModel):
    ai_clusters: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/ai_clusters'
    "$.components.schemas.CreatedResources.properties.ai_clusters"
    """

    api_keys: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/api_keys'
    "$.components.schemas.CreatedResources.properties.api_keys"
    """

    caas_containers: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/caas_containers'
    "$.components.schemas.CreatedResources.properties.caas_containers"
    """

    ddos_profiles: Optional[List[int]] = None
    """
    '#/components/schemas/CreatedResources/properties/ddos_profiles'
    "$.components.schemas.CreatedResources.properties.ddos_profiles"
    """

    faas_functions: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/faas_functions'
    "$.components.schemas.CreatedResources.properties.faas_functions"
    """

    faas_namespaces: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/faas_namespaces'
    "$.components.schemas.CreatedResources.properties.faas_namespaces"
    """

    file_shares: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/file_shares'
    "$.components.schemas.CreatedResources.properties.file_shares"
    """

    floatingips: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/floatingips'
    "$.components.schemas.CreatedResources.properties.floatingips"
    """

    healthmonitors: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/healthmonitors'
    "$.components.schemas.CreatedResources.properties.healthmonitors"
    """

    heat: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/heat'
    "$.components.schemas.CreatedResources.properties.heat"
    """

    images: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/images'
    "$.components.schemas.CreatedResources.properties.images"
    """

    inference_instances: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/inference_instances'
    "$.components.schemas.CreatedResources.properties.inference_instances"
    """

    instances: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/instances'
    "$.components.schemas.CreatedResources.properties.instances"
    """

    k8s_clusters: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/k8s_clusters'
    "$.components.schemas.CreatedResources.properties.k8s_clusters"
    """

    k8s_pools: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/k8s_pools'
    "$.components.schemas.CreatedResources.properties.k8s_pools"
    """

    l7polices: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/l7polices'
    "$.components.schemas.CreatedResources.properties.l7polices"
    """

    l7rules: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/l7rules'
    "$.components.schemas.CreatedResources.properties.l7rules"
    """

    laas_topic: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/laas_topic'
    "$.components.schemas.CreatedResources.properties.laas_topic"
    """

    listeners: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/listeners'
    "$.components.schemas.CreatedResources.properties.listeners"
    """

    loadbalancers: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/loadbalancers'
    "$.components.schemas.CreatedResources.properties.loadbalancers"
    """

    members: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/members'
    "$.components.schemas.CreatedResources.properties.members"
    """

    networks: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/networks'
    "$.components.schemas.CreatedResources.properties.networks"
    """

    pools: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/pools'
    "$.components.schemas.CreatedResources.properties.pools"
    """

    ports: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/ports'
    "$.components.schemas.CreatedResources.properties.ports"
    """

    postgresql_clusters: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/postgresql_clusters'
    "$.components.schemas.CreatedResources.properties.postgresql_clusters"
    """

    projects: Optional[List[int]] = None
    """
    '#/components/schemas/CreatedResources/properties/projects'
    "$.components.schemas.CreatedResources.properties.projects"
    """

    registry_registries: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/registry_registries'
    "$.components.schemas.CreatedResources.properties.registry_registries"
    """

    registry_users: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/registry_users'
    "$.components.schemas.CreatedResources.properties.registry_users"
    """

    routers: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/routers'
    "$.components.schemas.CreatedResources.properties.routers"
    """

    secrets: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/secrets'
    "$.components.schemas.CreatedResources.properties.secrets"
    """

    servergroups: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/servergroups'
    "$.components.schemas.CreatedResources.properties.servergroups"
    """

    snapshots: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/snapshots'
    "$.components.schemas.CreatedResources.properties.snapshots"
    """

    subnets: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/subnets'
    "$.components.schemas.CreatedResources.properties.subnets"
    """

    volumes: Optional[List[str]] = None
    """
    '#/components/schemas/CreatedResources/properties/volumes'
    "$.components.schemas.CreatedResources.properties.volumes"
    """


class Task(BaseModel):
    id: str
    """
    '#/components/schemas/TaskSerializer/properties/id'
    "$.components.schemas.TaskSerializer.properties.id"
    """

    created_on: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/created_on/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.created_on.anyOf[0]"
    """

    state: Literal["ERROR", "FINISHED", "NEW", "RUNNING"]
    """
    '#/components/schemas/TaskSerializer/properties/state'
    "$.components.schemas.TaskSerializer.properties.state"
    """

    task_type: str
    """
    '#/components/schemas/TaskSerializer/properties/task_type'
    "$.components.schemas.TaskSerializer.properties.task_type"
    """

    user_id: int
    """
    '#/components/schemas/TaskSerializer/properties/user_id'
    "$.components.schemas.TaskSerializer.properties.user_id"
    """

    acknowledged_at: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/acknowledged_at/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.acknowledged_at.anyOf[0]"
    """

    acknowledged_by: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/acknowledged_by/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.acknowledged_by.anyOf[0]"
    """

    client_id: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/client_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.client_id.anyOf[0]"
    """

    created_resources: Optional[CreatedResources] = None
    """
    '#/components/schemas/TaskSerializer/properties/created_resources/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.created_resources.anyOf[0]"
    """

    data: Optional[object] = None
    """
    '#/components/schemas/TaskSerializer/properties/data/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.data.anyOf[0]"
    """

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
    """
    '#/components/schemas/TaskSerializer/properties/detailed_state/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.detailed_state.anyOf[0]"
    """

    error: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/error/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.error.anyOf[0]"
    """

    finished_on: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/finished_on/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.finished_on.anyOf[0]"
    """

    job_id: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/job_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.job_id.anyOf[0]"
    """

    lifecycle_policy_id: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/lifecycle_policy_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.lifecycle_policy_id.anyOf[0]"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.project_id.anyOf[0]"
    """

    region_id: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/region_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.region_id.anyOf[0]"
    """

    request_id: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/request_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.request_id.anyOf[0]"
    """

    schedule_id: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/schedule_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.schedule_id.anyOf[0]"
    """

    updated_on: Optional[str] = None
    """
    '#/components/schemas/TaskSerializer/properties/updated_on/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.updated_on.anyOf[0]"
    """

    user_client_id: Optional[int] = None
    """
    '#/components/schemas/TaskSerializer/properties/user_client_id/anyOf/0'
    "$.components.schemas.TaskSerializer.properties.user_client_id.anyOf[0]"
    """
