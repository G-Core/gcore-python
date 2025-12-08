# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "CostReportGetAggregatedParams",
    "SchemaFilter",
    "SchemaFilterSchemaFilterSnapshotSerializer",
    "SchemaFilterSchemaFilterInstanceSerializer",
    "SchemaFilterSchemaFilterAIClusterSerializer",
    "SchemaFilterSchemaFilterAIVirtualClusterSerializer",
    "SchemaFilterSchemaFilterBasicVmSerializer",
    "SchemaFilterSchemaFilterBaremetalSerializer",
    "SchemaFilterSchemaFilterVolumeSerializer",
    "SchemaFilterSchemaFilterFileShareSerializer",
    "SchemaFilterSchemaFilterImageSerializer",
    "SchemaFilterSchemaFilterFloatingIPSerializer",
    "SchemaFilterSchemaFilterEgressTrafficSerializer",
    "SchemaFilterSchemaFilterLoadBalancerSerializer",
    "SchemaFilterSchemaFilterExternalIPSerializer",
    "SchemaFilterSchemaFilterBackupSerializer",
    "SchemaFilterSchemaFilterLogIndexSerializer",
    "SchemaFilterSchemaFilterFunctionsSerializer",
    "SchemaFilterSchemaFilterFunctionsCallsSerializer",
    "SchemaFilterSchemaFilterFunctionsTrafficSerializer",
    "SchemaFilterSchemaFilterContainersSerializer",
    "SchemaFilterSchemaFilterInferenceSerializer",
    "SchemaFilterSchemaFilterDbaasPostgreSQLVolumeSerializer",
    "SchemaFilterSchemaFilterDbaasPostgreSQLPublicNetworkSerializer",
    "SchemaFilterSchemaFilterDbaasPostgreSqlcpuSerializer",
    "SchemaFilterSchemaFilterDbaasPostgreSQLMemorySerializer",
    "SchemaFilterSchemaFilterDbaasPostgreSQLPoolerSerializer",
    "Tags",
    "TagsCondition",
]


class CostReportGetAggregatedParams(TypedDict, total=False):
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

    projects: Iterable[int]
    """List of project IDs"""

    regions: Iterable[int]
    """List of region IDs."""

    response_format: Literal["csv_totals", "json"]
    """Format of the response (csv or json)."""

    rounding: bool
    """Round cost values to 5 decimal places. When false, returns full precision."""

    schema_filter: SchemaFilter
    """Extended filter for field filtering."""

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
            "instance",
            "load_balancer",
            "log_index",
            "snapshot",
            "volume",
        ]
    ]
    """List of resource types to be filtered in the report."""


class SchemaFilterSchemaFilterSnapshotSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "last_size", "source_volume_uuid", "type", "uuid", "volume_type"]]
    """Field name to filter by"""

    type: Required[Literal["snapshot"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterInstanceSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["instance"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterAIClusterSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["ai_cluster"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterAIVirtualClusterSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["ai_virtual_cluster"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterBasicVmSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["basic_vm"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterBaremetalSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["baremetal"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterVolumeSerializer(TypedDict, total=False):
    field: Required[Literal["attached_to_vm", "last_name", "last_size", "type", "uuid", "volume_type"]]
    """Field name to filter by"""

    type: Required[Literal["volume"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterFileShareSerializer(TypedDict, total=False):
    field: Required[Literal["file_share_type", "last_name", "last_size", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["file_share"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterImageSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "last_size", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["image"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterFloatingIPSerializer(TypedDict, total=False):
    field: Required[Literal["ip_address", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["floatingip"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterEgressTrafficSerializer(TypedDict, total=False):
    field: Required[Literal["instance_name", "instance_type", "port_id", "type", "vm_id"]]
    """Field name to filter by"""

    type: Required[Literal["egress_traffic"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterLoadBalancerSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["load_balancer"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterExternalIPSerializer(TypedDict, total=False):
    field: Required[Literal["attached_to_vm", "ip_address", "network_id", "port_id", "subnet_id", "type"]]
    """Field name to filter by"""

    type: Required[Literal["external_ip"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterBackupSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "last_size", "schedule_id", "source_volume_uuid", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["backup"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterLogIndexSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "last_size", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["log_index"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterFunctionsSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["functions"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterFunctionsCallsSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["functions_calls"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterFunctionsTrafficSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["functions_traffic"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterContainersSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["containers"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterInferenceSerializer(TypedDict, total=False):
    field: Required[Literal["flavor", "last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["inference"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterDbaasPostgreSQLVolumeSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid", "volume_type"]]
    """Field name to filter by"""

    type: Required[Literal["dbaas_postgresql_volume"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterDbaasPostgreSQLPublicNetworkSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["dbaas_postgresql_public_network"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterDbaasPostgreSqlcpuSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["dbaas_postgresql_cpu"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterDbaasPostgreSQLMemorySerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["dbaas_postgresql_memory"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


class SchemaFilterSchemaFilterDbaasPostgreSQLPoolerSerializer(TypedDict, total=False):
    field: Required[Literal["last_name", "type", "uuid"]]
    """Field name to filter by"""

    type: Required[Literal["dbaas_postgresql_connection_pooler"]]

    values: Required[SequenceNotStr[str]]
    """List of field values to filter"""


SchemaFilter: TypeAlias = Union[
    SchemaFilterSchemaFilterSnapshotSerializer,
    SchemaFilterSchemaFilterInstanceSerializer,
    SchemaFilterSchemaFilterAIClusterSerializer,
    SchemaFilterSchemaFilterAIVirtualClusterSerializer,
    SchemaFilterSchemaFilterBasicVmSerializer,
    SchemaFilterSchemaFilterBaremetalSerializer,
    SchemaFilterSchemaFilterVolumeSerializer,
    SchemaFilterSchemaFilterFileShareSerializer,
    SchemaFilterSchemaFilterImageSerializer,
    SchemaFilterSchemaFilterFloatingIPSerializer,
    SchemaFilterSchemaFilterEgressTrafficSerializer,
    SchemaFilterSchemaFilterLoadBalancerSerializer,
    SchemaFilterSchemaFilterExternalIPSerializer,
    SchemaFilterSchemaFilterBackupSerializer,
    SchemaFilterSchemaFilterLogIndexSerializer,
    SchemaFilterSchemaFilterFunctionsSerializer,
    SchemaFilterSchemaFilterFunctionsCallsSerializer,
    SchemaFilterSchemaFilterFunctionsTrafficSerializer,
    SchemaFilterSchemaFilterContainersSerializer,
    SchemaFilterSchemaFilterInferenceSerializer,
    SchemaFilterSchemaFilterDbaasPostgreSQLVolumeSerializer,
    SchemaFilterSchemaFilterDbaasPostgreSQLPublicNetworkSerializer,
    SchemaFilterSchemaFilterDbaasPostgreSqlcpuSerializer,
    SchemaFilterSchemaFilterDbaasPostgreSQLMemorySerializer,
    SchemaFilterSchemaFilterDbaasPostgreSQLPoolerSerializer,
]


class TagsCondition(TypedDict, total=False):
    key: str
    """The name of the tag to filter (e.g., '`os_version`')."""

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
