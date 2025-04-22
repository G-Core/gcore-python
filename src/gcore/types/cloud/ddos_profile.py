# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ddos_profile_field import DDOSProfileField
from .ddos_profile_status import DDOSProfileStatus
from .ddos_profile_template import DDOSProfileTemplate
from .ddos_profile_option_list import DDOSProfileOptionList

__all__ = ["DDOSProfile"]


class DDOSProfile(BaseModel):
    id: int
    """
    '#/components/schemas/GetClientProfileSerializer/properties/id'
    "$.components.schemas.GetClientProfileSerializer.properties.id"
    """

    profile_template: DDOSProfileTemplate
    """
    '#/components/schemas/GetClientProfileSerializer/properties/profile_template'
    "$.components.schemas.GetClientProfileSerializer.properties.profile_template"
    """

    fields: Optional[List[DDOSProfileField]] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/fields'
    "$.components.schemas.GetClientProfileSerializer.properties.fields"
    """

    options: Optional[DDOSProfileOptionList] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/options/anyOf/0'
    "$.components.schemas.GetClientProfileSerializer.properties.options.anyOf[0]"
    """

    profile_template_description: Optional[str] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/profile_template_description/anyOf/0'
    "$.components.schemas.GetClientProfileSerializer.properties.profile_template_description.anyOf[0]"
    """

    protocols: Optional[List[object]] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/protocols/anyOf/0'
    "$.components.schemas.GetClientProfileSerializer.properties.protocols.anyOf[0]"
    """

    site: Optional[str] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/site/anyOf/0'
    "$.components.schemas.GetClientProfileSerializer.properties.site.anyOf[0]"
    """

    status: Optional[DDOSProfileStatus] = None
    """
    '#/components/schemas/GetClientProfileSerializer/properties/status/anyOf/0'
    "$.components.schemas.GetClientProfileSerializer.properties.status.anyOf[0]"
    """
