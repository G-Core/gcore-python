# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ddos_profile_template_field import DDOSProfileTemplateField

__all__ = ["DDOSProfileTemplate"]


class DDOSProfileTemplate(BaseModel):
    id: int
    """
    '#/components/schemas/ClientProfileTemplateSerializer/properties/id'
    "$.components.schemas.ClientProfileTemplateSerializer.properties.id"
    """

    name: str
    """
    '#/components/schemas/ClientProfileTemplateSerializer/properties/name'
    "$.components.schemas.ClientProfileTemplateSerializer.properties.name"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/ClientProfileTemplateSerializer/properties/description/anyOf/0'
    "$.components.schemas.ClientProfileTemplateSerializer.properties.description.anyOf[0]"
    """

    fields: Optional[List[DDOSProfileTemplateField]] = None
    """
    '#/components/schemas/ClientProfileTemplateSerializer/properties/fields'
    "$.components.schemas.ClientProfileTemplateSerializer.properties.fields"
    """
