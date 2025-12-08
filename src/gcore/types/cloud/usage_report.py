# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "UsageReport",
    "Resource",
    "ResourceResourceAIClusterSerializer",
    "ResourceResourceAIVirtualClusterSerializer",
    "ResourceResourceBaremetalSerializer",
    "ResourceResourceBasicVmSerializer",
    "ResourceResourceBackupSerializer",
    "ResourceResourceContainerSerializer",
    "ResourceResourceEgressTrafficSerializer",
    "ResourceResourceExternalIPSerializer",
    "ResourceResourceFileShareSerializer",
    "ResourceResourceFloatingIPSerializer",
    "ResourceResourceFunctionsSerializer",
    "ResourceResourceFunctionCallsSerializer",
    "ResourceResourceFunctionEgressTrafficSerializer",
    "ResourceResourceImagesSerializer",
    "ResourceResourceInferenceSerializer",
    "ResourceResourceInstanceSerializer",
    "ResourceResourceLoadBalancerSerializer",
    "ResourceResourceLogIndexSerializer",
    "ResourceResourceSnapshotSerializer",
    "ResourceResourceVolumeSerializer",
    "ResourceResourceDbaasPostgreSQLPoolerSerializer",
    "ResourceResourceDbaasPostgreSQLMemorySerializer",
    "ResourceResourceDbaasPostgreSQLPublicNetworkSerializer",
    "ResourceResourceDbaasPostgreSqlcpuSerializer",
    "ResourceResourceDbaasPostgreSQLVolumeSerializer",
    "Total",
    "TotalTotalAIClusterReportItemSerializer",
    "TotalTotalAIVirtualClusterReportItemSerializer",
    "TotalTotalBaremetalReportItemSerializer",
    "TotalTotalBasicVmReportItemSerializer",
    "TotalTotalContainerReportItemSerializer",
    "TotalTotalEgressTrafficReportItemSerializer",
    "TotalTotalExternalIPReportItemSerializer",
    "TotalTotalFileShareReportItemSerializer",
    "TotalTotalFloatingIPReportItemSerializer",
    "TotalTotalFunctionsReportItemSerializer",
    "TotalTotalFunctionCallsReportItemSerializer",
    "TotalTotalFunctionEgressTrafficReportItemSerializer",
    "TotalTotalImagesReportItemSerializer",
    "TotalTotalInferenceReportItemSerializer",
    "TotalTotalInstanceReportItemSerializer",
    "TotalTotalLoadBalancerReportItemSerializer",
    "TotalTotalLogIndexReportItemSerializer",
    "TotalTotalSnapshotReportItemSerializer",
    "TotalTotalVolumeReportItemSerializer",
    "TotalTotalDbaasPostgreSQLPoolerReportItemSerializer",
    "TotalTotalDbaasPostgreSQLMemoryReportItemSerializer",
    "TotalTotalDbaasPostgreSQLPublicNetworkReportItemSerializer",
    "TotalTotalDbaasPostgreSqlcpuReportItemSerializer",
    "TotalTotalDbaasPostgreSQLVolumeReportItemSerializer",
]


class ResourceResourceAIClusterSerializer(BaseModel):
    """
    These properties are common for all individual AI clusters
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the Baremetal GPU cluster"""

    last_name: str
    """Name of the AI cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["ai_cluster"]

    uuid: str
    """UUID of the Baremetal GPU cluster"""


class ResourceResourceAIVirtualClusterSerializer(BaseModel):
    """
    These properties are common for all individual AI Virtual clusters
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the Virtual GPU cluster"""

    last_name: str
    """Name of the AI cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["ai_virtual_cluster"]

    uuid: str
    """UUID of the Virtual GPU cluster"""


class ResourceResourceBaremetalSerializer(BaseModel):
    """
    These properties are common for all individual bare metal servers
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the bare metal server"""

    last_name: str
    """Name of the bare metal server"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["baremetal"]

    uuid: str
    """UUID of the bare metal server"""


class ResourceResourceBasicVmSerializer(BaseModel):
    """
    These properties are common for all individual basic VMs
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the basic VM"""

    last_name: str
    """Name of the basic VM"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["basic_vm"]

    uuid: str
    """UUID of the basic VM"""


class ResourceResourceBackupSerializer(BaseModel):
    """
    These properties are common for all individual backups
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the backup"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the backup in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    schedule_id: str
    """ID of the backup schedule"""

    source_volume_uuid: str
    """UUID of the source volume"""

    type: Literal["backup"]

    uuid: str
    """UUID of the backup"""


class ResourceResourceContainerSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the container"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["containers"]

    uuid: str
    """UUID of the container"""


class ResourceResourceEgressTrafficSerializer(BaseModel):
    """
    These properties are common for all individual egress traffic
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["bytes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    instance_type: Literal["baremetal", "vm"]
    """Type of the instance"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    port_id: str
    """ID of the port the traffic is associated with"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: str
    """Unit of size"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["egress_traffic"]

    vm_id: str
    """ID of the bare metal server the traffic is associated with"""

    instance_name: Optional[str] = None
    """Name of the instance"""


class ResourceResourceExternalIPSerializer(BaseModel):
    """
    These properties are common for all individual external IPs
    in all cost and usage reports results (but not in totals)
    """

    attached_to_vm: Optional[str] = None
    """ID of the VM the IP is attached to"""

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    ip_address: str
    """IP address"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    network_id: str
    """ID of the network the IP is attached to"""

    port_id: str
    """ID of the port the IP is associated with"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    subnet_id: str
    """ID of the subnet the IP is attached to"""

    type: Literal["external_ip"]


class ResourceResourceFileShareSerializer(BaseModel):
    """
    These properties are common for all individual file shares
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    file_share_type: str
    """Type of the file share"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the file share"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the file share in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: Literal["GiB"]
    """Unit of size"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["file_share"]

    uuid: str
    """UUID of the file share"""


class ResourceResourceFloatingIPSerializer(BaseModel):
    """
    These properties are common for all individual floating IPs
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    ip_address: str
    """IP address"""

    last_name: str
    """Name of the floating IP"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["floatingip"]

    uuid: str
    """UUID of the floating IP"""


class ResourceResourceFunctionsSerializer(BaseModel):
    """
    These properties are common for all individual functions
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the function"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions"]

    uuid: str
    """UUID of the function"""


class ResourceResourceFunctionCallsSerializer(BaseModel):
    """
    These properties are common for all individual function calls
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["MLS"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the function call"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_calls"]

    uuid: str
    """UUID of the function call"""


class ResourceResourceFunctionEgressTrafficSerializer(BaseModel):
    """
    These properties are common for all individual function egress traffic
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GB"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the function egress traffic"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_traffic"]

    uuid: str
    """UUID of the function egress traffic"""


class ResourceResourceImagesSerializer(BaseModel):
    """
    These properties are common for all individual images
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the image"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the image in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: Literal["bytes"]
    """Unit of size"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["image"]

    uuid: str
    """UUID of the image"""


class ResourceResourceInferenceSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: str
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the inference deployment"""

    last_name: str
    """Name of the inference deployment"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["inference"]

    uuid: str
    """UUID of the inference deployment"""


class ResourceResourceInstanceSerializer(BaseModel):
    """
    These properties are common for all individual instances
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the instance"""

    last_name: str
    """Name of the instance"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["instance"]

    uuid: str
    """UUID of the instance"""


class ResourceResourceLoadBalancerSerializer(BaseModel):
    """
    These properties are common for all individual load balancers
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    flavor: str
    """Flavor of the load balancer"""

    last_name: str
    """Name of the load balancer"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["load_balancer"]

    uuid: str
    """UUID of the load balancer"""


class ResourceResourceLogIndexSerializer(BaseModel):
    """
    These properties are common for all individual log indexes
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the log index"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the log index in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: str
    """Unit of size"""

    type: Literal["log_index"]

    uuid: Optional[str] = None
    """UUID of the log index"""


class ResourceResourceSnapshotSerializer(BaseModel):
    """
    These properties are common for all individual snapshots
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the snapshot"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the snapshot in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: str
    """Unit of size"""

    source_volume_uuid: str
    """UUID of the source volume"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["snapshot"]

    uuid: str
    """UUID of the snapshot"""

    volume_type: str
    """Type of the volume"""


class ResourceResourceVolumeSerializer(BaseModel):
    """
    These properties are common for all individual volumes
    in all cost and usage reports results (but not in totals)
    """

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the volume"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    last_size: int
    """Size of the volume in bytes"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: str
    """Unit of size"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal["volume"]

    uuid: str
    """UUID of the volume"""

    volume_type: str
    """Type of the volume"""

    attached_to_vm: Optional[str] = None
    """ID of the VM the volume is attached to"""


class ResourceResourceDbaasPostgreSQLPoolerSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_connection_pooler"]

    uuid: str
    """UUID of the cluster"""


class ResourceResourceDbaasPostgreSQLMemorySerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_memory"]

    uuid: str
    """UUID of the cluster"""


class ResourceResourceDbaasPostgreSQLPublicNetworkSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_public_network"]

    uuid: str
    """UUID of the cluster"""


class ResourceResourceDbaasPostgreSqlcpuSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_cpu"]

    uuid: str
    """UUID of the cluster"""


class ResourceResourceDbaasPostgreSQLVolumeSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_name: str
    """Name of the cluster"""

    last_seen: datetime
    """Last time the resource was seen in the given period"""

    project_id: int
    """ID of the project the resource belongs to"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    size_unit: str
    """Unit of size"""

    type: Literal["dbaas_postgresql_volume"]

    uuid: str
    """UUID of the cluster"""

    volume_type: str
    """Type of the volume"""


Resource: TypeAlias = Annotated[
    Union[
        ResourceResourceAIClusterSerializer,
        ResourceResourceAIVirtualClusterSerializer,
        ResourceResourceBaremetalSerializer,
        ResourceResourceBasicVmSerializer,
        ResourceResourceBackupSerializer,
        ResourceResourceContainerSerializer,
        ResourceResourceEgressTrafficSerializer,
        ResourceResourceExternalIPSerializer,
        ResourceResourceFileShareSerializer,
        ResourceResourceFloatingIPSerializer,
        ResourceResourceFunctionsSerializer,
        ResourceResourceFunctionCallsSerializer,
        ResourceResourceFunctionEgressTrafficSerializer,
        ResourceResourceImagesSerializer,
        ResourceResourceInferenceSerializer,
        ResourceResourceInstanceSerializer,
        ResourceResourceLoadBalancerSerializer,
        ResourceResourceLogIndexSerializer,
        ResourceResourceSnapshotSerializer,
        ResourceResourceVolumeSerializer,
        ResourceResourceDbaasPostgreSQLPoolerSerializer,
        ResourceResourceDbaasPostgreSQLMemorySerializer,
        ResourceResourceDbaasPostgreSQLPublicNetworkSerializer,
        ResourceResourceDbaasPostgreSqlcpuSerializer,
        ResourceResourceDbaasPostgreSQLVolumeSerializer,
    ],
    PropertyInfo(discriminator="type"),
]


class TotalTotalAIClusterReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the Baremetal GPU cluster"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["ai_cluster"]


class TotalTotalAIVirtualClusterReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the Virtual GPU cluster"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["ai_virtual_cluster"]


class TotalTotalBaremetalReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the bare metal server"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["baremetal"]


class TotalTotalBasicVmReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the basic VM"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["basic_vm"]


class TotalTotalContainerReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["containers"]


class TotalTotalEgressTrafficReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["bytes"]
    """Unit of billing value"""

    instance_type: Literal["baremetal", "vm"]
    """Type of the instance"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["egress_traffic"]


class TotalTotalExternalIPReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["external_ip"]


class TotalTotalFileShareReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    file_share_type: str
    """Type of the file share"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["file_share"]


class TotalTotalFloatingIPReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["floatingip"]


class TotalTotalFunctionsReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions"]


class TotalTotalFunctionCallsReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["MLS"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_calls"]


class TotalTotalFunctionEgressTrafficReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GB"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_traffic"]


class TotalTotalImagesReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["image"]


class TotalTotalInferenceReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: str
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["inference"]


class TotalTotalInstanceReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the instance"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["instance"]


class TotalTotalLoadBalancerReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    flavor: str
    """Flavor of the load balancer"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["load_balancer"]


class TotalTotalLogIndexReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["log_index"]


class TotalTotalSnapshotReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["snapshot"]

    volume_type: str
    """Type of the volume"""


class TotalTotalVolumeReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["volume"]

    volume_type: str
    """Type of the volume"""


class TotalTotalDbaasPostgreSQLPoolerReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_connection_pooler"]


class TotalTotalDbaasPostgreSQLMemoryReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_memory"]


class TotalTotalDbaasPostgreSQLPublicNetworkReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_public_network"]


class TotalTotalDbaasPostgreSqlcpuReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_cpu"]


class TotalTotalDbaasPostgreSQLVolumeReportItemSerializer(BaseModel):
    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_volume"]

    volume_type: str
    """Type of the volume"""


Total: TypeAlias = Annotated[
    Union[
        TotalTotalAIClusterReportItemSerializer,
        TotalTotalAIVirtualClusterReportItemSerializer,
        TotalTotalBaremetalReportItemSerializer,
        TotalTotalBasicVmReportItemSerializer,
        TotalTotalContainerReportItemSerializer,
        TotalTotalEgressTrafficReportItemSerializer,
        TotalTotalExternalIPReportItemSerializer,
        TotalTotalFileShareReportItemSerializer,
        TotalTotalFloatingIPReportItemSerializer,
        TotalTotalFunctionsReportItemSerializer,
        TotalTotalFunctionCallsReportItemSerializer,
        TotalTotalFunctionEgressTrafficReportItemSerializer,
        TotalTotalImagesReportItemSerializer,
        TotalTotalInferenceReportItemSerializer,
        TotalTotalInstanceReportItemSerializer,
        TotalTotalLoadBalancerReportItemSerializer,
        TotalTotalLogIndexReportItemSerializer,
        TotalTotalSnapshotReportItemSerializer,
        TotalTotalVolumeReportItemSerializer,
        TotalTotalDbaasPostgreSQLPoolerReportItemSerializer,
        TotalTotalDbaasPostgreSQLMemoryReportItemSerializer,
        TotalTotalDbaasPostgreSQLPublicNetworkReportItemSerializer,
        TotalTotalDbaasPostgreSqlcpuReportItemSerializer,
        TotalTotalDbaasPostgreSQLVolumeReportItemSerializer,
    ],
    PropertyInfo(discriminator="type"),
]


class UsageReport(BaseModel):
    count: int
    """Total count of the resources"""

    resources: List[Resource]

    totals: List[Total]
