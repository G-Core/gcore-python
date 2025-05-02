# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FixedAddressShort"]


class FixedAddressShort(BaseModel):
    addr: str
    """IP address"""

    interface_name: Optional[str] = None
    """Interface name.

    This field will be `null` if `with_interfaces_name=true` is not set in the
    request when listing instances. It will also be `null` if the `interface_name`
    was not specified during instance creation or when attaching the interface.
    """

    type: Literal["fixed"]
    """Type of the address"""
