# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .tag_update_map_param import TagUpdateMapParam

__all__ = ["InstanceUpdateParams", "Interface"]


class InstanceUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    data_volume_ids: SequenceNotStr[str]
    """Full list of the data volumes of the instance.

    Volumes that are not in the list are detached. New volumes are attached.
    """

    flavor_name: str
    """Name of the new flavor. The instance is resized to this flavor."""

    interfaces: Iterable[Interface]
    """Full list of the ports of the instance.

    Ports that are not in the list are detached. New ports are attached. Keep the
    current ports in their current order.
    """

    name: str
    """Instance name."""

    placement_group_id: Optional[str]
    """ID of the placement group.

    Send null to remove the instance from its placement group.
    """

    tags: Optional[TagUpdateMapParam]
    """Tags as JSON Merge Patch.

    A key with the value null removes that tag. The value null removes all tags.
    """


class Interface(TypedDict, total=False):
    port_id: Required[str]
    """Existing port to attach. Array order is the NIC/boot order."""
