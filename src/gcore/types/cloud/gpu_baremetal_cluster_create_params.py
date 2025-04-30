# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interface_ip_family import InterfaceIPFamily

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
    project_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: str
    """
    '#/paths/%2Fcloud%2Fv1%2Fai%2Fclusters%2Fgpu%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/ai/clusters/gpu/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    flavor: Required[str]
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/flavor'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.flavor"
    """

    image_id: Required[str]
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/image_id'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.image_id"
    """

    interfaces: Required[Iterable[Interface]]
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/interfaces'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.interfaces"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/name'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.name"
    """

    instances_count: int
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/instances_count'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.instances_count"
    """

    keypair_name: str
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/keypair_name'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.keypair_name"
    """

    password: str
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/password'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.password"
    """

    tags: Dict[str, str]
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/tags'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.tags"
    """

    user_data: str
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/user_data'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.user_data"
    """

    username: str
    """
    '#/components/schemas/CreateAIClusterGPUSerializer/properties/username'
    "$.components.schemas.CreateAIClusterGPUSerializer.properties.username"
    """


class InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class InterfaceNewInterfaceExternalSerializerPydantic(TypedDict, total=False):
    type: Required[Literal["external"]]
    """
    '#/components/schemas/NewInterfaceExternalSerializerPydantic/properties/type'
    "$.components.schemas.NewInterfaceExternalSerializerPydantic.properties.type"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceExternalSerializerPydantic/properties/interface_name'
    "$.components.schemas.NewInterfaceExternalSerializerPydantic.properties.interface_name"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/NewInterfaceExternalSerializerPydantic/properties/ip_family/anyOf/0'
    "$.components.schemas.NewInterfaceExternalSerializerPydantic.properties.ip_family.anyOf[0]"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceExternalSerializerPydantic/properties/port_group'
    "$.components.schemas.NewInterfaceExternalSerializerPydantic.properties.port_group"
    """

    security_groups: Iterable[InterfaceNewInterfaceExternalSerializerPydanticSecurityGroup]
    """
    '#/components/schemas/NewInterfaceExternalSerializerPydantic/properties/security_groups'
    "$.components.schemas.NewInterfaceExternalSerializerPydantic.properties.security_groups"
    """


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/existing_floating_id'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.existing_floating_id"
    """

    source: Required[Literal["existing"]]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.source"
    """


InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/network_id'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.network_id"
    """

    subnet_id: Required[str]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/subnet_id'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.subnet_id"
    """

    type: Required[Literal["subnet"]]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/type'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.type"
    """

    floating_ip: InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticFloatingIP
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/floating_ip'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/interface_name'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/port_group'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.port_group"
    """

    security_groups: Iterable[InterfaceNewInterfaceSpecificSubnetFipSerializerPydanticSecurityGroup]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetFipSerializerPydantic/properties/security_groups'
    "$.components.schemas.NewInterfaceSpecificSubnetFipSerializerPydantic.properties.security_groups"
    """


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/existing_floating_id'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.existing_floating_id"
    """

    source: Required[Literal["existing"]]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.source"
    """


InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class InterfaceNewInterfaceAnySubnetFipSerializerPydantic(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/network_id'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.network_id"
    """

    type: Required[Literal["any_subnet"]]
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/type'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.type"
    """

    floating_ip: InterfaceNewInterfaceAnySubnetFipSerializerPydanticFloatingIP
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/floating_ip'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/interface_name'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.interface_name"
    """

    ip_address: str
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/ip_address'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.ip_address"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/ip_family/anyOf/0'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.ip_family.anyOf[0]"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/port_group'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.port_group"
    """

    security_groups: Iterable[InterfaceNewInterfaceAnySubnetFipSerializerPydanticSecurityGroup]
    """
    '#/components/schemas/NewInterfaceAnySubnetFipSerializerPydantic/properties/security_groups'
    "$.components.schemas.NewInterfaceAnySubnetFipSerializerPydantic.properties.security_groups"
    """


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    existing_floating_id: Required[str]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/existing_floating_id'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.existing_floating_id"
    """

    source: Required[Literal["existing"]]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.source"
    """


InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIP: TypeAlias = Union[
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic(TypedDict, total=False):
    port_id: Required[str]
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/port_id'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.port_id"
    """

    type: Required[Literal["reserved_fixed_ip"]]
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/type'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.type"
    """

    floating_ip: InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticFloatingIP
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/floating_ip'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/interface_name'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/port_group'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.port_group"
    """

    security_groups: Iterable[InterfaceNewInterfaceReservedFixedIPFipSerializerPydanticSecurityGroup]
    """
    '#/components/schemas/NewInterfaceReservedFixedIpFipSerializerPydantic/properties/security_groups'
    "$.components.schemas.NewInterfaceReservedFixedIpFipSerializerPydantic.properties.security_groups"
    """


Interface: TypeAlias = Union[
    InterfaceNewInterfaceExternalSerializerPydantic,
    InterfaceNewInterfaceSpecificSubnetFipSerializerPydantic,
    InterfaceNewInterfaceAnySubnetFipSerializerPydantic,
    InterfaceNewInterfaceReservedFixedIPFipSerializerPydantic,
]
