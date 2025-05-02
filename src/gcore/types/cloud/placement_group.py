# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["PlacementGroup", "Instance"]


class Instance(BaseModel):
    instance_id: str
    """The ID of the instance, corresponding to the attribute 'id'."""

    instance_name: str
    """The name of the instance, corresponding to the attribute 'name'."""


class PlacementGroup(BaseModel):
    instances: List[Instance]
    """The list of instances in this server group."""

    name: str
    """The name of the server group."""

    policy: str
    """The server group policy.

    Options are: anti-affinity, affinity, or soft-anti-affinity.
    """

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    servergroup_id: str
    """The ID of the server group."""
