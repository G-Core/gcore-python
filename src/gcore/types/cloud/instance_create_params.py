# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily

__all__ = [
    "InstanceCreateParams",
    "Interface",
    "InterfaceNewInterfaceExternalSerializerPydantic",
    "InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup",
    "InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic",
    "InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIP",
    "InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup",
    "InterfaceNewInterfaceAnySubnetFipSerializerPydantic",
    "InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIP",
    "InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup",
    "InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic",
    "InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIP",
    "InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup",
    "Volume",
    "VolumeCreateInstanceCreateNewVolumeSerializer",
    "VolumeCreateInstanceCreateVolumeFromImageSerializer",
    "VolumeCreateInstanceCreateVolumeFromSnapshotSerializer",
    "VolumeCreateInstanceCreateVolumeFromApptemplateSerializer",
    "VolumeCreateInstanceExistingVolumeSerializer",
    "SecurityGroup",
]


class InstanceCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    flavor: Required[str]
    """The flavor of the instance."""

    interfaces: Required[Iterable[Interface]]
    """A list of network interfaces for the instance.

    You can create one or more interfaces - private, public, or both.
    """

    volumes: Required[Iterable[Volume]]
    """List of volumes that will be attached to the instance."""

    allow_app_ports: bool
    """Set to `true` if creating the instance from an `apptemplate`.

    This allows application ports in the security group for instances created from a
    marketplace application template.
    """

    configuration: Optional[Dict[str, object]]
    """
    Parameters for the application template if creating the instance from an
    `apptemplate`.
    """

    name: str
    """Instance name."""

    name_template: str
    """
    If you want the instance name to be automatically generated based on IP
    addresses, you can provide a name template instead of specifying the name
    manually. The template should include a placeholder that will be replaced during
    provisioning. Supported placeholders are: `{ip_octets}` (last 3 octets of the
    IP), `{two_ip_octets}`, and `{one_ip_octet}`.
    """

    password: str
    """For Linux instances, 'username' and 'password' are used to create a new user.

    When only 'password' is provided, it is set as the password for the default user
    of the image. For Windows instances, 'username' cannot be specified. Use the
    'password' field to set the password for the 'Admin' user on Windows. Use the
    '`user_data`' field to provide a script to create new users on Windows. The
    password of the Admin user cannot be updated via '`user_data`'.
    """

    security_groups: Iterable[SecurityGroup]
    """
    Specifies security group UUIDs to be applied to all instance network interfaces.
    """

    servergroup_id: str
    """Placement group ID for instance placement policy.

    Supported group types:

    - `anti-affinity`: Ensures instances are placed on different hosts for high
      availability.
    - `affinity`: Places instances on the same host for low-latency communication.
    - `soft-anti-affinity`: Tries to place instances on different hosts but allows
      sharing if needed.
    """

    ssh_key_name: Optional[str]
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    user_data: str
    """String in base64 format.

    For Linux instances, '`user_data`' is ignored when 'password' field is provided.
    For Windows instances, Admin user password is set by 'password' field and cannot
    be updated via '`user_data`'. Examples of the `user_data`:
    https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """

    username: str
    """For Linux instances, 'username' and 'password' are used to create a new user.

    For Windows instances, 'username' cannot be specified. Use 'password' field to
    set the password for the 'Admin' user on Windows.
    """


class InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class InterfaceNewInterfaceExternalSerializerPydantic(TypedDict, total=False):
    """Instance will be attached to default external network"""

    type: Required[Literal["external"]]
    """A public IP address will be assigned to the instance."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_family: Optional[InterfaceIPFamily]
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""

    security_groups: Iterable[InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup]
    """Specifies security group UUIDs to be applied to the instance network interface."""


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    An existing available floating IP id must be specified if the source is set to
    `existing`
    """

    source: Required[Literal["existing"]]
    """An existing available floating IP will be attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic(TypedDict, total=False):
    """
    The instance will get an IP address from the selected network.
    If you choose to add a floating IP, the instance will be reachable from the internet.
    Otherwise, it will only have a private IP within the network.
    """

    network_id: Required[str]
    """The network where the instance will be connected."""

    subnet_id: Required[str]
    """The instance will get an IP address from this subnet."""

    type: Required[Literal["subnet"]]
    """The instance will get an IP address from the selected network.

    If you choose to add a floating IP, the instance will be reachable from the
    internet. Otherwise, it will only have a private IP within the network.
    """

    floating_ip: InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIP
    """Allows the instance to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    security_groups: Iterable[InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup]
    """Specifies security group UUIDs to be applied to the instance network interface."""


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    An existing available floating IP id must be specified if the source is set to
    `existing`
    """

    source: Required[Literal["existing"]]
    """An existing available floating IP will be attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class InterfaceNewInterfaceAnySubnetFipSerializerPydantic(TypedDict, total=False):
    network_id: Required[str]
    """The network where the instance will be connected."""

    type: Required[Literal["any_subnet"]]
    """Instance will be attached to a subnet with the largest count of free IPs."""

    floating_ip: InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIP
    """Allows the instance to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_address: str
    """You can specify a specific IP address from your subnet."""

    ip_family: Optional[InterfaceIPFamily]
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""

    security_groups: Iterable[InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup]
    """Specifies security group UUIDs to be applied to the instance network interface."""


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    An existing available floating IP id must be specified if the source is set to
    `existing`
    """

    source: Required[Literal["existing"]]
    """An existing available floating IP will be attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic(TypedDict, total=False):
    port_id: Required[str]
    """Network ID the subnet belongs to. Port will be plugged in this network."""

    type: Required[Literal["reserved_fixed_ip"]]
    """An existing available reserved fixed IP will be attached to the instance.

    If the reserved IP is not public and you choose to add a floating IP, the
    instance will be accessible from the internet.
    """

    floating_ip: InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIP
    """Allows the instance to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    security_groups: Iterable[InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup]
    """Specifies security group UUIDs to be applied to the instance network interface."""


Interface: TypeAlias = Union[
    InterfaceNewInterfaceExternalSerializerPydantic,
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic,
    InterfaceNewInterfaceAnySubnetFipSerializerPydantic,
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic,
]


class VolumeCreateInstanceCreateNewVolumeSerializer(TypedDict, total=False):
    size: Required[int]
    """Volume size in GiB."""

    source: Required[Literal["new-volume"]]
    """New volume will be created from scratch and attached to the instance."""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    delete_on_termination: bool
    """Set to `true` to automatically delete the volume when the instance is deleted."""

    name: str
    """The name of the volume.

    If not specified, a name will be generated automatically.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type name. Supported values:

    - `standard` - Network SSD block storage offering stable performance with high
      random I/O and data reliability (6 IOPS per 1 GiB, 0.4 MB/s per 1 GiB). Max
      IOPS: 4500. Max bandwidth: 300 MB/s.
    - `ssd_hiiops` - High-performance SSD storage for latency-sensitive
      transactional workloads (60 IOPS per 1 GiB, 2.5 MB/s per 1 GiB). Max
      IOPS: 9000. Max bandwidth: 500 MB/s.
    - `ssd_lowlatency` - SSD storage optimized for low-latency and real-time
      processing. Max IOPS: 5000. Average latency: 300 µs. Snapshots and volume
      resizing are **not** supported for `ssd_lowlatency`.
    """


