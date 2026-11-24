# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = ["ServerUpdateParams", "Interface"]


class ServerUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    interfaces: Iterable[Interface]
    """Full list of the interfaces of the server.

    Interfaces that are not in the list are detached. Keep the current interfaces in
    their current order. Add new interfaces at the end of the list. Send at least
    one interface.
    """

    name: str
    """Server name."""

    tags: Optional[TagUpdateMapParam]
    """Update key-value tags using JSON Merge Patch semantics (RFC 7396).

    Provide key-value pairs to add or update tags. Set tag values to `null` to
    remove tags. Unspecified tags remain unchanged. Read-only tags are always
    preserved and cannot be modified.

    **Examples:**

    - **Add/update tags:**
      `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
      updates existing ones.
    - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
    - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
      tags are preserved).
    - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
      specified tags.
    - **Mixed operations:**
      `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
      adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
      preserving other existing tags.
    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class Interface(TypedDict, total=False):
    port_id: Required[str]
    """Existing port to attach. Array order is the NIC/boot order."""

    port_group: int
    """0-based bond/trunk group, dense across all interfaces.

    Omitted defaults to group 0. Must be omitted on DPU/SmartNIC flavors.
    """
