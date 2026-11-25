# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..ip_assignment_request_param import IPAssignmentRequestParam

__all__ = ["PortPreviewParams"]


class PortPreviewParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    region_id: Required[int]
    """Region ID where the port is created"""

    ip_assignments: Iterable[IPAssignmentRequestParam]
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