class VolumeCreateInstanceCreateVolumeFromImageSerializer(TypedDict, total=False):
    image_id: Required[str]
    """Image ID."""

    source: Required[Literal["image"]]
    """New volume will be created from the image and attached to the instance.

    Specify `boot_index=0` to boot from this volume.
    """

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    boot_index: int
    """
    - `0` means that this is the primary boot device;
    - A unique positive value is set for the secondary bootable devices;
    - A negative number means that the boot is prohibited.
    """

    delete_on_termination: bool
    """Set to `true` to automatically delete the volume when the instance is deleted."""

    name: str
    """The name of the volume.

    If not specified, a name will be generated automatically.
    """

    size: int
    """Volume size in GiB.

    - For instances: **specify the desired volume size explicitly**.
    - For basic VMs: the size is set automatically based on the flavor.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type name. Supported values:

    - `standard` - Network SSD block storage offering stable performance with high
      random I/O and data reliability (6 IOPS per 1 GiB, 0.4 MB/s per 1 GiB). Max
      IOPS: 4500. Max bandwidth: 300 MB/s.
    - `ssd_hiiops` - High-performance SSD storage for latency-sensitive
      transactional workloads (60 IOPS per 1 GiB, 2.5 MB/s per 1 GiB). Max
      IOPS: 9000. Max bandwidth: 500 MB/s.
    - `ssd_lowlatency` - SSD storage optimized for low-latency and real-time
      processing. Max IOPS: 5000. Average latency: 300 µs. Snapshots and volume
      resizing are **not** supported for `ssd_lowlatency`.
    """


class VolumeCreateInstanceCreateVolumeFromSnapshotSerializer(TypedDict, total=False):
    size: Required[int]
    """Volume size in GiB."""

    snapshot_id: Required[str]
    """Snapshot ID."""

    source: Required[Literal["snapshot"]]
    """New volume will be created from the snapshot and attached to the instance."""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    boot_index: int
    """
    - `0` means that this is the primary boot device;
    - A unique positive value is set for the secondary bootable devices;
    - A negative number means that the boot is prohibited.
    """

    delete_on_termination: bool
    """Set to `true` to automatically delete the volume when the instance is deleted."""

    name: str
    """The name of the volume.

    If not specified, a name will be generated automatically.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["ssd_hiiops", "standard"]
    """Specifies the volume type.

    If omitted, the type from the source volume will be used by default.
    """


class VolumeCreateInstanceCreateVolumeFromApptemplateSerializer(TypedDict, total=False):
    apptemplate_id: Required[str]
    """App template ID."""

    source: Required[Literal["apptemplate"]]
    """New volume will be created from the app template and attached to the instance."""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    boot_index: int
    """
    - `0` means that this is the primary boot device;
    - A unique positive value is set for the secondary bootable devices;
    - A negative number means that the boot is prohibited.
    """

    delete_on_termination: bool
    """Set to `true` to automatically delete the volume when the instance is deleted."""

    name: str
    """The name of the volume.

    If not specified, a name will be generated automatically.
    """

    size: int
    """Volume size in GiB."""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type name. Supported values:

    - `standard` - Network SSD block storage offering stable performance with high
      random I/O and data reliability (6 IOPS per 1 GiB, 0.4 MB/s per 1 GiB). Max
      IOPS: 4500. Max bandwidth: 300 MB/s.
    - `ssd_hiiops` - High-performance SSD storage for latency-sensitive
      transactional workloads (60 IOPS per 1 GiB, 2.5 MB/s per 1 GiB). Max
      IOPS: 9000. Max bandwidth: 500 MB/s.
    - `ssd_lowlatency` - SSD storage optimized for low-latency and real-time
      processing. Max IOPS: 5000. Average latency: 300 µs. Snapshots and volume
      resizing are **not** supported for `ssd_lowlatency`.
    """


class VolumeCreateInstanceExistingVolumeSerializer(TypedDict, total=False):
    source: Required[Literal["existing-volume"]]
    """Existing available volume will be attached to the instance."""

    volume_id: Required[str]
    """Volume ID."""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    boot_index: int
    """
    - `0` means that this is the primary boot device;
    - A unique positive value is set for the secondary bootable devices;
    - A negative number means that the boot is prohibited.
    """

    delete_on_termination: bool
    """Set to `true` to automatically delete the volume when the instance is deleted."""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """


Volume: TypeAlias = Union[
    VolumeCreateInstanceCreateNewVolumeSerializer,
    VolumeCreateInstanceCreateVolumeFromImageSerializer,
    VolumeCreateInstanceCreateVolumeFromSnapshotSerializer,
    VolumeCreateInstanceCreateVolumeFromApptemplateSerializer,
    VolumeCreateInstanceExistingVolumeSerializer,
]


class SecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""
