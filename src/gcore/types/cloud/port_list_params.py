# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PortListParams", "CreatedAt", "IPAddress", "TagKey", "TagValue", "UpdatedAt"]


class PortListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    attached: bool
    """Filter attached (true) or standalone (false) ports."""

    attached_to_resource_ids: SequenceNotStr[str]
    """Filter by attached resource ID(s).

    Matches ports attached to any of the given resources.
    """

    attached_to_resource_types: List[
        Literal[
            "baremetal_server",
            "basic_vm",
            "dhcp",
            "gpu_baremetal_server",
            "gpu_virtual_server",
            "instance",
            "load_balancer",
            "router",
        ]
    ]
    """Filter by attachment resource type(s).

    A port matches if its type is any of the given values.
    """

    created_at: CreatedAt
    """Range filter on creation time."""

    ids: SequenceNotStr[str]
    """Filter by port UUID(s)."""

    ip_address: IPAddress
    """Filter by fixed IP address."""

    limit: int
    """Max items to return."""

    managed: bool
    """Filter by managed status.

    true = managed by a service, false = customer-operated. A port with a manager
    type that this API version does not know counts as managed, but its `managed_by`
    is null. Cannot be combined with `managed_by` when false.
    """

    managed_by: Literal[
        "file_share",
        "gpu_baremetal_cluster",
        "gpu_virtual_cluster",
        "k8s_cluster",
        "load_balancer",
        "network",
        "router",
        "system",
    ]
    """Filter by manager type, e.g. system or `k8s_cluster`."""

    managed_by_resource_ids: SequenceNotStr[str]
    """Filter by managing resource ID(s)."""

    managed_by_resource_names: SequenceNotStr[str]
    """Filter by managing resource name(s)."""

    network_ids: SequenceNotStr[str]
    """Filter by network ID(s)."""

    offset: int
    """Items to skip."""

    order_by: Literal[
        "created_at.asc",
        "created_at.desc",
        "network_grouping.asc",
        "region_id.asc",
        "region_id.desc",
        "updated_at.asc",
        "updated_at.desc",
    ]
    """Sort field and direction.

    `network_grouping.asc` keeps the ports of one network together. In each region,
    the networks shared with the project come first, in the order of the share. If
    no shared network is public, the default public network of the region comes
    next. Then come other public networks, then all other networks.
    """

    public: bool
    """
    Filter ports on networks that give publicly routed address space (true) or not
    (false).
    """

    region_ids: Iterable[int]
    """Filter by region ID(s). Omit = all regions."""

    security_group_ids: SequenceNotStr[str]
    """Filter by security group ID(s).

    A port matches if it has any of the given security groups.
    """

    subnet_ids: SequenceNotStr[str]
    """Filter by subnet ID(s).

    A port matches if it has a fixed IP in any of the given subnets.
    """

    tag_key: TagKey
    """Filter by tag key regardless of value, e.g. `tag_key[contains]=team`."""

    tag_value: TagValue
    """Filter by tag value regardless of key, e.g. `tag_value[prefix]=prod`."""

    tags: Dict[str, SequenceNotStr[str]]
    """Filter by exact tag key-value pairs, e.g.

    `tags[env]=prod&tags[team]=core`. Repeat a key to match any of several values
    for it, e.g. `tags[env]=prod&tags[env]=dev`. Values for one key are ORed,
    different keys are ANDed; values match case-insensitively.
    """

    updated_at: UpdatedAt
    """Range filter on last-update time."""


class CreatedAt(TypedDict, total=False):
    """Range filter on creation time."""

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly after this timestamp, e.g. `[gt]=2026-01-01T00:00:00Z`."""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or after this timestamp (inclusive), e.g. `[gte]=2026-01-01T00:00:00Z`."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly before this timestamp, e.g. `[lt]=2026-02-01T00:00:00Z`."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or before this timestamp (inclusive), e.g. `[lte]=2026-02-01T00:00:00Z`."""


class IPAddress(TypedDict, total=False):
    """Filter by fixed IP address."""

    contains: SequenceNotStr[str]
    """Substring match on IP address, e.g.

    `[contains]=192.168`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Exact IP match, e.g.

    `[exact]=192.168.1.10`. Repeat the key to match any of several.
    """


class TagKey(TypedDict, total=False):
    """Filter by tag key regardless of value, e.g. `tag_key[contains]=team`."""

    contains: SequenceNotStr[str]
    """Case-insensitive substring, e.g.

    `[contains]=web`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Case-insensitive exact match, e.g.

    `[exact]=web-1`. Repeat the key to match any of several.
    """

    prefix: SequenceNotStr[str]
    """Case-insensitive starts-with, e.g.

    `[prefix]=prod-`. Repeat the key to match any prefix.
    """

    suffix: SequenceNotStr[str]
    """Case-insensitive ends-with, e.g.

    `[suffix]=-db`. Repeat the key to match any suffix.
    """


class TagValue(TypedDict, total=False):
    """Filter by tag value regardless of key, e.g. `tag_value[prefix]=prod`."""

    contains: SequenceNotStr[str]
    """Case-insensitive substring, e.g.

    `[contains]=web`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Case-insensitive exact match, e.g.

    `[exact]=web-1`. Repeat the key to match any of several.
    """

    prefix: SequenceNotStr[str]
    """Case-insensitive starts-with, e.g.

    `[prefix]=prod-`. Repeat the key to match any prefix.
    """

    suffix: SequenceNotStr[str]
    """Case-insensitive ends-with, e.g.

    `[suffix]=-db`. Repeat the key to match any suffix.
    """


class UpdatedAt(TypedDict, total=False):
    """Range filter on last-update time."""

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly after this timestamp, e.g. `[gt]=2026-01-01T00:00:00Z`."""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or after this timestamp (inclusive), e.g. `[gte]=2026-01-01T00:00:00Z`."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly before this timestamp, e.g. `[lt]=2026-02-01T00:00:00Z`."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or before this timestamp (inclusive), e.g. `[lte]=2026-02-01T00:00:00Z`."""
