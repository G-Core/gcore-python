# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily

__all__ = [
    "ReservedFixedIPCreateParams",
    "NewReservedFixedIPExternalSerializer",
    "NewReservedFixedIPSpecificSubnetSerializer",
    "NewReservedFixedIPAnySubnetSerializer",
    "NewReservedFixedIPSpecificIPAddressSerializer",
    "NewReservedFixedIPSpecificPortSerializer",
]


class NewReservedFixedIPExternalSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    type: Required[Literal["external"]]
    """Must be 'external'"""

    ip_family: Optional[InterfaceIPFamily]
    """Which subnets should be selected: IPv4, IPv6 or use dual stack."""

    is_vip: bool
    """If reserved fixed IP is a VIP"""


class NewReservedFixedIPSpecificSubnetSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    subnet_id: Required[str]
    """Reserved fixed IP will be allocated in this subnet"""

    type: Required[Literal["subnet"]]
    """Must be 'subnet'."""

    is_vip: bool
    """If reserved fixed IP is a VIP"""


class NewReservedFixedIPAnySubnetSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    network_id: Required[str]
    """Reserved fixed IP will be allocated in a subnet of this network"""

    type: Required[Literal["any_subnet"]]
    """Must be '`any_subnet`'."""

    ip_family: Optional[InterfaceIPFamily]
    """Which subnets should be selected: IPv4, IPv6 or use dual stack."""

    is_vip: bool
    """If reserved fixed IP is a VIP"""


class NewReservedFixedIPSpecificIPAddressSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    ip_address: Required[str]
    """Reserved fixed IP will be allocated the given IP address"""

    network_id: Required[str]
    """Reserved fixed IP will be allocated in a subnet of this network"""

    type: Required[Literal["ip_address"]]
    """Must be '`ip_address`'."""

    is_vip: bool
    """If reserved fixed IP is a VIP"""


class NewReservedFixedIPSpecificPortSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    port_id: Required[str]
    """
    Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
    Balancer entity).
    """

    type: Required[Literal["port"]]
    """Must be 'port'."""


ReservedFixedIPCreateParams: TypeAlias = Union[
    NewReservedFixedIPExternalSerializer,
    NewReservedFixedIPSpecificSubnetSerializer,
    NewReservedFixedIPAnySubnetSerializer,
    NewReservedFixedIPSpecificIPAddressSerializer,
    NewReservedFixedIPSpecificPortSerializer,
]
