# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily

__all__ = [
    "GPUBaremetalClusterCreateParams",
    "Interface",
    "InterfaceCreateGPUClusterExternalInterfaceSerializer",
    "InterfaceCreateGPUClusterSubnetInterfaceSerializer",
    "InterfaceCreateGPUClusterSubnetInterfaceSerializerFloatingIP",
    "InterfaceCreateGPUClusterAnySubnetInterfaceSerializer",
    "InterfaceCreateGPUClusterAnySubnetInterfaceSerializerFloatingIP",
]


class GPUBaremetalClusterCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    flavor: Required[str]
    """Flavor name"""

    image_id: Required[str]
    """Image ID"""

    interfaces: Required[Iterable[Interface]]
    """A list of network interfaces for the server.

    You can create one or more interfaces - private, public, or both.
    """

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
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """

    tags: Dict[str, str]
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
    `user_data`: https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """

    username: str
    """A name of a new user in the Linux instance.

    It may be passed with a 'password' parameter
    """


class InterfaceCreateGPUClusterExternalInterfaceSerializer(TypedDict, total=False):
    type: Required[Literal["external"]]
    """A public IP address will be assigned to the server."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_family: Optional[InterfaceIPFamily]
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""


class InterfaceCreateGPUClusterSubnetInterfaceSerializerFloatingIP(TypedDict, total=False):
    source: Required[Literal["new"]]


class InterfaceCreateGPUClusterSubnetInterfaceSerializer(TypedDict, total=False):
    network_id: Required[str]
    """The network where the server will be connected."""

    subnet_id: Required[str]
    """The server will get an IP address from this subnet."""

    type: Required[Literal["subnet"]]
    """The instance will get an IP address from the selected network.

    If you choose to add a floating IP, the instance will be reachable from the
    internet. Otherwise, it will only have a private IP within the network.
    """

    floating_ip: InterfaceCreateGPUClusterSubnetInterfaceSerializerFloatingIP
    """Floating IP config for this subnet attachment"""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """


class InterfaceCreateGPUClusterAnySubnetInterfaceSerializerFloatingIP(TypedDict, total=False):
    source: Required[Literal["new"]]


class InterfaceCreateGPUClusterAnySubnetInterfaceSerializer(TypedDict, total=False):
    network_id: Required[str]
    """The network where the server will be connected."""

    type: Required[Literal["any_subnet"]]
    """Server will be attached to a subnet with the largest count of free IPs."""

    floating_ip: InterfaceCreateGPUClusterAnySubnetInterfaceSerializerFloatingIP
    """Allows the server to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_address: str
    """You can specify a specific IP address from your subnet."""

    ip_family: InterfaceIPFamily
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""


Interface: TypeAlias = Union[
    InterfaceCreateGPUClusterExternalInterfaceSerializer,
    InterfaceCreateGPUClusterSubnetInterfaceSerializer,
    InterfaceCreateGPUClusterAnySubnetInterfaceSerializer,
]
