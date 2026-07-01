# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ClusterListParams", "CreatedAt", "Flavor", "Name", "ServersCount", "TagKey", "TagValue", "UpdatedAt"]


class ClusterListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    created_at: CreatedAt
    """Filter by creation time (UTC), e.g. `created_at[gte]=2026-01-01T00:00:00Z`."""

    flavor: Flavor
    """Filter by flavor (case-insensitive), e.g.

    `flavor[prefix]=bm3-`, `flavor[exact]=bm3-ai-1xlarge-h100-80-8`.
    """

    ids: SequenceNotStr[str]
    """Return only clusters with these IDs, e.g. `ids=<id1>&ids=<id2>`."""

    image_ids: SequenceNotStr[str]
    """Return only clusters built from these source image IDs, e.g.

    `image_ids=<id1>&image_ids=<id2>`.
    """

    limit: int
    """Limit of items on a single page"""

    managed_by: List[Literal["k8s", "user"]]
    """
    Filter by who manages the cluster: `user` (default) or `k8s` (Managed
    Kubernetes). Pass both to include all, e.g. `managed_by=user&managed_by=k8s`.
    """

    name: Name
    """Filter by name (case-insensitive), e.g.

    `name[contains]=gpu`, `name[prefix]=prod-`.
    """

    offset: int
    """Offset in results list"""

    servers_count: ServersCount
    """Filter by node count, e.g.

    `servers_count[gte]=2`, `servers_count[gte]=2&servers_count[lt]=8`.
    """

    tag_key: TagKey
    """Filter by tag key regardless of value, e.g. `tag_key[contains]=team`."""

    tag_value: TagValue
    """Filter by tag value regardless of key, e.g. `tag_value[prefix]=prod`."""

    tags: Dict[str, str]
    """Filter by exact tag key-value pairs, e.g.

    `tags[env]=prod&tags[team]=core`. Pairs are ANDed; values match
    case-insensitively.
    """

    updated_at: UpdatedAt
    """Filter by last-change time (UTC), e.g. `updated_at[gte]=2026-06-01T00:00:00Z`."""


class CreatedAt(TypedDict, total=False):
    """Filter by creation time (UTC), e.g. `created_at[gte]=2026-01-01T00:00:00Z`."""

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly after this timestamp, e.g. `[gt]=2026-01-01T00:00:00Z`."""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or after this timestamp (inclusive), e.g. `[gte]=2026-01-01T00:00:00Z`."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly before this timestamp, e.g. `[lt]=2026-02-01T00:00:00Z`."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or before this timestamp (inclusive), e.g. `[lte]=2026-02-01T00:00:00Z`."""


class Flavor(TypedDict, total=False):
    """Filter by flavor (case-insensitive), e.g.

    `flavor[prefix]=bm3-`, `flavor[exact]=bm3-ai-1xlarge-h100-80-8`.
    """

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


class Name(TypedDict, total=False):
    """Filter by name (case-insensitive), e.g.

    `name[contains]=gpu`, `name[prefix]=prod-`.
    """

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


class ServersCount(TypedDict, total=False):
    """Filter by node count, e.g.

    `servers_count[gte]=2`, `servers_count[gte]=2&servers_count[lt]=8`.
    """

    gt: int
    """Strictly greater than, e.g. `[gt]=1`."""

    gte: int
    """Greater than or equal, e.g. `[gte]=2`."""

    lt: int
    """Strictly less than, e.g. `[lt]=8`."""

    lte: int
    """Less than or equal, e.g. `[lte]=4`."""


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
    """Filter by last-change time (UTC), e.g. `updated_at[gte]=2026-06-01T00:00:00Z`."""

    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly after this timestamp, e.g. `[gt]=2026-01-01T00:00:00Z`."""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or after this timestamp (inclusive), e.g. `[gte]=2026-01-01T00:00:00Z`."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Strictly before this timestamp, e.g. `[lt]=2026-02-01T00:00:00Z`."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """At or before this timestamp (inclusive), e.g. `[lte]=2026-02-01T00:00:00Z`."""
