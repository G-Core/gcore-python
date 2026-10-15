# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CostReportGetBreakdownParams", "Tags", "TagsCondition"]


class CostReportGetBreakdownParams(TypedDict, total=False):
    time_from: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start date of the report period (ISO 8601).

    The report starts from the beginning of this day in UTC.
    """

    time_to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The end date of the report period (ISO 8601).

    The report ends just before the beginning of this day in UTC.
    """

    enable_last_day: bool
    """Expenses for the last specified day are taken into account.

    As the default, False.
    """

    group_by: Literal["flavor", "project", "region", "type"]
    """Dimension the daily rows are summed down to. Only one grouping per request."""

    project_ids: Iterable[int]
    """List of project IDs. Omit for all accessible projects."""

    region_ids: Iterable[int]
    """List of region IDs.

    Omit for all regions and global usage; an empty list is rejected. Use 0 for
    global usage that has no region.
    """

    response_format: Literal["csv_records", "json"]
    """Format of the response: json (default) or `csv_records`."""

    tags: Tags
    """Filter by tags"""

    types: List[
        Literal[
            "ai_cluster",
            "ai_virtual_cluster",
            "backup",
            "baremetal",
            "basic_vm",
            "containers",
            "dbaas_postgresql_connection_pooler",
            "dbaas_postgresql_cpu",
            "dbaas_postgresql_memory",
            "dbaas_postgresql_public_network",
            "dbaas_postgresql_volume",
            "egress_traffic",
            "external_ip",
            "file_share",
            "floatingip",
            "functions",
            "functions_calls",
            "functions_traffic",
            "image",
            "inference",
            "inference_public_models",
            "instance",
            "load_balancer",
            "log_index",
            "snapshot",
            "volume",
        ]
    ]
    """List of resource types. Omit for all types."""


class TagsCondition(TypedDict, total=False):
    key: str
    """The name of the tag to filter (e.g., 'os_version')."""

    strict: bool
    """Determines how strictly the tag value must match the specified value.

    If true, the tag value must exactly match the given value. If false, a less
    strict match (e.g., partial or case-insensitive match) may be applied.
    """

    value: str
    """The value of the tag to filter (e.g., '22.04')."""


class Tags(TypedDict, total=False):
    """Filter by tags"""

    conditions: Required[Iterable[TagsCondition]]
    """A list of tag filtering conditions defining how tags should match."""

    condition_type: Literal["AND", "OR"]
    """Specifies whether conditions are combined using OR (default) or AND logic."""
