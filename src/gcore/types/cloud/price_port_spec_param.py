# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .price_floating_ip_param import PriceFloatingIPParam

__all__ = ["PricePortSpecParam", "IPAssignment"]


class IPAssignment(TypedDict, total=False):
    subnet_id: Required[str]
    """ID of the subnet"""

    floating_ip: PriceFloatingIPParam
    """Floating IP of this address of the new port."""

    ip_address: str
    """IP address to assign.

    Omit it to get any free address of the subnet, which is the only option when the
    subnet's free addresses are not known to the caller.
    """


class PricePortSpecParam(TypedDict, total=False):
    floating_ip: PriceFloatingIPParam
    """Floating IP of the new port."""

    ip_assignments: Iterable[IPAssignment]
    """IP addresses of the new port.

    Omit the field to get one address from an IPv4 subnet.
    """

    network_id: str
    """Network of the new port.

    When omitted, it is the network of the subnets in `ip_assignments`, or the
    public network of the region if `ip_assignments` is omitted.
    """
