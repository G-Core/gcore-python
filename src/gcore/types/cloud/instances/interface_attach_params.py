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

    region_id: int

    ddos_profile: NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile
    """Advanced DDoS protection."""

    interface_name: str
    """Interface name"""

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6 or use dual stack."""

    port_group: int
    """Each group will be added to the separate trunk."""

    security_groups: Iterable[NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup]
    """List of security group IDs"""

    type: str
    """Must be 'external'. Union tag"""


class NewInterfaceExternalExtendSchemaWithDdosddosProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """ID of DDoS profile field"""

    field_name: Optional[str]
    """Name of DDoS profile field"""

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified."""

    value: Optional[str]
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""


class NewInterfaceExternalExtendSchemaWithDDOSDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[NewInterfaceExternalExtendSchemaWithDdosddosProfileField]
    """Protection parameters."""

    profile_template_name: str
    """DDoS profile template name."""


class NewInterfaceExternalExtendSchemaWithDDOSSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class NewInterfaceSpecificSubnetSchema(TypedDict, total=False):
    project_id: int

    region_id: int

    subnet_id: Required[str]
    """Port will get an IP address from this subnet"""

    ddos_profile: NewInterfaceSpecificSubnetSchemaDDOSProfile
    """Advanced DDoS protection."""

    interface_name: str
    """Interface name"""

    port_group: int
    """Each group will be added to the separate trunk."""

    security_groups: Iterable[NewInterfaceSpecificSubnetSchemaSecurityGroup]
    """List of security group IDs"""

    type: str
    """Must be 'subnet'"""


class NewInterfaceSpecificSubnetSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """ID of DDoS profile field"""

    field_name: Optional[str]
    """Name of DDoS profile field"""

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified."""

    value: Optional[str]
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""


class NewInterfaceSpecificSubnetSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[NewInterfaceSpecificSubnetSchemaDDOSProfileField]
    """Protection parameters."""

    profile_template_name: str
    """DDoS profile template name."""


class NewInterfaceSpecificSubnetSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class NewInterfaceAnySubnetSchema(TypedDict, total=False):
    project_id: int

    region_id: int

    network_id: Required[str]
    """Port will get an IP address in this network subnet"""

    ddos_profile: NewInterfaceAnySubnetSchemaDDOSProfile
    """Advanced DDoS protection."""

    interface_name: str
    """Interface name"""

    ip_family: Literal["dual", "ipv4", "ipv6"]
    """Which subnets should be selected: IPv4, IPv6 or use dual stack."""

    port_group: int
    """Each group will be added to the separate trunk."""

    security_groups: Iterable[NewInterfaceAnySubnetSchemaSecurityGroup]
    """List of security group IDs"""

    type: str
    """Must be '`any_subnet`'"""


class NewInterfaceAnySubnetSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """ID of DDoS profile field"""

    field_name: Optional[str]
    """Name of DDoS profile field"""

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified."""

    value: Optional[str]
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""


class NewInterfaceAnySubnetSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[NewInterfaceAnySubnetSchemaDDOSProfileField]
    """Protection parameters."""

    profile_template_name: str
    """DDoS profile template name."""


class NewInterfaceAnySubnetSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class NewInterfaceReservedFixedIPSchema(TypedDict, total=False):
    project_id: int

    region_id: int

    port_id: Required[str]
    """Port ID"""

    ddos_profile: NewInterfaceReservedFixedIPSchemaDDOSProfile
    """Advanced DDoS protection."""

    interface_name: str
    """Interface name"""

    port_group: int
    """Each group will be added to the separate trunk."""

    security_groups: Iterable[NewInterfaceReservedFixedIPSchemaSecurityGroup]
    """List of security group IDs"""

    type: str
    """Must be '`reserved_fixed_ip`'. Union tag"""


class NewInterfaceReservedFixedIPSchemaDDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """ID of DDoS profile field"""

    field_name: Optional[str]
    """Name of DDoS profile field"""

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified."""

    value: Optional[str]
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""


class NewInterfaceReservedFixedIPSchemaDDOSProfile(TypedDict, total=False):
    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[NewInterfaceReservedFixedIPSchemaDDOSProfileField]
    """Protection parameters."""

    profile_template_name: str
    """DDoS profile template name."""


class NewInterfaceReservedFixedIPSchemaSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


InterfaceAttachParams: TypeAlias = Union[
    NewInterfaceExternalExtendSchemaWithDDOS,
    NewInterfaceSpecificSubnetSchema,
    NewInterfaceAnySubnetSchema,
    NewInterfaceReservedFixedIPSchema,
]
