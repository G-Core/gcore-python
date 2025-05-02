# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..subnet import Subnet
from ...._models import BaseModel

__all__ = ["IPWithSubnet"]


class IPWithSubnet(BaseModel):
    ip_address: str
    """
    '#/components/schemas/PortIpWithSubnetSerializer/properties/ip_address'
    "$.components.schemas.PortIpWithSubnetSerializer.properties.ip_address"
    """

    subnet: Subnet
    """
    '#/components/schemas/PortIpWithSubnetSerializer/properties/subnet'
    "$.components.schemas.PortIpWithSubnetSerializer.properties.subnet"
    """

    subnet_id: str
    """
    '#/components/schemas/PortIpWithSubnetSerializer/properties/subnet_id'
    "$.components.schemas.PortIpWithSubnetSerializer.properties.subnet_id"
    """
