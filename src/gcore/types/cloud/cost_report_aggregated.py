# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CostReportAggregated",
    "Result",
    "ResultTotalAIClusterWithCostSerializer",
    "ResultTotalAIVirtualClusterWithCostSerializer",
    "ResultTotalBaremetalWithCostSerializer",
    "ResultTotalBasicVmWithCostSerializer",
    "ResultTotalBackupWithCostSerializer",
    "ResultTotalContainerWithCostSerializer",
    "ResultTotalEgressTrafficWithCostSerializer",
    "ResultTotalExternalIPWithCostSerializer",
    "ResultTotalFileShareWithCostSerializer",
    "ResultTotalFloatingIPWithCostSerializer",
    "ResultTotalFunctionsWithCostSerializer",
    "ResultTotalFunctionCallsWithCostSerializer",
    "ResultTotalFunctionEgressTrafficWithCostSerializer",
    "ResultTotalImagesWithCostSerializer",
    "ResultTotalInferenceWithCostSerializer",
    "ResultTotalInstanceWithCostSerializer",
    "ResultTotalLoadBalancerWithCostSerializer",
    "ResultTotalLogIndexWithCostSerializer",
    "ResultTotalSnapshotWithCostSerializer",
    "ResultTotalVolumeWithCostSerializer",
    "ResultTotalDbaasPostgreSQLPoolerWithCostSerializer",
    "ResultTotalDbaasPostgreSQLMemoryWithCostSerializer",
    "ResultTotalDbaasPostgreSQLPublicNetworkWithCostSerializer",
    "ResultTotalDbaasPostgreSqlcpuWithCostSerializer",
    "ResultTotalDbaasPostgreSQLVolumeWithCostSerializer",
]


class ResultTotalAIClusterWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the Baremetal GPU cluster"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["ai_cluster"]


class ResultTotalAIVirtualClusterWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the Virtual GPU cluster"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["ai_virtual_cluster"]


class ResultTotalBaremetalWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the bare metal server"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["baremetal"]


class ResultTotalBasicVmWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the basic VM"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["basic_vm"]


class ResultTotalBackupWithCostSerializer(BaseModel):
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

    last_size: int
    """Size of the backup in bytes"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["backup"]


class ResultTotalContainerWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["containers"]


class ResultTotalEgressTrafficWithCostSerializer(BaseModel):
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

    instance_type: Literal["baremetal", "vm"]
    """Type of the instance"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["egress_traffic"]


class ResultTotalExternalIPWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["external_ip"]


class ResultTotalFileShareWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["file_share"]


class ResultTotalFloatingIPWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["floatingip"]


class ResultTotalFunctionsWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions"]


class ResultTotalFunctionCallsWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_calls"]


class ResultTotalFunctionEgressTrafficWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["functions_traffic"]


class ResultTotalImagesWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["image"]


class ResultTotalInferenceWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["inference"]


class ResultTotalInstanceWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the instance"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["instance"]


class ResultTotalLoadBalancerWithCostSerializer(BaseModel):
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

    flavor: str
    """Flavor of the load balancer"""

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["load_balancer"]


class ResultTotalLogIndexWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["log_index"]


class ResultTotalSnapshotWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["snapshot"]

    volume_type: str
    """Type of the volume"""


class ResultTotalVolumeWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["volume"]

    volume_type: str
    """Type of the volume"""


class ResultTotalDbaasPostgreSQLPoolerWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_connection_pooler"]


class ResultTotalDbaasPostgreSQLMemoryWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_memory"]


class ResultTotalDbaasPostgreSQLPublicNetworkWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_public_network"]


class ResultTotalDbaasPostgreSqlcpuWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_cpu"]


class ResultTotalDbaasPostgreSQLVolumeWithCostSerializer(BaseModel):
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

    region: int
    """Region ID"""

    region_id: int
    """Region ID"""

    type: Literal["dbaas_postgresql_volume"]

    volume_type: str
    """Type of the volume"""


Result: TypeAlias = Annotated[
    Union[
        ResultTotalAIClusterWithCostSerializer,
        ResultTotalAIVirtualClusterWithCostSerializer,
        ResultTotalBaremetalWithCostSerializer,
        ResultTotalBasicVmWithCostSerializer,
        ResultTotalBackupWithCostSerializer,
        ResultTotalContainerWithCostSerializer,
        ResultTotalEgressTrafficWithCostSerializer,
        ResultTotalExternalIPWithCostSerializer,
        ResultTotalFileShareWithCostSerializer,
        ResultTotalFloatingIPWithCostSerializer,
        ResultTotalFunctionsWithCostSerializer,
        ResultTotalFunctionCallsWithCostSerializer,
        ResultTotalFunctionEgressTrafficWithCostSerializer,
        ResultTotalImagesWithCostSerializer,
        ResultTotalInferenceWithCostSerializer,
        ResultTotalInstanceWithCostSerializer,
        ResultTotalLoadBalancerWithCostSerializer,
        ResultTotalLogIndexWithCostSerializer,
        ResultTotalSnapshotWithCostSerializer,
        ResultTotalVolumeWithCostSerializer,
        ResultTotalDbaasPostgreSQLPoolerWithCostSerializer,
        ResultTotalDbaasPostgreSQLMemoryWithCostSerializer,
        ResultTotalDbaasPostgreSQLPublicNetworkWithCostSerializer,
        ResultTotalDbaasPostgreSqlcpuWithCostSerializer,
        ResultTotalDbaasPostgreSQLVolumeWithCostSerializer,
    ],
    PropertyInfo(discriminator="type"),
]


class CostReportAggregated(BaseModel):
    count: int
    """Count of returned totals"""

    price_status: Literal["error", "hide", "show"]
    """Price status for the UI, type: string"""

    results: List[Result]
