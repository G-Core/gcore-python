# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["InstanceListParams", "CreatedAt", "FlavorName", "IPAddress", "Name", "TagKey", "TagValue", "UpdatedAt"]


class InstanceListParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    created_at: CreatedAt
    """Range filter on creation time."""

    flavor_name: FlavorName
    """Operator flavor name filter."""

    ids: SequenceNotStr[str]
    """Filter by instance UUID(s)."""

    ip_address: IPAddress
    """Exact IP filter on a fixed IP."""

    limit: int
    """Max items to return."""

    managed: bool
    """Filter by managed status.

    true = managed by a service, false = customer-operated.
    """

    managed_by: Literal["k8s_cluster"]
    """Filter by manager type, e.g. `k8s_cluster`."""

    managed_by_resource_ids: SequenceNotStr[str]
    """Filter by managing resource ID(s)."""

    managed_by_resource_names: SequenceNotStr[str]
    """Filter by managing resource name(s)."""

    name: Name
    """Operator name filter, e.g. name[contains]=web."""

    network_ids: SequenceNotStr[str]
    """Filter by network ID(s) the instance has a port on."""

    offset: int
    """Items to skip."""

    order_by: Literal[
        "created_at.asc",
        "created_at.desc",
        "name.asc",
        "name.desc",
        "region_id.asc",
        "region_id.desc",
        "status.asc",
        "status.desc",
    ]
    """Sort field and direction."""

    region_ids: Iterable[int]
    """Filter by region ID(s). Omit = all regions."""

    security_group_ids: SequenceNotStr[str]
    """Filter by security group ID(s)."""

    statuses: List[
        Literal[
            "active",
            "deleted",
            "deleting",
            "error",
            "provisioning",
            "rebooting",
            "rebuilding",
            "resizing",
            "stopped",
            "unknown",
            "updating",
        ]
    ]
    """Filter by lifecycle status(es)."""

    subnet_ids: SequenceNotStr[str]
    """Filter by subnet ID(s)."""

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


class FlavorName(TypedDict, total=False):
    """Operator flavor name filter."""

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


class IPAddress(TypedDict, total=False):
    """Exact IP filter on a fixed IP."""

    contains: SequenceNotStr[str]
    """Substring match on IP address, e.g.

    `[contains]=192.168`. Repeat the key to match any substring.
    """

    exact: SequenceNotStr[str]
    """Exact IP match, e.g.

    `[exact]=192.168.1.10`. Repeat the key to match any of several.
    """


class Name(TypedDict, total=False):
    """Operator name filter, e.g. name[contains]=web."""

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
