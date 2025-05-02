# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily
from .tag_update_list_param import TagUpdateListParam

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

    You can create one or more interfaces—private, public, or both.
    """

    volumes: Required[Iterable[Volume]]
    """List of volumes for instances"""

    allow_app_ports: bool
    """Set to `true` if creating the instance from an `apptemplate`.

    This allows application ports in the security group for instances created from a
    marketplace application template.
    """

    configuration: Optional[object]
    """
    Parameters for the application template if creating the instance from an
    `apptemplate`.
    """

    name_templates: List[str]
    """
    If you want instance names to be automatically generated using IP octets, you
    can specify name templates instead of setting names manually.Provide a list of
    templated names that should be replaced using the selected template. The
    following template formats are supported: `{ip_octets}`, `{two_ip_octets}`, and
    `{one_ip_octet}`.
    """

    names: List[str]
    """List of instance names. Specify one name to create a single instance."""

    password: str
    """For Linux instances, 'username' and 'password' are used to create a new user.

    When only 'password' is provided, it is set as the password for the default user
    of the image. For Windows instances, 'username' cannot be specified. Use the
    'password' field to set the password for the 'Admin' user on Windows. Use the
    'user_data' field to provide a script to create new users on Windows. The
    password of the Admin user cannot be updated via 'user_data'.
    """

    security_groups: Iterable[SecurityGroup]
    """Applies only to instances and is ignored for bare metal.

    Specifies security group UUIDs to be applied to all instance network interfaces.
    """

    servergroup_id: str
    """Server group ID for instance placement policy.

    Can be an anti-affinity, affinity, or soft-anti-affinity group. `anti-affinity`
    ensures instances are placed on different hosts for high availability.
    `affinity` places instances on the same host for low-latency communication.
    `soft-anti-affinity` tries to place instances on different hosts but allows
    sharing if needed.
    """

    ssh_key_name: Optional[str]
    """Specifies the name of the SSH keypair, created via the `/v1/ssh_keys` endpoint."""

    tags: TagUpdateListParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    user_data: str
    """String in base64 format.

    For Linux instances, 'user_data' is ignored when 'password' field is provided.
    For Windows instances, Admin user password is set by 'password' field and cannot
    be updated via 'user_data'. Examples of the user_data:
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
    type: Required[Literal["external"]]
    """A public IP address will be assigned to the instance."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_family: Optional[InterfaceIPFamily]
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""

    port_group: int
    """Applicable only to bare metal. Each group is added to a separate trunk."""

    security_groups: Iterable[InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup]
    """Applies only to instances and is ignored for bare metal.

    Specifies security group UUIDs to be applied to the instance network interface.
    """


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

    port_group: int
    """Applicable only to bare metal. Each group is added to a separate trunk."""

    security_groups: Iterable[InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup]
    """Applies only to instances and is ignored for bare metal.

    Specifies security group UUIDs to be applied to the instance network interface.
    """


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

    port_group: int
    """Applicable only to bare metal. Each group is added to a separate trunk."""

    security_groups: Iterable[InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup]
    """Applies only to instances and is ignored for bare metal.

    Specifies security group UUIDs to be applied to the instance network interface.
    """


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

    port_group: int
    """Applicable only to bare metal. Each group is added to a separate trunk."""

    security_groups: Iterable[InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup]
    """Applies only to instances and is ignored for bare metal.

    Specifies security group UUIDs to be applied to the instance network interface.
    """


Interface: TypeAlias = Union[
    InterfaceNewInterfaceExternalSerializerPydantic,
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic,
    InterfaceNewInterfaceAnySubnetFipSerializerPydantic,
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic,
]


class Volume(TypedDict, total=False):
    source: Required[Literal["apptemplate", "existing-volume", "image", "new-volume", "snapshot"]]
    """Volume source.

    For `image`, specify `image_id` and `size`. For `new-volume`, specify `size`.
    For `existing-volume`, specify `volume_id`. For `snapshot`, specify
    `snapshot_id`. For `apptemplate`, specify `apptemplate_id`.
    """

    apptemplate_id: str
    """App template ID. Required if `source` is `apptemplate`"""

    attachment_tag: str
    """Block device attachment tag (not exposed in the normal tags)"""

    boot_index: int
    """0 means that this is the primary boot device.

    A unique positive value is set for the other bootable devices. A negative number
    means that the boot is prohibited.
    """

    delete_on_termination: bool
    """Whether the volume should be deleted along with the VM"""

    image_id: str
    """Image ID. Required if `source` is `image`"""

    name: str
    """The name of the volume.

    If not specified, a name will be generated automatically.
    """

    size: int
    """Required when the `source` is either `new-volume` or `image`.

    If specified for the `snapshot` or `existing-volume` `source`, the value must
    match the size of the snapshot or the existing volume, respectively.
    """

    snapshot_id: str
    """Volume snapshot ID. Required if `source` is `snapshot`"""

    tags: TagUpdateListParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """Volume type name.

    Supported values: `standard` – Network SSD block storage offering stable
    performance with high random I/O and data reliability (6 IOPS per 1 GiB, 0.4
    MB/s per 1 GiB). Max IOPS: 4500. Max bandwidth: 300 MB/s. `ssd_hiiops` –
    High-performance SSD storage for latency-sensitive transactional workloads (60
    IOPS per 1 GiB, 2.5 MB/s per 1 GiB). Max IOPS: 9000. Max bandwidth: 500 MB/s.
    `ssd_lowlatency` – SSD storage optimized for low-latency and real-time
    processing. Max IOPS: 5000. Average latency: 300 µs. Snapshots and volume
    resizing are not supported for `ssd_lowlatency`.
    """

    volume_id: str
    """Volume ID. Required if `source` is `existing-volume`"""


class SecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""
