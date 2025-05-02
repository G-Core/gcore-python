# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FloatingAddress"]


class FloatingAddress(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFloatingAddressSerializer/properties/addr'
    "$.components.schemas.InstanceFloatingAddressSerializer.properties.addr"
    """

    type: Literal["floating"]
    """
    '#/components/schemas/InstanceFloatingAddressSerializer/properties/type'
    "$.components.schemas.InstanceFloatingAddressSerializer.properties.type"
    """
