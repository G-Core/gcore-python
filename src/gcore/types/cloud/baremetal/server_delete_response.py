# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ServerDeleteResponse", "ResourcesToDelete", "ResourcesToPreserve"]


class ResourcesToDelete(BaseModel):
    id: str
    """The ID of the resource."""

    name: Optional[str] = None
    """The name of the resource.

    For a floating IP, the IP address. `null` for a volume, and for a resource
    without a name.
    """

    type: Literal["baremetal_servers", "floating_ips", "ports"]
    """The type of the resource."""


class ResourcesToPreserve(BaseModel):
    id: str
    """The ID of the resource."""

    name: Optional[str] = None
    """The name of the resource.

    For a floating IP, the IP address. `null` for a volume, and for a resource
    without a name.
    """

    type: Literal["baremetal_servers", "floating_ips", "ports"]
    """The type of the resource."""


class ServerDeleteResponse(BaseModel):
    resources_to_delete: List[ResourcesToDelete]
    """
    Every resource that this request deletes: the server, and each port and floating
    IP that goes with it. Sorted by `type`, then by `id`.
    """

    resources_to_preserve: List[ResourcesToPreserve]
    """The ports and floating IPs of the server that stay after the delete.

    Sorted by `type`, then by `id`.
    """

    tasks: List[str]
    """List of task IDs representing asynchronous operations.

    Use these IDs to monitor operation progress:

    - `GET /v1/tasks/{task_id}` - Check individual task status and details Poll task
      status until completion (`FINISHED`/`ERROR`) before proceeding with dependent
      operations.
    """
