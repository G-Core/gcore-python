# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PortCreateParams", "AllowedAddressPair", "IPAssignment"]


class PortCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: Required[int]
    """Region ID where the port is created"""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """

    allowed_address_pairs: Iterable[AllowedAddressPair]
    """A set of zero or more allowed port address pair and/or subnet masks."""

    ip_assignments: Iterable[IPAssignment]
    """IP addresses to assign.

    All subnets must belong to the same network. Repeat a subnet to get several
    addresses from it. Omit the field to get one address from an IPv4 subnet.
    """

    network_id: str
    """Network to create the port in.

    When omitted, it is the network of the subnets in `ip_assignments`, or the
    region's public network if `ip_assignments` is omitted. Every subnet in
    `ip_assignments` must belong to it.
    """

    port_security_enabled: bool
    """
    When true, the network driver enforces port security on this port (anti-spoofing
    checks and security-group filtering apply). Defaults to the network's setting.
    """

    security_group_ids: SequenceNotStr[str]
    """List of security group IDs to attach to the port."""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Tag keys and values
    cannot contain characters from U+0080 to U+00FF. Some tags are read-only and
    cannot be modified by the user. Tags are also integrated with cost reports,
    allowing cost data to be filtered based on tag keys or values.
    """


class AllowedAddressPair(TypedDict, total=False):
    ip_address: Required[str]
    """IP address or subnet of the allowed address pair"""


class IPAssignment(TypedDict, total=False):
    subnet_id: Required[str]
    """ID of the subnet"""

    ip_address: str
    """IP address to assign.

    Omit it to get any free address of the subnet, which is the only option when the
    subnet's free addresses are not known to the caller.
    """
