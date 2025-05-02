# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BaremetalFixedAddress"]


class BaremetalFixedAddress(BaseModel):
    addr: str
    """Address"""

    interface_name: Optional[str] = None
    """Interface name.

    This field will be `null` if `with_interfaces_name=true` is not set in the
    request when listing servers. It will also be `null` if the `interface_name` was
    not specified during server creation or when attaching the interface.
    """

    subnet_id: str
    """The unique identifier of the subnet associated with this address."""

    subnet_name: str
    """The name of the subnet associated with this address."""

    type: Literal["fixed"]
    """Type of the address"""
