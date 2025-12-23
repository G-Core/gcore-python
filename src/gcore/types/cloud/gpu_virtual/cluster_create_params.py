# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ClusterCreateParams",
    "ServersSettings",
    "ServersSettingsInterface",
    "ServersSettingsInterfaceExternalInterfaceInputSerializer",
    "ServersSettingsInterfaceSubnetInterfaceInputSerializer",
    "ServersSettingsInterfaceSubnetInterfaceInputSerializerFloatingIP",
    "ServersSettingsInterfaceAnySubnetInterfaceInputSerializer",
    "ServersSettingsInterfaceAnySubnetInterfaceInputSerializerFloatingIP",
    "ServersSettingsVolume",
    "ServersSettingsVolumeNewVolumeInputSerializer",
    "ServersSettingsVolumeImageVolumeInputSerializer",
    "ServersSettingsCredentials",
    "ServersSettingsFileShare",
    "ServersSettingsSecurityGroup",
]


class ClusterCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    flavor: Required[str]
    """Cluster flavor ID"""

    name: Required[str]
    """Cluster name"""

    servers_count: Required[int]
    """Number of servers in the cluster"""

    servers_settings: Required[ServersSettings]
    """Configuration settings for the servers in the cluster"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """


class ServersSettingsInterfaceExternalInterfaceInputSerializer(TypedDict, total=False):
    type: Required[Literal["external"]]

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6, or use dual stack."""

    name: str
    """Interface name"""


class ServersSettingsInterfaceSubnetInterfaceInputSerializerFloatingIP(TypedDict, total=False):
    """Floating IP config for this subnet attachment"""

    source: Required[Literal["new"]]


class ServersSettingsInterfaceSubnetInterfaceInputSerializer(TypedDict, total=False):
    network_id: Required[str]
    """Network ID the subnet belongs to. Port will be plugged in this network"""

    subnet_id: Required[str]
    """Port is assigned an IP address from this subnet"""

    type: Required[Literal["subnet"]]

    floating_ip: ServersSettingsInterfaceSubnetInterfaceInputSerializerFloatingIP
    """Floating IP config for this subnet attachment"""

    name: str
    """Interface name"""


class ServersSettingsInterfaceAnySubnetInterfaceInputSerializerFloatingIP(TypedDict, total=False):
    """Floating IP config for this subnet attachment"""

    source: Required[Literal["new"]]


class ServersSettingsInterfaceAnySubnetInterfaceInputSerializer(TypedDict, total=False):
    network_id: Required[str]
    """Network ID the subnet belongs to. Port will be plugged in this network"""

    type: Required[Literal["any_subnet"]]

    floating_ip: ServersSettingsInterfaceAnySubnetInterfaceInputSerializerFloatingIP
    """Floating IP config for this subnet attachment"""

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6, or use dual stack"""

    name: str
    """Interface name"""


ServersSettingsInterface: TypeAlias = Union[
    ServersSettingsInterfaceExternalInterfaceInputSerializer,
    ServersSettingsInterfaceSubnetInterfaceInputSerializer,
    ServersSettingsInterfaceAnySubnetInterfaceInputSerializer,
]


class ServersSettingsVolumeNewVolumeInputSerializer(TypedDict, total=False):
    boot_index: Required[int]
    """Boot index of the volume"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["new"]]

    type: Required[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Volume type"""

    delete_on_termination: bool
    """Flag indicating whether the volume is deleted on instance termination"""

    tags: Dict[str, str]
    """Tags associated with the volume"""


class ServersSettingsVolumeImageVolumeInputSerializer(TypedDict, total=False):
    boot_index: Required[int]
    """Boot index of the volume"""

    image_id: Required[str]
    """Image ID for the volume"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["image"]]

    type: Required[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Volume type"""

    delete_on_termination: bool
    """Flag indicating whether the volume is deleted on instance termination"""

    tags: Dict[str, str]
    """Tags associated with the volume"""


ServersSettingsVolume: TypeAlias = Union[
    ServersSettingsVolumeNewVolumeInputSerializer, ServersSettingsVolumeImageVolumeInputSerializer
]


class ServersSettingsCredentials(TypedDict, total=False):
    """Optional server access credentials"""

    password: str
    """Used to set the password for the specified 'username' on Linux instances.

    If 'username' is not provided, the password is applied to the default user of
    the image. Mutually exclusive with '`user_data`' - only one can be specified.
    """

    ssh_key_name: str
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """

    username: str
    """The 'username' and 'password' fields create a new user on the system"""


class ServersSettingsFileShare(TypedDict, total=False):
    id: Required[str]
    """Unique identifier of the file share in UUID format."""

    mount_path: Required[str]
    """Absolute mount path inside the system where the file share will be mounted."""


class ServersSettingsSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class ServersSettings(TypedDict, total=False):
    """Configuration settings for the servers in the cluster"""

    interfaces: Required[Iterable[ServersSettingsInterface]]
    """Subnet IPs and floating IPs"""

    volumes: Required[Iterable[ServersSettingsVolume]]
    """List of volumes"""

    credentials: ServersSettingsCredentials
    """Optional server access credentials"""

    file_shares: Iterable[ServersSettingsFileShare]
    """List of file shares to be mounted across the cluster."""

    security_groups: Iterable[ServersSettingsSecurityGroup]
    """List of security groups UUIDs"""

    user_data: str
    """Optional custom user data (Base64-encoded)"""
