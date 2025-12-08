# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..interface_ip_family import InterfaceIPFamily

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
    """Project ID"""

    region_id: int
    """Region ID"""

    flavor: Required[str]
    """The flavor of the instance."""

    interfaces: Required[Iterable[Interface]]
    """A list of network interfaces for the server.

    You can create one or more interfaces - private, public, or both.
    """

    app_config: Optional[Dict[str, object]]
    """
    Parameters for the application template if creating the instance from an
    `apptemplate`.
    """

    apptemplate_id: str
    """Apptemplate ID. Either `image_id` or `apptemplate_id` is required."""

    ddos_profile: DDOSProfile
    """Enable advanced DDoS protection for the server"""

    image_id: str
    """Image ID. Either `image_id` or `apptemplate_id` is required."""

    name: str
    """Server name."""

    name_template: str
    """
    If you want server names to be automatically generated based on IP addresses,
    you can provide a name template instead of specifying the name manually. The
    template should include a placeholder that will be replaced during provisioning.
    Supported placeholders are: `{ip_octets}` (last 3 octets of the IP),
    `{two_ip_octets}`, and `{one_ip_octet}`.
    """

    password: str
    """For Linux instances, 'username' and 'password' are used to create a new user.

    When only 'password' is provided, it is set as the password for the default user
    of the image. For Windows instances, 'username' cannot be specified. Use the
    'password' field to set the password for the 'Admin' user on Windows. Use the
    '`user_data`' field to provide a script to create new users on Windows. The
    password of the Admin user cannot be updated via '`user_data`'.
    """

    ssh_key_name: Optional[str]
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    user_data: str
    """String in base64 format.

    For Linux instances, '`user_data`' is ignored when 'password' field is provided.
    For Windows instances, Admin user password is set by 'password' field and cannot
    be updated via '`user_data`'. Examples of the `user_data`:
    https://cloudinit.readthedocs.io/en/latest/topics/examples.html
    """

    username: str
    """For Linux instances, 'username' and 'password' are used to create a new user.

    For Windows instances, 'username' cannot be specified. Use 'password' field to
    set the password for the 'Admin' user on Windows.
    """


class InterfaceCreateBareMetalExternalInterfaceSerializer(TypedDict, total=False):
    """Instance will be attached to default external network"""

    type: Required[Literal["external"]]
    """A public IP address will be assigned to the instance."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    ip_family: Optional[InterfaceIPFamily]
    """Specify `ipv4`, `ipv6`, or `dual` to enable both."""

    port_group: int
    """Specifies the trunk group to which this interface belongs.

    Applicable only for bare metal servers. Each unique port group is mapped to a
    separate trunk port. Use this to control how interfaces are grouped across
    trunks.
    """


class InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalSubnetInterfaceSerializer(TypedDict, total=False):
    """
    The instance will get an IP address from the selected network.
    If you choose to add a floating IP, the instance will be reachable from the internet.
    Otherwise, it will only have a private IP within the network.
    """

    network_id: Required[str]
    """The network where the instance will be connected."""

    subnet_id: Required[str]
    """The instance will get an IP address from this subnet."""

    type: Required[Literal["subnet"]]
    """The instance will get an IP address from the selected network.

    If you choose to add a floating IP, the instance will be reachable from the
    internet. Otherwise, it will only have a private IP within the network.
    """

    floating_ip: InterfaceCreateBareMetalSubnetInterfaceSerializerFloatingIP
    """Allows the instance to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    port_group: int
    """Specifies the trunk group to which this interface belongs.

    Applicable only for bare metal servers. Each unique port group is mapped to a
    separate trunk port. Use this to control how interfaces are grouped across
    trunks.
    """


class InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalAnySubnetInterfaceSerializer(TypedDict, total=False):
    network_id: Required[str]
    """The network where the instance will be connected."""

    type: Required[Literal["any_subnet"]]
    """Instance will be attached to a subnet with the largest count of free IPs."""

    floating_ip: InterfaceCreateBareMetalAnySubnetInterfaceSerializerFloatingIP
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
    """Specifies the trunk group to which this interface belongs.

    Applicable only for bare metal servers. Each unique port group is mapped to a
    separate trunk port. Use this to control how interfaces are grouped across
    trunks.
    """


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer(
    TypedDict, total=False
):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer(
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


InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIP: TypeAlias = Union[
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPNewInstanceFloatingIPInterfaceSerializer,
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIPExistingInstanceFloatingIPInterfaceSerializer,
]


class InterfaceCreateBareMetalReservedFixedIPInterfaceSerializer(TypedDict, total=False):
    port_id: Required[str]
    """Network ID the subnet belongs to. Port will be plugged in this network."""

    type: Required[Literal["reserved_fixed_ip"]]
    """An existing available reserved fixed IP will be attached to the instance.

    If the reserved IP is not public and you choose to add a floating IP, the
    instance will be accessible from the internet.
    """

    floating_ip: InterfaceCreateBareMetalReservedFixedIPInterfaceSerializerFloatingIP
    """Allows the instance to have a public IP that can be reached from the internet."""

    interface_name: str
    """Interface name.

    Defaults to `null` and is returned as `null` in the API response if not set.
    """

    port_group: int
    """Specifies the trunk group to which this interface belongs.

    Applicable only for bare metal servers. Each unique port group is mapped to a
    separate trunk port. Use this to control how interfaces are grouped across
    trunks.
    """


Interface: TypeAlias = Union[
    InterfaceCreateBareMetalExternalInterfaceSerializer,
    InterfaceCreateBareMetalSubnetInterfaceSerializer,
    InterfaceCreateBareMetalAnySubnetInterfaceSerializer,
    InterfaceCreateBareMetalReservedFixedIPInterfaceSerializer,
]


class DDOSProfileField(TypedDict, total=False):
    base_field: Optional[int]
    """Unique identifier of the DDoS protection field being configured"""

    field_name: Optional[str]
    """Human-readable name of the DDoS protection field being configured"""

    field_value: object

    value: Optional[str]
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""


class DDOSProfile(TypedDict, total=False):
    """Enable advanced DDoS protection for the server"""

    profile_template: Required[int]
    """Unique identifier of the DDoS protection template to use for this profile"""

    fields: Iterable[DDOSProfileField]
    """
    List of field configurations that customize the protection parameters for this
    profile
    """
