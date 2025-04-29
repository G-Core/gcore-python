# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["PlacementGroup", "Instance"]


class Instance(BaseModel):
    instance_id: str
    """
    '#/components/schemas/InstanceBriefSerializer/properties/instance_id'
    "$.components.schemas.InstanceBriefSerializer.properties.instance_id"
    """

    instance_name: str
    """
    '#/components/schemas/InstanceBriefSerializer/properties/instance_name'
    "$.components.schemas.InstanceBriefSerializer.properties.instance_name"
    """


class PlacementGroup(BaseModel):
    instances: List[Instance]
    """
    '#/components/schemas/ServerGroupSerializer/properties/instances'
    "$.components.schemas.ServerGroupSerializer.properties.instances"
    """

    name: str
    """
    '#/components/schemas/ServerGroupSerializer/properties/name'
    "$.components.schemas.ServerGroupSerializer.properties.name"
    """

    policy: str
    """
    '#/components/schemas/ServerGroupSerializer/properties/policy'
    "$.components.schemas.ServerGroupSerializer.properties.policy"
    """

    project_id: int
    """
    '#/components/schemas/ServerGroupSerializer/properties/project_id'
    "$.components.schemas.ServerGroupSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/ServerGroupSerializer/properties/region'
    "$.components.schemas.ServerGroupSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/ServerGroupSerializer/properties/region_id'
    "$.components.schemas.ServerGroupSerializer.properties.region_id"
    """

    servergroup_id: str
    """
    '#/components/schemas/ServerGroupSerializer/properties/servergroup_id'
    "$.components.schemas.ServerGroupSerializer.properties.servergroup_id"
    """
