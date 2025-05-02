# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FixedAddressShort"]


class FixedAddressShort(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/addr'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.addr"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.interface_name.anyOf[0]"
    """

    type: Literal["fixed"]
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/type'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.type"
    """
