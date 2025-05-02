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
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    flavor: Required[str]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/flavor'
    "$.components.schemas.CreateInstanceSerializerV2.properties.flavor"
    """

    interfaces: Required[Iterable[Interface]]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/interfaces'
    "$.components.schemas.CreateInstanceSerializerV2.properties.interfaces"
    """

    volumes: Required[Iterable[Volume]]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/volumes'
    "$.components.schemas.CreateInstanceSerializerV2.properties.volumes"
    """

    allow_app_ports: bool
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/allow_app_ports'
    "$.components.schemas.CreateInstanceSerializerV2.properties.allow_app_ports"
    """

    configuration: Optional[object]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/configuration/anyOf/0'
    "$.components.schemas.CreateInstanceSerializerV2.properties.configuration.anyOf[0]"
    """

    name_templates: List[str]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/name_templates'
    "$.components.schemas.CreateInstanceSerializerV2.properties.name_templates"
    """

    names: List[str]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/names'
    "$.components.schemas.CreateInstanceSerializerV2.properties.names"
    """

    password: str
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/password'
    "$.components.schemas.CreateInstanceSerializerV2.properties.password"
    """

    security_groups: Iterable[SecurityGroup]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/security_groups'
    "$.components.schemas.CreateInstanceSerializerV2.properties.security_groups"
    """

    servergroup_id: str
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/servergroup_id'
    "$.components.schemas.CreateInstanceSerializerV2.properties.servergroup_id"
    """

    ssh_key_name: Optional[str]
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.CreateInstanceSerializerV2.properties.ssh_key_name.anyOf[0]"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/tags'
    "$.components.schemas.CreateInstanceSerializerV2.properties.tags"
    """

    user_data: str
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/user_data'
    "$.components.schemas.CreateInstanceSerializerV2.properties.user_data"
    """

    username: str
    """
    '#/components/schemas/CreateInstanceSerializerV2/properties/username'
    "$.components.schemas.CreateInstanceSerializerV2.properties.username"
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


class Volume(TypedDict, total=False):
    source: Required[Literal["apptemplate", "existing-volume", "image", "new-volume", "snapshot"]]
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/source'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.source"
    """

    apptemplate_id: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/apptemplate_id'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.apptemplate_id"
    """

    attachment_tag: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/attachment_tag'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.attachment_tag"
    """

    boot_index: int
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/boot_index'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.boot_index"
    """

    delete_on_termination: bool
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/delete_on_termination'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.delete_on_termination"
    """

    image_id: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/image_id'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.image_id"
    """

    name: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/name'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.name"
    """

    size: int
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/size'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.size"
    """

    snapshot_id: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/snapshot_id'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.snapshot_id"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/tags'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.tags"
    """

    type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/type_name'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.type_name"
    """

    volume_id: str
    """
    '#/components/schemas/CreateInstanceVolumeSerializerPydantic/properties/volume_id'
    "$.components.schemas.CreateInstanceVolumeSerializerPydantic.properties.volume_id"
    """


class SecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """
