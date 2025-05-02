# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily
from .tag_update_list_param import TagUpdateListParam

__all__ = [
    "GPUBaremetalClusterCreateParams",
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
]


class GPUBaremetalClusterCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    flavor: Required[str]
    """Flavor name"""

    image_id: Required[str]
    """Image ID"""

    interfaces: Required[Iterable[Interface]]
    """Subnet IPs and floating IPs"""

    name: Required[str]
    """GPU Cluster name"""

    instances_count: int
    """Number of servers to create"""

    password: str
    """A password for a bare metal server.

    This parameter is used to set a password for the "Admin" user on a Windows
    instance, a default user or a new user on a Linux instance
    """

    ssh_key_name: str
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

    Must not be passed together with 'username' or 'password'. Examples of the
    user_data: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """

    username: str
    """A name of a new user in the Linux instance.

    It may be passed with a 'password' parameter
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
