# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .tag_update_map_param import TagUpdateMapParam

__all__ = ["PortUpdateParams", "AllowedAddressPair", "IPAssignment"]


class PortUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    allowed_address_pairs: Iterable[AllowedAddressPair]
    """A set of zero or more allowed port address pair and/or subnet masks.

    Replaces the full set of allowed address pairs. Send `[]` to clear; omit the
    field to leave existing pairs unchanged.
    """

    ip_assignments: Iterable[IPAssignment]
    """IP assignments on the port.

    Replaces the full set. Subnets must belong to the port's network, and a port an
    instance holds supports one subnet per IP version. An entry without `ip_address`
    keeps an address the port already has in that subnet, in the order the port
    reports them, or takes a free one when the port has none. Addresses that no
    entry keeps are released.
    """

    port_security_enabled: bool
    """
    When true, the network driver enforces port security on this port (anti-spoofing
    checks and security-group filtering apply). When false, all traffic is allowed
    and security groups are not applied.
    """

    security_group_ids: SequenceNotStr[str]
    """List of security group IDs.

    Replaces the full set of security groups attached to the port. Send `[]` to
    detach all groups; omit the field to leave existing groups unchanged.
    """

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


class AllowedAddressPair(TypedDict, total=False):
    ip_address: Required[str]
    """IP address or subnet of the allowed address pair"""


class IPAssignment(TypedDict, total=False):
    subnet_id: Required[str]
    """ID of the subnet"""

    ip_address: str
    """IP address to assign.

    Omit it to get any free address of the subnet, which is the only option when the
    subnet's free addresses are not known to the caller.
    """
