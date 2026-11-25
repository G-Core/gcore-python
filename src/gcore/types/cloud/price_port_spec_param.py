# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .price_floating_ip_param import PriceFloatingIPParam
from .ip_assignment_request_param import IPAssignmentRequestParam

__all__ = ["PricePortSpecParam"]


class PricePortSpecParam(TypedDict, total=False):
    floating_ip: PriceFloatingIPParam
    """Floating IP of the new port."""

    ip_assignments: Iterable[IPAssignmentRequestParam]
    """IP addresses of the new port.

    Omit the field to get one address from an IPv4 subnet.
    """

    network_id: str
    """Network of the new port.

    When omitted, it is the network of the subnets in `ip_assignments`, or the
    public network of the region if `ip_assignments` is omitted.
    """
