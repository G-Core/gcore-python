# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileOptionList"]


class DDOSProfileOptionList(BaseModel):
    active: Optional[bool] = None
    """
    '#/components/schemas/ProfileOptionsSerializer/properties/active/anyOf/0'
    "$.components.schemas.ProfileOptionsSerializer.properties.active.anyOf[0]"
    """

    bgp: Optional[bool] = None
    """
    '#/components/schemas/ProfileOptionsSerializer/properties/bgp/anyOf/0'
    "$.components.schemas.ProfileOptionsSerializer.properties.bgp.anyOf[0]"
    """
