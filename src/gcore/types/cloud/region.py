# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Region", "Coordinates"]


class Coordinates(BaseModel):
    latitude: float
    """
    '#/components/schemas/Coordinate/properties/latitude'
    "$.components.schemas.Coordinate.properties.latitude"
    """

    longitude: float
    """
    '#/components/schemas/Coordinate/properties/longitude'
    "$.components.schemas.Coordinate.properties.longitude"
    """


class Region(BaseModel):
    id: int
    """
    '#/components/schemas/RegionSerializer/properties/id'
    "$.components.schemas.RegionSerializer.properties.id"
    """

    access_level: Literal["core", "edge"]
    """
    '#/components/schemas/RegionSerializer/properties/access_level'
    "$.components.schemas.RegionSerializer.properties.access_level"
    """

    ai_service_endpoint_id: Optional[int] = None
    """
    '#/components/schemas/RegionSerializer/properties/ai_service_endpoint_id/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.ai_service_endpoint_id.anyOf[0]"
    """

    available_volume_types: Optional[List[str]] = None
    """
    '#/components/schemas/RegionSerializer/properties/available_volume_types/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.available_volume_types.anyOf[0]"
    """

    coordinates: Optional[Coordinates] = None
    """
    '#/components/schemas/RegionSerializer/properties/coordinates/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.coordinates.anyOf[0]"
    """

    country: Optional[str] = None
    """
    '#/components/schemas/RegionSerializer/properties/country/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.country.anyOf[0]"
    """

    created_at: datetime
    """
    '#/components/schemas/RegionSerializer/properties/created_at'
    "$.components.schemas.RegionSerializer.properties.created_at"
    """

    created_on: datetime
    """
    '#/components/schemas/RegionSerializer/properties/created_on'
    "$.components.schemas.RegionSerializer.properties.created_on"
    """

    ddos_endpoint_id: Optional[int] = None
    """
    '#/components/schemas/RegionSerializer/properties/ddos_endpoint_id/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.ddos_endpoint_id.anyOf[0]"
    """

    display_name: str
    """
    '#/components/schemas/RegionSerializer/properties/display_name'
    "$.components.schemas.RegionSerializer.properties.display_name"
    """

    endpoint_type: Literal["admin", "internal", "public"]
    """
    '#/components/schemas/RegionSerializer/properties/endpoint_type'
    "$.components.schemas.RegionSerializer.properties.endpoint_type"
    """

    external_network_id: Optional[str] = None
    """
    '#/components/schemas/RegionSerializer/properties/external_network_id/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.external_network_id.anyOf[0]"
    """

    file_share_types: Optional[List[Literal["standard", "vast"]]] = None
    """
    '#/components/schemas/RegionSerializer/properties/file_share_types/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.file_share_types.anyOf[0]"
    """

    has_ai: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_ai'
    "$.components.schemas.RegionSerializer.properties.has_ai"
    """

    has_ai_gpu: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_ai_gpu'
    "$.components.schemas.RegionSerializer.properties.has_ai_gpu"
    """

    has_baremetal: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_baremetal'
    "$.components.schemas.RegionSerializer.properties.has_baremetal"
    """

    has_basic_vm: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_basic_vm'
    "$.components.schemas.RegionSerializer.properties.has_basic_vm"
    """

    has_k8s: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_k8s'
    "$.components.schemas.RegionSerializer.properties.has_k8s"
    """

    has_kvm: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_kvm'
    "$.components.schemas.RegionSerializer.properties.has_kvm"
    """

    has_sfs: bool
    """
    '#/components/schemas/RegionSerializer/properties/has_sfs'
    "$.components.schemas.RegionSerializer.properties.has_sfs"
    """

    keystone_id: int
    """
    '#/components/schemas/RegionSerializer/properties/keystone_id'
    "$.components.schemas.RegionSerializer.properties.keystone_id"
    """

    keystone_name: str
    """
    '#/components/schemas/RegionSerializer/properties/keystone_name'
    "$.components.schemas.RegionSerializer.properties.keystone_name"
    """

    metrics_database_id: Optional[int] = None
    """
    '#/components/schemas/RegionSerializer/properties/metrics_database_id/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.metrics_database_id.anyOf[0]"
    """

    state: Literal["ACTIVE", "DELETED", "DELETING", "DELETION_FAILED", "INACTIVE", "MAINTENANCE", "NEW"]
    """
    '#/components/schemas/RegionSerializer/properties/state'
    "$.components.schemas.RegionSerializer.properties.state"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/RegionSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.task_id.anyOf[0]"
    """

    vlan_physical_network: str
    """
    '#/components/schemas/RegionSerializer/properties/vlan_physical_network'
    "$.components.schemas.RegionSerializer.properties.vlan_physical_network"
    """

    zone: Optional[Literal["AMERICAS", "APAC", "EMEA", "RUSSIA_AND_CIS"]] = None
    """
    '#/components/schemas/RegionSerializer/properties/zone/anyOf/0'
    "$.components.schemas.RegionSerializer.properties.zone.anyOf[0]"
    """

    has_dbaas: Optional[bool] = None
    """
    '#/components/schemas/RegionSerializer/properties/has_dbaas'
    "$.components.schemas.RegionSerializer.properties.has_dbaas"
    """
