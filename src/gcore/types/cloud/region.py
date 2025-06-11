# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Region", "Coordinates"]


class Coordinates(BaseModel):
    latitude: float

    longitude: float


class Region(BaseModel):
    id: int
    """Region ID"""

    access_level: Literal["core", "edge"]
    """The access level of the region."""

    ai_service_endpoint_id: Optional[int] = None
    """AI service API endpoint ID"""

    available_volume_types: Optional[List[str]] = None
    """List of available volume types, 'standard', '`ssd_hiiops`', 'cold']."""

    coordinates: Optional[Coordinates] = None
    """Coordinates of the region"""

    country: Optional[str] = None
    """Country"""

    created_at: datetime
    """Region creation date and time"""

    created_on: datetime
    """This field is deprecated. Use `created_at` instead."""

    ddos_endpoint_id: Optional[int] = None
    """DDoS endpoint ID"""

    display_name: str
    """Human-readable region name"""

    endpoint_type: Literal["admin", "internal", "public"]
    """Endpoint type"""

    external_network_id: Optional[str] = None
    """External network ID for Neutron"""

    file_share_types: Optional[List[Literal["standard", "vast"]]] = None
    """List of available file share types"""

    has_ai: bool
    """Region has AI capability"""

    has_ai_gpu: bool
    """Region has AI GPU capability"""

    has_baremetal: bool
    """Region has bare metal capability"""

    has_basic_vm: bool
    """Region has basic vm capability"""

    has_dbaas: bool
    """Region has DBAAS service"""

    has_k8s: bool
    """Region has managed kubernetes capability"""

    has_kvm: bool
    """Region has KVM virtualization capability"""

    has_sfs: bool
    """Region has SFS capability"""

    keystone_id: int
    """Foreign key to Keystone entity"""

    keystone_name: str
    """Technical region name"""

    metrics_database_id: Optional[int] = None
    """Foreign key to Metrics database entity"""

    state: Literal["ACTIVE", "DELETED", "DELETING", "DELETION_FAILED", "INACTIVE", "MAINTENANCE", "NEW"]
    """Region state"""

    task_id: Optional[str] = None
    """This field is deprecated and can be ignored"""

    vlan_physical_network: str
    """Physical network name to create vlan networks"""

    zone: Optional[Literal["AMERICAS", "APAC", "EMEA", "RUSSIA_AND_CIS"]] = None
    """Geographical zone"""
