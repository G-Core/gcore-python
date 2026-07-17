# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..interface_ip_family import InterfaceIPFamily

__all__ = [
    "InterfaceAttachParams",
    "AttachInterfaceExternalRequestSerializer",
    "AttachInterfaceExternalRequestSerializerDDOSProfile",
    "AttachInterfaceExternalRequestSerializerDDOSProfileField",
    "AttachInterfaceExternalRequestSerializerSecurityGroup",
    "AttachInterfaceSubnetRequestSerializer",
    "AttachInterfaceSubnetRequestSerializerDDOSProfile",
    "AttachInterfaceSubnetRequestSerializerDDOSProfileField",
    "AttachInterfaceSubnetRequestSerializerSecurityGroup",
    "AttachInterfaceAnySubnetRequestSerializer",
    "AttachInterfaceAnySubnetRequestSerializerDDOSProfile",
    "AttachInterfaceAnySubnetRequestSerializerDDOSProfileField",
    "AttachInterfaceAnySubnetRequestSerializerSecurityGroup",
    "AttachInterfaceReservedFixedIPRequestSerializer",
    "AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile",
    "AttachInterfaceReservedFixedIPRequestSerializerDDOSProfileField",
    "AttachInterfaceReservedFixedIPRequestSerializerSecurityGroup",
]


class AttachInterfaceExternalRequestSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    ddos_profile: Optional[AttachInterfaceExternalRequestSerializerDDOSProfile]
    """Advanced DDoS protection."""

    interface_name: Optional[str]
    """Interface name."""

    ip_family: Optional[InterfaceIPFamily]

    port_group: int
    """Each group will be added to a separate trunk."""

    security_groups: Optional[Iterable[AttachInterfaceExternalRequestSerializerSecurityGroup]]
    """List of security group IDs."""

    type: Literal["external"]


class AttachInterfaceExternalRequestSerializerDDOSProfileField(TypedDict, total=False):
    base_field: Required[int]
    """ID of DDoS profile field."""

    field_value: object
    """Complex value for the DDoS profile field."""

    value: Optional[str]
    """Basic type value."""


class AttachInterfaceExternalRequestSerializerDDOSProfile(TypedDict, total=False):
    """Advanced DDoS protection."""

    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[AttachInterfaceExternalRequestSerializerDDOSProfileField]
    """Protection parameters."""

    profile_template_name: Optional[str]
    """DDoS profile template name."""


class AttachInterfaceExternalRequestSerializerSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class AttachInterfaceSubnetRequestSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    subnet_id: Required[str]
    """Port will get an IP address from this subnet."""

    ddos_profile: Optional[AttachInterfaceSubnetRequestSerializerDDOSProfile]
    """Advanced DDoS protection."""

    interface_name: Optional[str]
    """Interface name."""

    port_group: int
    """Each group will be added to a separate trunk."""

    security_groups: Optional[Iterable[AttachInterfaceSubnetRequestSerializerSecurityGroup]]
    """List of security group IDs."""

    type: Literal["subnet"]


class AttachInterfaceSubnetRequestSerializerDDOSProfileField(TypedDict, total=False):
    base_field: Required[int]
    """ID of DDoS profile field."""

    field_value: object
    """Complex value for the DDoS profile field."""

    value: Optional[str]
    """Basic type value."""


class AttachInterfaceSubnetRequestSerializerDDOSProfile(TypedDict, total=False):
    """Advanced DDoS protection."""

    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[AttachInterfaceSubnetRequestSerializerDDOSProfileField]
    """Protection parameters."""

    profile_template_name: Optional[str]
    """DDoS profile template name."""


class AttachInterfaceSubnetRequestSerializerSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class AttachInterfaceAnySubnetRequestSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    network_id: Required[str]
    """Port will get an IP address in this network subnet."""

    ddos_profile: Optional[AttachInterfaceAnySubnetRequestSerializerDDOSProfile]
    """Advanced DDoS protection."""

    interface_name: Optional[str]
    """Interface name."""

    ip_family: Optional[InterfaceIPFamily]

    port_group: int
    """Each group will be added to a separate trunk."""

    security_groups: Optional[Iterable[AttachInterfaceAnySubnetRequestSerializerSecurityGroup]]
    """List of security group IDs."""

    type: Literal["any_subnet"]


class AttachInterfaceAnySubnetRequestSerializerDDOSProfileField(TypedDict, total=False):
    base_field: Required[int]
    """ID of DDoS profile field."""

    field_value: object
    """Complex value for the DDoS profile field."""

    value: Optional[str]
    """Basic type value."""


class AttachInterfaceAnySubnetRequestSerializerDDOSProfile(TypedDict, total=False):
    """Advanced DDoS protection."""

    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[AttachInterfaceAnySubnetRequestSerializerDDOSProfileField]
    """Protection parameters."""

    profile_template_name: Optional[str]
    """DDoS profile template name."""


class AttachInterfaceAnySubnetRequestSerializerSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


class AttachInterfaceReservedFixedIPRequestSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    port_id: Required[str]
    """Port ID."""

    ddos_profile: Optional[AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile]
    """Advanced DDoS protection."""

    interface_name: Optional[str]
    """Interface name."""

    port_group: int
    """Each group will be added to a separate trunk."""

    security_groups: Optional[Iterable[AttachInterfaceReservedFixedIPRequestSerializerSecurityGroup]]
    """List of security group IDs."""

    type: Literal["reserved_fixed_ip"]


class AttachInterfaceReservedFixedIPRequestSerializerDDOSProfileField(TypedDict, total=False):
    base_field: Required[int]
    """ID of DDoS profile field."""

    field_value: object
    """Complex value for the DDoS profile field."""

    value: Optional[str]
    """Basic type value."""


class AttachInterfaceReservedFixedIPRequestSerializerDDOSProfile(TypedDict, total=False):
    """Advanced DDoS protection."""

    profile_template: Required[int]
    """DDoS profile template ID."""

    fields: Iterable[AttachInterfaceReservedFixedIPRequestSerializerDDOSProfileField]
    """Protection parameters."""

    profile_template_name: Optional[str]
    """DDoS profile template name."""


class AttachInterfaceReservedFixedIPRequestSerializerSecurityGroup(TypedDict, total=False):
    id: Required[str]
    """Resource ID"""


InterfaceAttachParams: TypeAlias = Union[
    AttachInterfaceExternalRequestSerializer,
    AttachInterfaceSubnetRequestSerializer,
    AttachInterfaceAnySubnetRequestSerializer,
    AttachInterfaceReservedFixedIPRequestSerializer,
]
