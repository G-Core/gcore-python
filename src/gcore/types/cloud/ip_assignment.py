# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["IPAssignment"]


class IPAssignment(BaseModel):
    ip_address: str
    """
    '#/components/schemas/PortIpSubnetIdSerializer/properties/ip_address'
    "$.components.schemas.PortIpSubnetIdSerializer.properties.ip_address"
    """

    subnet_id: str
    """
    '#/components/schemas/PortIpSubnetIdSerializer/properties/subnet_id'
    "$.components.schemas.PortIpSubnetIdSerializer.properties.subnet_id"
    """
