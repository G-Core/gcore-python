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
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    type: Required[Literal["external"]]
    """
    '#/components/schemas/NewReservedFixedIpExternalSerializer/properties/type'
    "$.components.schemas.NewReservedFixedIpExternalSerializer.properties.type"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/NewReservedFixedIpExternalSerializer/properties/ip_family/anyOf/0'
    "$.components.schemas.NewReservedFixedIpExternalSerializer.properties.ip_family.anyOf[0]"
    """

    is_vip: bool
    """
    '#/components/schemas/NewReservedFixedIpExternalSerializer/properties/is_vip'
    "$.components.schemas.NewReservedFixedIpExternalSerializer.properties.is_vip"
    """


class NewReservedFixedIPSpecificSubnetSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    subnet_id: Required[str]
    """
    '#/components/schemas/NewReservedFixedIpSpecificSubnetSerializer/properties/subnet_id'
    "$.components.schemas.NewReservedFixedIpSpecificSubnetSerializer.properties.subnet_id"
    """

    type: Required[Literal["subnet"]]
    """
    '#/components/schemas/NewReservedFixedIpSpecificSubnetSerializer/properties/type'
    "$.components.schemas.NewReservedFixedIpSpecificSubnetSerializer.properties.type"
    """

    is_vip: bool
    """
    '#/components/schemas/NewReservedFixedIpSpecificSubnetSerializer/properties/is_vip'
    "$.components.schemas.NewReservedFixedIpSpecificSubnetSerializer.properties.is_vip"
    """


class NewReservedFixedIPAnySubnetSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    network_id: Required[str]
    """
    '#/components/schemas/NewReservedFixedIpAnySubnetSerializer/properties/network_id'
    "$.components.schemas.NewReservedFixedIpAnySubnetSerializer.properties.network_id"
    """

    type: Required[Literal["any_subnet"]]
    """
    '#/components/schemas/NewReservedFixedIpAnySubnetSerializer/properties/type'
    "$.components.schemas.NewReservedFixedIpAnySubnetSerializer.properties.type"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/NewReservedFixedIpAnySubnetSerializer/properties/ip_family/anyOf/0'
    "$.components.schemas.NewReservedFixedIpAnySubnetSerializer.properties.ip_family.anyOf[0]"
    """

    is_vip: bool
    """
    '#/components/schemas/NewReservedFixedIpAnySubnetSerializer/properties/is_vip'
    "$.components.schemas.NewReservedFixedIpAnySubnetSerializer.properties.is_vip"
    """


class NewReservedFixedIPSpecificIPAddressSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    ip_address: Required[str]
    """
    '#/components/schemas/NewReservedFixedIpSpecificIpAddressSerializer/properties/ip_address'
    "$.components.schemas.NewReservedFixedIpSpecificIpAddressSerializer.properties.ip_address"
    """

    network_id: Required[str]
    """
    '#/components/schemas/NewReservedFixedIpSpecificIpAddressSerializer/properties/network_id'
    "$.components.schemas.NewReservedFixedIpSpecificIpAddressSerializer.properties.network_id"
    """

    type: Required[Literal["ip_address"]]
    """
    '#/components/schemas/NewReservedFixedIpSpecificIpAddressSerializer/properties/type'
    "$.components.schemas.NewReservedFixedIpSpecificIpAddressSerializer.properties.type"
    """

    is_vip: bool
    """
    '#/components/schemas/NewReservedFixedIpSpecificIpAddressSerializer/properties/is_vip'
    "$.components.schemas.NewReservedFixedIpSpecificIpAddressSerializer.properties.is_vip"
    """


class NewReservedFixedIPSpecificPortSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    port_id: Required[str]
    """
    '#/components/schemas/NewReservedFixedIpSpecificPortSerializer/properties/port_id'
    "$.components.schemas.NewReservedFixedIpSpecificPortSerializer.properties.port_id"
    """

    type: Required[Literal["port"]]
    """
    '#/components/schemas/NewReservedFixedIpSpecificPortSerializer/properties/type'
    "$.components.schemas.NewReservedFixedIpSpecificPortSerializer.properties.type"
    """


ReservedFixedIPCreateParams: TypeAlias = Union[
    NewReservedFixedIPExternalSerializer,
    NewReservedFixedIPSpecificSubnetSerializer,
    NewReservedFixedIPAnySubnetSerializer,
    NewReservedFixedIPSpecificIPAddressSerializer,
    NewReservedFixedIPSpecificPortSerializer,
]
