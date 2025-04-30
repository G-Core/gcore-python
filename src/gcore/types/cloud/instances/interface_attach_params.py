# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "InterfaceAttachParams",
    "NewInterfaceExternalExtendSchemaWithDDOS",
    "NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile",
    "NewInterfaceExternalExtendSchemaWithDdosddosProfileField",
    "NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup",
    "NewInterfaceSpecificSubnetSchema",
    "NewInterfaceSpecificSubnetSchemaDDOSProfile",
    "NewInterfaceSpecificSubnetSchemaDDOSProfileField",
    "NewInterfaceSpecificSubnetSchemaSecurityGroup",
    "NewInterfaceAnySubnetSchema",
    "NewInterfaceAnySubnetSchemaDDOSProfile",
    "NewInterfaceAnySubnetSchemaDDOSProfileField",
    "NewInterfaceAnySubnetSchemaSecurityGroup",
    "NewInterfaceReservedFixedIPSchema",
    "NewInterfaceReservedFixedIPSchemaDDOSProfile",
    "NewInterfaceReservedFixedIPSchemaDDOSProfileField",
    "NewInterfaceReservedFixedIPSchemaSecurityGroup",
]


class NewInterfaceExternalExtendSchemaWithDDOS(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"
    """

    ddos_profile: NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ddos_profile/allOf/0'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ddos_profile.allOf[0]"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/interface_name'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.interface_name"
    """

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/ip_family'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.ip_family"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/port_group'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.port_group"
    """

    security_groups: Iterable[NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/security_groups'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.security_groups"
    """

    type: str
    """
    '#/components/schemas/NewInterfaceExternalExtendSchemaWithDdos/properties/type'
    "$.components.schemas.NewInterfaceExternalExtendSchemaWithDdos.properties.type"
    """


class NewInterfaceExternalExtendSchemaWithDdosddosProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/base_field'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.base_field"
    """

    field_name: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_name'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_name"
    """

    field_value: object
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_value"
    """

    value: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.value"
    """


class NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template"
    """

    fields: Iterable[NewInterfaceExternalExtendSchemaWithDdosddosProfileField]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/fields'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.fields"
    """

    profile_template_name: str
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template_name'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template_name"
    """


class NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSchema/properties/id'
    "$.components.schemas.MandatoryIdSchema.properties.id"
    """


class NewInterfaceSpecificSubnetSchema(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"
    """

    subnet_id: Required[str]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/subnet_id'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.subnet_id"
    """

    ddos_profile: NewInterfaceSpecificSubnetSchemaDDOSProfile
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/ddos_profile/allOf/0'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.ddos_profile.allOf[0]"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/interface_name'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/port_group'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.port_group"
    """

    security_groups: Iterable[NewInterfaceSpecificSubnetSchemaSecurityGroup]
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/security_groups'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.security_groups"
    """

    type: str
    """
    '#/components/schemas/NewInterfaceSpecificSubnetSchema/properties/type'
    "$.components.schemas.NewInterfaceSpecificSubnetSchema.properties.type"
    """


class NewInterfaceSpecificSubnetSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/base_field'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.base_field"
    """

    field_name: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_name'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_name"
    """

    field_value: object
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_value"
    """

    value: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.value"
    """


class NewInterfaceSpecificSubnetSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template"
    """

    fields: Iterable[NewInterfaceSpecificSubnetSchemaDDOSProfileField]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/fields'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.fields"
    """

    profile_template_name: str
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template_name'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template_name"
    """


class NewInterfaceSpecificSubnetSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSchema/properties/id'
    "$.components.schemas.MandatoryIdSchema.properties.id"
    """


class NewInterfaceAnySubnetSchema(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"
    """

    network_id: Required[str]
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/network_id'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.network_id"
    """

    ddos_profile: NewInterfaceAnySubnetSchemaDDOSProfile
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ddos_profile/allOf/0'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ddos_profile.allOf[0]"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/interface_name'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.interface_name"
    """

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/ip_family'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.ip_family"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/port_group'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.port_group"
    """

    security_groups: Iterable[NewInterfaceAnySubnetSchemaSecurityGroup]
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/security_groups'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.security_groups"
    """

    type: str
    """
    '#/components/schemas/NewInterfaceAnySubnetSchema/properties/type'
    "$.components.schemas.NewInterfaceAnySubnetSchema.properties.type"
    """


class NewInterfaceAnySubnetSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/base_field'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.base_field"
    """

    field_name: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_name'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_name"
    """

    field_value: object
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_value"
    """

    value: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.value"
    """


class NewInterfaceAnySubnetSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template"
    """

    fields: Iterable[NewInterfaceAnySubnetSchemaDDOSProfileField]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/fields'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.fields"
    """

    profile_template_name: str
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template_name'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template_name"
    """


class NewInterfaceAnySubnetSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSchema/properties/id'
    "$.components.schemas.MandatoryIdSchema.properties.id"
    """


class NewInterfaceReservedFixedIPSchema(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fattach_interface/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/attach_interface'].post.parameters[1].schema"
    """

    port_id: Required[str]
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_id'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_id"
    """

    ddos_profile: NewInterfaceReservedFixedIPSchemaDDOSProfile
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/ddos_profile/allOf/0'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.ddos_profile.allOf[0]"
    """

    interface_name: str
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/interface_name'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.interface_name"
    """

    port_group: int
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/port_group'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.port_group"
    """

    security_groups: Iterable[NewInterfaceReservedFixedIPSchemaSecurityGroup]
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/security_groups'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.security_groups"
    """

    type: str
    """
    '#/components/schemas/NewInterfaceReservedFixedIpSchema/properties/type'
    "$.components.schemas.NewInterfaceReservedFixedIpSchema.properties.type"
    """


class NewInterfaceReservedFixedIPSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/base_field'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.base_field"
    """

    field_name: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_name'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_name"
    """

    field_value: object
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/field_value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.field_value"
    """

    value: Optional[str]
    """
    '#/components/schemas/DeprecatedCreateClientProfileFieldSchema/properties/value'
    "$.components.schemas.DeprecatedCreateClientProfileFieldSchema.properties.value"
    """


class NewInterfaceReservedFixedIPSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template"
    """

    fields: Iterable[NewInterfaceReservedFixedIPSchemaDDOSProfileField]
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/fields'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.fields"
    """

    profile_template_name: str
    """
    '#/components/schemas/DeprecatedCreateDdosProfileSchema/properties/profile_template_name'
    "$.components.schemas.DeprecatedCreateDdosProfileSchema.properties.profile_template_name"
    """


class NewInterfaceReservedFixedIPSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """
    '#/components/schemas/MandatoryIdSchema/properties/id'
    "$.components.schemas.MandatoryIdSchema.properties.id"
    """


InterfaceAttachParams: TypeAlias = Union[
    NewInterfaceExternalExtendSchemaWithDDOS,
    NewInterfaceSpecificSubnetSchema,
    NewInterfaceAnySubnetSchema,
    NewInterfaceReservedFixedIPSchema,
]
