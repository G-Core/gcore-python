# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..interface_ip_family import InterfaceIPFamily
from ..tag_update_list_param import TagUpdateListParam

__all__ = [
    "ServerCreateParams",
    "Interface",
    "InterfaceCreateBareMetalExternalInterfaceSerializer",
    "InterfaceCreateBareMetalSubnetInterfaceSerializer",
    "InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIP",
    "InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "InterfaceCreateBareMetalAnySubnetInterfaceSerializer",
    "InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIP",
    "InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "InterfaceCreateBareMetalReservedFixedIPInterfaceSerializer",
    "InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIP",
    "InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "DDOSProfile",
    "DDOSProfileField",
]


class ServerCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    flavor: Required[str]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/flavor'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.flavor"
    """

    interfaces: Required[Iterable[Interface]]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/interfaces'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.interfaces"
    """

    app_config: Optional[object]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/app_config/anyOf/0'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.app_config.anyOf[0]"
    """

    apptemplate_id: str
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/apptemplate_id'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.apptemplate_id"
    """

    ddos_profile: DDOSProfile
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/ddos_profile'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.ddos_profile"
    """

    image_id: str
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/image_id'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.image_id"
    """

    keypair_name: Optional[str]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/keypair_name/anyOf/0'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.keypair_name.anyOf[0]"
    """

    name_templates: List[str]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/name_templates'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.name_templates"
    """

    names: List[str]
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/names'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.names"
    """

    password: str
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/password'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.password"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/tags'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.tags"
    """

    user_data: str
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/user_data'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.user_data"
    """

    username: str
    """
    '#/components/schemas/CreateBareMetalServerSerializer/properties/username'
    "$.components.schemas.CreateBareMetalServerSerializer.properties.username"
    """


class InterfaceCreateBareMetalExternalInterfaceSerializer(TypedDict, total=False):
    type: Required[Literal["external"]]
    """
    '#/components/schemas/CreateBareMetalExternalInterfaceSerializer/properties/type'
    "$.components.schemas.CreateBareMetalExternalInterfaceSerializer.properties.type"
    """

    interface_name: str
    """
    '#/components/schemas/CreateBareMetalExternalInterfaceSerializer/properties/interface_name'
    "$.components.schemas.CreateBareMetalExternalInterfaceSerializer.properties.interface_name"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/CreateBareMetalExternalInterfaceSerializer/properties/ip_family/anyOf/0'
    "$.components.schemas.CreateBareMetalExternalInterfaceSerializer.properties.ip_family.anyOf[0]"
    """

    port_group: int
    """
    '#/components/schemas/CreateBareMetalExternalInterfaceSerializer/properties/port_group'
    "$.components.schemas.CreateBareMetalExternalInterfaceSerializer.properties.port_group"
    """


class InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalSubnetInterfaceSerializer(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/network_id'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.network_id"
    """

    subnet_id: Required[str]
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/subnet_id'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.subnet_id"
    """

    type: Required[Literal["subnet"]]
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/type'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.type"
    """

    floating_ip: InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIP
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/floating_ip'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/interface_name'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/CreateBareMetalSubnetInterfaceSerializer/properties/port_group'
    "$.components.schemas.CreateBareMetalSubnetInterfaceSerializer.properties.port_group"
    """


class InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalAnySubnetInterfaceSerializer(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/network_id'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.network_id"
    """

    type: Required[Literal["any_subnet"]]
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/type'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.type"
    """

    floating_ip: InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIP
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/floating_ip'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/interface_name'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.interface_name"
    """

    ip_address: str
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/ip_address'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.ip_address"
    """

    ip_family: Optional[InterfaceIPFamily]
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/ip_family/anyOf/0'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.ip_family.anyOf[0]"
    """

    port_group: int
    """
    '#/components/schemas/CreateBareMetalAnySubnetInterfaceSerializer/properties/port_group'
    "$.components.schemas.CreateBareMetalAnySubnetInterfaceSerializer.properties.port_group"
    """


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializer(TypedDict, total=False):
    port_id: Required[str]
    """
    '#/components/schemas/CreateBareMetalReservedFixedIpInterfaceSerializer/properties/port_id'
    "$.components.schemas.CreateBareMetalReservedFixedIpInterfaceSerializer.properties.port_id"
    """

    type: Required[Literal["reserved_fixed_ip"]]
    """
    '#/components/schemas/CreateBareMetalReservedFixedIpInterfaceSerializer/properties/type'
    "$.components.schemas.CreateBareMetalReservedFixedIpInterfaceSerializer.properties.type"
    """

    floating_ip: InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIP
    """
    '#/components/schemas/CreateBareMetalReservedFixedIpInterfaceSerializer/properties/floating_ip'
    "$.components.schemas.CreateBareMetalReservedFixedIpInterfaceSerializer.properties.floating_ip"
    """

    interface_name: str
    """
    '#/components/schemas/CreateBareMetalReservedFixedIpInterfaceSerializer/properties/interface_name'
    "$.components.schemas.CreateBareMetalReservedFixedIpInterfaceSerializer.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/CreateBareMetalReservedFixedIpInterfaceSerializer/properties/port_group'
    "$.components.schemas.CreateBareMetalReservedFixedIpInterfaceSerializer.properties.port_group"
    """


Interface: TypeAlias = Union[
    InterfaceCreateBareMetalExternalInterfaceSerializer,
    InterfaceCreateBareMetalSubnetInterfaceSerializer,
    InterfaceCreateBareMetalAnySubnetInterfaceSerializer,
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializer,
]


class DDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """
    '#/components/schemas/CreateBareMetalDDoSProfileFieldSerializer/properties/base_field/anyOf/0'
    "$.components.schemas.CreateBareMetalDDoSProfileFieldSerializer.properties.base_field.anyOf[0]"
    """

    field_name: Optional[str]
    """
    '#/components/schemas/CreateBareMetalDDoSProfileFieldSerializer/properties/field_name/anyOf/0'
    "$.components.schemas.CreateBareMetalDDoSProfileFieldSerializer.properties.field_name.anyOf[0]"
    """

    field_value: Union[Iterable[object], int, str, None]
    """
    '#/components/schemas/CreateBareMetalDDoSProfileFieldSerializer/properties/field_value'
    "$.components.schemas.CreateBareMetalDDoSProfileFieldSerializer.properties.field_value"
    """

    value: Optional[str]
    """
    '#/components/schemas/CreateBareMetalDDoSProfileFieldSerializer/properties/value/anyOf/0'
    "$.components.schemas.CreateBareMetalDDoSProfileFieldSerializer.properties.value.anyOf[0]"
    """


class DDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """
    '#/components/schemas/CreateDDoSProfileSerializer/properties/profile_template'
    "$.components.schemas.CreateDDoSProfileSerializer.properties.profile_template"
    """

    fields: Optional[Iterable[DDOSProfileField]]
    """
    '#/components/schemas/CreateDDoSProfileSerializer/properties/fields/anyOf/0'
    "$.components.schemas.CreateDDoSProfileSerializer.properties.fields.anyOf[0]"
    """

    profile_template_name: Optional[str]
    """
    '#/components/schemas/CreateDDoSProfileSerializer/properties/profile_template_name/anyOf/0'
    "$.components.schemas.CreateDDoSProfileSerializer.properties.profile_template_name.anyOf[0]"
    """
