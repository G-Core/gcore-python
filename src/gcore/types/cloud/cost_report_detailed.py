# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CostReportDetailed",
    "Result",
    "ResultResourceAIClusterWithCostSerializer",
    "ResultResourceAIVirtualClusterWithCostSerializer",
    "ResultResourceBaremetalWithCostSerializer",
    "ResultResourceBasicVmWithCostSerializer",
    "ResultResourceBackupWithCostSerializer",
    "ResultResourceContainerWithCostSerializer",
    "ResultResourceEgressTrafficWithCostSerializer",
    "ResultResourceExternalIPWithCostSerializer",
    "ResultResourceFileShareWithCostSerializer",
    "ResultResourceFloatingIPWithCostSerializer",
    "ResultResourceFunctionsWithCostSerializer",
    "ResultResourceFunctionCallsWithCostSerializer",
    "ResultResourceFunctionEgressTrafficWithCostSerializer",
    "ResultResourceImagesWithCostSerializer",
    "ResultResourceInferenceWithCostSerializer",
    "ResultResourceInstanceWithCostSerializer",
    "ResultResourceLoadBalancerWithCostSerializer",
    "ResultResourceLogIndexWithCostSerializer",
    "ResultResourceSnapshotWithCostSerializer",
    "ResultResourceVolumeWithCostSerializer",
    "ResultResourceDbaasPostgreSQLPoolerWithCostSerializer",
    "ResultResourceDbaasPostgreSQLMemoryWithCostSerializer",
    "ResultResourceDbaasPostgreSQLPublicNetworkWithCostSerializer",
    "ResultResourceDbaasPostgreSqlcpuWithCostSerializer",
    "ResultResourceDbaasPostgreSQLVolumeWithCostSerializer",
]


class ResultResourceAIClusterWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceAIVirtualClusterWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceBaremetalWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceBasicVmWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceBackupWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceContainerWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceEgressTrafficWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["bytes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceExternalIPWithCostSerializer(BaseModel):
    attached_to_vm: Optional[str] = None
    """ID of the VM the IP is attached to"""

    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceFileShareWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceFloatingIPWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceFunctionsWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GBS"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceFunctionCallsWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["MLS"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceFunctionEgressTrafficWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["GB"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceImagesWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceInferenceWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: str
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceInstanceWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceLoadBalancerWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceLogIndexWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceSnapshotWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceVolumeWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceDbaasPostgreSQLPoolerWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceDbaasPostgreSQLMemoryWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceDbaasPostgreSQLPublicNetworkWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceDbaasPostgreSqlcpuWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["minutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


class ResultResourceDbaasPostgreSQLVolumeWithCostSerializer(BaseModel):
    billing_feature_name: Optional[str] = None

    billing_metric_name: str
    """Name of the billing metric"""

    billing_value: float
    """Value of the billing metric"""

    billing_value_unit: Literal["gbminutes"]
    """Unit of billing value"""

    cost: Optional[float] = None
    """Cost for requested period"""

    currency: Optional[str] = None
    """Currency of the cost"""

    err: Optional[str] = None
    """Error message"""

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


Result: TypeAlias = Annotated[
    Union[
        ResultResourceAIClusterWithCostSerializer,
        ResultResourceAIVirtualClusterWithCostSerializer,
        ResultResourceBaremetalWithCostSerializer,
        ResultResourceBasicVmWithCostSerializer,
        ResultResourceBackupWithCostSerializer,
        ResultResourceContainerWithCostSerializer,
        ResultResourceEgressTrafficWithCostSerializer,
        ResultResourceExternalIPWithCostSerializer,
        ResultResourceFileShareWithCostSerializer,
        ResultResourceFloatingIPWithCostSerializer,
        ResultResourceFunctionsWithCostSerializer,
        ResultResourceFunctionCallsWithCostSerializer,
        ResultResourceFunctionEgressTrafficWithCostSerializer,
        ResultResourceImagesWithCostSerializer,
        ResultResourceInferenceWithCostSerializer,
        ResultResourceInstanceWithCostSerializer,
        ResultResourceLoadBalancerWithCostSerializer,
        ResultResourceLogIndexWithCostSerializer,
        ResultResourceSnapshotWithCostSerializer,
        ResultResourceVolumeWithCostSerializer,
        ResultResourceDbaasPostgreSQLPoolerWithCostSerializer,
        ResultResourceDbaasPostgreSQLMemoryWithCostSerializer,
        ResultResourceDbaasPostgreSQLPublicNetworkWithCostSerializer,
        ResultResourceDbaasPostgreSqlcpuWithCostSerializer,
        ResultResourceDbaasPostgreSQLVolumeWithCostSerializer,
    ],
    PropertyInfo(discriminator="type"),
]


class CostReportDetailed(BaseModel):
    count: int
    """Count of all the resources"""

    price_status: Literal["error", "hide", "show"]
    """Price status for the UI, type: string"""

    results: List[Result]
