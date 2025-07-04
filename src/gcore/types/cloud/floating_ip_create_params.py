# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["FloatingIPCreateParams"]


class FloatingIPCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    fixed_ip_address: Optional[str]
    """
    If the port has multiple IP addresses, a specific one can be selected using this
    field. If not specified, the first IP in the port's list will be used by
    default.
    """

    port_id: Optional[str]
    """
    If provided, the floating IP will be immediately attached to the specified port.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
