# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FixedAddress"]


class FixedAddress(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/addr'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.addr"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.interface_name.anyOf[0]"
    """

    subnet_id: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/subnet_id'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.subnet_id"
    """

    subnet_name: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/subnet_name'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.subnet_name"
    """

    type: Literal["fixed"]
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/type'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.type"
    """
