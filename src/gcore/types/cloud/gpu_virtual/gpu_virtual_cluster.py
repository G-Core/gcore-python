# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..tag import Tag
from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "GPUVirtualCluster",
    "ServersSettings",
    "ServersSettingsFileShare",
    "ServersSettingsInterface",
    "ServersSettingsInterfaceExternalInterfaceOutputSerializer",
    "ServersSettingsInterfaceSubnetInterfaceOutputSerializer",
    "ServersSettingsInterfaceSubnetInterfaceOutputSerializerFloatingIP",
    "ServersSettingsInterfaceAnySubnetInterfaceOutputSerializer",
    "ServersSettingsInterfaceAnySubnetInterfaceOutputSerializerFloatingIP",
    "ServersSettingsSecurityGroup",
    "ServersSettingsVolume",
]


class ServersSettingsFileShare(BaseModel):
    id: str
    """Unique identifier of the file share in UUID format."""

    mount_path: str
    """Absolute mount path inside the system where the file share will be mounted."""


class ServersSettingsInterfaceExternalInterfaceOutputSerializer(BaseModel):
    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6, or use dual stack."""

    name: Optional[str] = None
    """Interface name"""

    type: Literal["external"]


class ServersSettingsInterfaceSubnetInterfaceOutputSerializerFloatingIP(BaseModel):
    """Floating IP config for this subnet attachment"""

    source: Literal["new"]


class ServersSettingsInterfaceSubnetInterfaceOutputSerializer(BaseModel):
    floating_ip: Optional[ServersSettingsInterfaceSubnetInterfaceOutputSerializerFloatingIP] = None
    """Floating IP config for this subnet attachment"""

    name: Optional[str] = None
    """Interface name"""

    network_id: str
    """Network ID the subnet belongs to. Port will be plugged in this network"""

    subnet_id: str
    """Port is assigned an IP address from this subnet"""

    type: Literal["subnet"]


class ServersSettingsInterfaceAnySubnetInterfaceOutputSerializerFloatingIP(BaseModel):
    """Floating IP config for this subnet attachment"""

    source: Literal["new"]


class ServersSettingsInterfaceAnySubnetInterfaceOutputSerializer(BaseModel):
    floating_ip: Optional[ServersSettingsInterfaceAnySubnetInterfaceOutputSerializerFloatingIP] = None
    """Floating IP config for this subnet attachment"""

    ip_address: Optional[str] = None
    """Fixed IP address"""

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6, or use dual stack"""

    name: Optional[str] = None
    """Interface name"""

    network_id: str
    """Network ID the subnet belongs to. Port will be plugged in this network"""

    type: Literal["any_subnet"]


ServersSettingsInterface: TypeAlias = Annotated[
    Union[
        ServersSettingsInterfaceExternalInterfaceOutputSerializer,
        ServersSettingsInterfaceSubnetInterfaceOutputSerializer,
        ServersSettingsInterfaceAnySubnetInterfaceOutputSerializer,
    ],
    PropertyInfo(discriminator="type"),
]


class ServersSettingsSecurityGroup(BaseModel):
    id: str
    """Security group ID"""

    name: str
    """Security group name"""


class ServersSettingsVolume(BaseModel):
    boot_index: Optional[int] = None
    """Boot index of the volume"""

    delete_on_termination: bool
    """Flag indicating whether the volume is deleted on instance termination"""

    image_id: Optional[str] = None
    """Image ID for the volume"""

    name: str
    """Volume name"""

    size: int
    """Volume size in GiB"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type"""


class ServersSettings(BaseModel):
    file_shares: List[ServersSettingsFileShare]
    """List of file shares mounted across the cluster."""

    interfaces: List[ServersSettingsInterface]

    security_groups: List[ServersSettingsSecurityGroup]
    """Security groups"""

    ssh_key_name: Optional[str] = None
    """SSH key name"""

    user_data: Optional[str] = None
    """Optional custom user data"""

    volumes: List[ServersSettingsVolume]
    """List of volumes"""


class GPUVirtualCluster(BaseModel):
    id: str
    """Cluster unique identifier"""

    created_at: datetime
    """Cluster creation date time"""

    flavor: str
    """Cluster flavor name"""

    name: str
    """Cluster name"""

    servers_count: int
    """Cluster servers count"""

    servers_ids: List[str]
    """List of cluster nodes"""

    servers_settings: ServersSettings

    status: Literal["active", "deleting", "error", "new", "resizing"]
    """Cluster status"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    updated_at: Optional[datetime] = None
    """Cluster update date time"""
