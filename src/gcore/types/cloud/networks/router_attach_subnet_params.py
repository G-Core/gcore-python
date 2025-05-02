# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouterAttachSubnetParams"]


class RouterAttachSubnetParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    subnet_id: Required[str]
    """Subnet ID on which router interface will be created"""

    ip_address: str
    """
    IP address to assign for router's interface, if not specified, address will be
    selected automatically
    """
