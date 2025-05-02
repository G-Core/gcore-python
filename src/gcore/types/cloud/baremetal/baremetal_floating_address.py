# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BaremetalFloatingAddress"]


class BaremetalFloatingAddress(BaseModel):
    addr: str
    """
    '#/components/schemas/BareMetalFloatingAddressSerializer/properties/addr'
    "$.components.schemas.BareMetalFloatingAddressSerializer.properties.addr"
    """

    type: Literal["floating"]
    """
    '#/components/schemas/BareMetalFloatingAddressSerializer/properties/type'
    "$.components.schemas.BareMetalFloatingAddressSerializer.properties.type"
    """
