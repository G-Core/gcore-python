# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PlacementGroupDeleteResponse", "ResourcesToDelete", "ResourcesToPreserve"]


class ResourcesToDelete(BaseModel):
    id: str
    """The ID of the resource."""

    name: Optional[str] = None
    """The name of the resource.

    For a floating IP, the IP address. `null` for a volume, and for a resource
    without a name.
    """

    type: Literal["placement_groups"]
    """The type of the resource."""


class ResourcesToPreserve(BaseModel):
    id: str
    """The ID of the resource."""

    name: Optional[str] = None
    """The name of the resource.

    For a floating IP, the IP address. `null` for a volume, and for a resource
    without a name.
    """

    type: Literal["placement_groups"]
    """The type of the resource."""


class PlacementGroupDeleteResponse(BaseModel):
    resources_to_delete: List[ResourcesToDelete]
    """The placement group. Nothing else goes with it."""

    resources_to_preserve: List[ResourcesToPreserve]
    """Always empty.

    No resource is attached to a placement group. The other deletes use the same
    shape.
    """

    tasks: List[str]
    """List of task IDs representing asynchronous operations.

    Use these IDs to monitor operation progress:

    - `GET /v1/tasks/{task_id}` - Check individual task status and details Poll task
      status until completion (`FINISHED`/`ERROR`) before proceeding with dependent
      operations.
    """
