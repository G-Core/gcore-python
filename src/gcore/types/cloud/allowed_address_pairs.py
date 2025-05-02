# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AllowedAddressPairs"]


class AllowedAddressPairs(BaseModel):
    ip_address: str
    """
    '#/components/schemas/AllowedAddressPairsSerializer/properties/ip_address/anyOf/0'
    "$.components.schemas.AllowedAddressPairsSerializer.properties.ip_address.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/AllowedAddressPairsSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.AllowedAddressPairsSerializer.properties.mac_address.anyOf[0]"
    """
